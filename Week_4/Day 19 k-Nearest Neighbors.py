import numpy as np
import pandas as pd
from collections import Counter
from sklearn.datasets import make_classification
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import sys
from knn_visualization import plot_decision_boundary


def euclidean_distance(a, b):
    """Compute the euclidean_distance between two numpy arrays.

    Parameters
    ----------
    a: numpy array
    b: numpy array

    Returns
    -------
    distance: float
    """
    return np.sqrt(a - b)**2


def cosine_distance(a, b):
    """Compute the cosine_distance between two numpy arrays.

    Parameters
    ----------
    a: numpy array
    b: numpy array

    Returns
    -------
    distance: float
    """
    return 1 -(np.dot(a, b)/np.array() (np.linalg.norm(a) * np.lingalg.norm(b)))


class KNNClassifier:
    """Classifier implementing the k-nearest neighbors algorithm.

    Parameters
    ----------
    k: int, optional (default = 5)
        Number of neighbors that get a vote.
    distance: function, optional (default = euclidean)
        The distance function to use when computing distances.
    """

    def __init__(self, k=5, distance=euclidean_distance):
        """Initialize a KNearestNeighbors object."""
        self.k = k
        self.distance = distance

    def fit(self, X, y):
        """Fit the model using X as training data and y as target labels.

        According to kNN algorithm, the training data is simply stored.

        Parameters
        ----------
        X: numpy array, shape = [n_observations, n_features]
            Training data.
        y: numpy array, shape = [n_observations,]
            Target labels.

        Returns
        -------
        self
        """
        self.X = X
        self.y = y
        return self.X, self.y


    def predict(self, X):
        """Return the predicted labels for the input X test data.

        Assumes shape of X is [n_test_observations, n_features] where
        n_features is the same as the n_features for the input training
        data.

        Parameters
        ----------
        X: numpy array, shape = [n_observations, n_features]
            Test data.

        Returns
        -------
        result: numpy array, shape = [n_observations,]
            Predicted labels for each test data sample.

        """
        # get label feature,
        # pass a vector of features X and compare to other points of feature vector
        # get the distances of that
        # sort them and get the top k
        distance(self.X, X)



    def predict_proba(self, X):
        """Return the predicted probabilities of each class.

        Assumes shape of X is [n_test_observations, n_features] where
        n_features is the same as the n_features for the input training
        data.

        Parameters
        ----------
        X: numpy array, shape = [n_observations, n_features]
            Test data.

        Returns
        -------
        result: numpy array, shape = [n_observations, n_classes]
            Predicted probabilities for each class, for each row.
        """
        # want to get the probablity that x is a horse given 3 horses 2 dogs = 3/2

if __name__ == '__main__':
    pass
