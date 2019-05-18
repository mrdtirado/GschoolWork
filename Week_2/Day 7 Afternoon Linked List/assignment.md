# Creating a Linked List
Today, we'll be creating a linked list.  If you look in the ```src``` folder, you'll see two pieces of starter code: ```node.py``` and ```linked-list.py```.  Your task for the afternoon will be to fill these pieces of code in, and reproduce the functionality of a python list with your linked-list class.

## Part 1 - Build a Node Class
1. We're going to start with a very basic node class.  A node is an object that has some value (it can be a number, or a string, or really anything).  Start by filling out the defined functions.  Your node class should have two attributes ```value``` and ```next```.  Value should be set equal to the data that the node is storing, and next should be set equal to the next node in the class.  If you don't have a node to point to, you can start by having it equal to ```None```.

2. The Node class we've written allows the values of nodes to be of any type.  Python lists allow for any type as well, but we might prefer to enforce that all of our members are of the same type.  Use inheritance to create a ```TypedNode``` class.  Here, you'll only need to redefine the ```__init__``` and ```set_value``` functions.

## Part 2 - Building a Linked List
Typing ```dir([])``` into a Python interpreter gets you a list of all the methods that python lists have.  To begin with, we'll focus on the normal methods.  

3. Begin with the __init__ method.  The init method should take in a python list, and transform it into a linked list.  Your linked list class should have an attribute ```head```, that is the first node in your list.  Other nodes should be accessed by iterating through the node classes.  You are free to store other attributes that you might find useful as well.

You'll likely end up writing the same code in the ```append``` class as you do in the init class, so you probably will want to define that method at this time as well, and simply have ```init``` call it.

<b>Hint -</b> think about the time complexity of adding in new data to the end of a linked list.  Can you make this an O(1) operation by adding an additional attribute?

4. Define the ```count``` method.  Again, think about the time complexity associated with how you are approaching this.  It can be an O(1) operation *if* you have the right attribute.

5. Define ```pop```.  If you've never used pop on a python list, try it out!  What is happening when you use it?  Reproduce this logic in your linked list.  Be careful, if you have helper attributes for the previous steps, you'll need to make sure they are not made incorrect by this process.

6. Define ```extend```.  Extend should take in another LinkedList object, and extend the list this way.  If you have the right helpers, this should actually be pretty easy.

7. Define ```insert```.  Insert should take two arguments, both the value, and the position in the linked list (e.g. 5, 0 would mean that you are inserting a new node at the head position, with value of 5.).  During step 1, we had you use append to fill in the list in the ```__init__``` function.  How would you use the ```insert``` function to avoid using ```append```?

8. Define ```reverse```.  Here, you should be heavily leveraging functions you've already defined.

9. Define ```copy```.  Note, that it is not sufficient to simply make a new instance of the head node.

## Part 3: Challenge Questions
10. Define a ```TypedLinkedList```.  Here, in addition to passing in the data in a list, you'll need to provide a variable type.  You'll want to leverage inheritance from your linked list, as well as the TypedNode class you defined in part 1.

11. Define ```sort```.  This morning, we used list slicing and indexing to perform MergeSort and HeapSort, but slicing is not possible with linked lists.  It is possible to do MergeSort on a linked list, however, you need to define a helper function that will merge two sorted linked lists. Note, it is cheating to use python arrays as *any* type of container for this function, but you can use linked lists containing linked lists.

