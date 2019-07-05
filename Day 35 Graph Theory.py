
from collections import deque
from src.load_imdb_data import load_imdb_data
from sys import argv, exit
import networkx as nx

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from networkx.algorithms import community
import nxpd

plt.style.use('ggplot')
%matplotlib inline


def shortest_path(actors, movies, actor1, actor2):
    ''' Return the shortest path from actor1 to actor2.
    If there is more than one path, return any of them.
    parameters
    ----------
    actors: dictionary
        Adjacent list with actor(str): movies(set) key-value pairs.
    movies: dictionary
        Adjaceny list with movie(str): actors(set) key-value pairs.
    actor1: str
        Actor to start at.
    Actor2: str
        Actor to search for.
    Returns
    -------
    Path: list
        List of actors and movies that starts at actor 1 and ends at actor2
        or None if there is no such path.
    '''
    Mov = nx.from_dict_of_lists(movies)
    Act = nx.from_dict_of_lists(actors)
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([actor1])
    while len(queue) != 0:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == actor2:
            return path
        # enumerate all adjacent nodes, construct a new path and push it to que
        for neighbor in Mov.neighbors(node):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)

    return None

def shortest_path_multiple(actors, movies, actor1, actor2):
    ''' Return the shortest path from actor1 to actor2.
    If there is more than one path, return any of them.
    parameters
    ----------
    actors: dictionary
        Adjacent list with actor(str): movies(set) key-value pairs.
    movies: dictionary
        Adjaceny list with movie(str): actors(set) key-value pairs.
    actor1: str
        Actor to start at.
    Actor2: str
        Actor to search for.
    Returns
    -------
    Path: list
        List of actors and movies that starts at actor 1 and ends at actor2
        or None if there is no such path.
    '''
    Mov = nx.from_dict_of_lists(movies)
    Act = nx.from_dict_of_lists(actors)
    # maintain a queue of paths
    queue = [[actor1]]
    visited = []
    length = None
    # push the first path into the queue
    path_lst = []
    if actor1 == actor2:
        return 'Actor1 = Actor2'
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # don't look at nodes we've already been to
        if node not in visited:
            neighbours = Mov.neighbors(node)


            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)

                queue.append(new_path)
                # return path if neighbour is actor2
                if neighbour == actor2:
#                     print(new_path)
                    if length == None:
                        length = len(new_path)

                    if neighbour == actor2 and len(new_path) == length:
                        path_lst.append(new_path)
                        print(new_path)
                    if len(new_path) > length:
                        return path_lst
            visited.append(node)
    return None

    def print_path(path):
        """Print out the length of the path and all the nodes in the path.

        Parameters
        ----------
        path: list
            List of node names (strings)

        Returns
        -------
        None
        """
        if path:
            print("length:", (len(path) - 1)/ 2)
            for i, item in enumerate(path):
                if i % 2 == 0:
                    print("    {}".format(item))
                else:
                    print(item)
        else:
            print("No path!")


    if __name__ == '__main__':
        if len(argv) != 4:
            print("Usage: python {} <data_file> <actor1> <actor2>".format(argv[0]))
            exit(1)
        filename = argv[1]
        actor1 = argv[2]
        actor2 = argv[3]
        actors, movies = load_imdb_data(filename)
        print("Searching for shortest path from {} to {}".format(actor1, actor2))
        path = shortest_path(actors, movies, actor1, actor2)
        print_path(path)


def shortest_path_dict(graph, actor1, actor2):
    Q = [actor1]
    path = dict()
    path[actor1] = [actor1]
    while len(Q) != 0:
        node = Q.pop(0)
        if actor2 in node:
            return path[node], path
        for neighbor in graph[node]:
            if neighbor in path: continue
            path[neighbor] = path[node] + [neighbor]
            Q.append(neighbor)
    return None

# call on it
actors_adj={**actors,**movies}
shortest_path(actors_adj, "Kevin Bacon", "Jody Mullins")
