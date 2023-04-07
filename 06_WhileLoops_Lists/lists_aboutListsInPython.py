"""
    Docs/
    Python/
    Lists

Lists

A list in Python is a sequence data type used for storing a comma-separated collection of objects in a single variable. Lists are always ordered and can contain different types of objects (strings, integers, booleans, etc.). Since they are mutable data types, lists are a good choice for dynamic data (that may be added or removed over time).
Syntax
"""
# With square brackets
list_a = []

# With built-in function
list_b = list()
"""
Lists can either be defined with square brackets ([]) or with the built-in list() constructor method. In any case, the values initially passed to the new list must be comma-separated.

The following example showcases how lists can hold items of the same type or a mix of different types:
"""
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_2 = ["one", 2, "3"]
"""
Stacks and Queues

Python lists can also be made to behave like stacks and queues.

Stacks follow a “last-in, first-out” insertion order. This behavior can be showcased with the .append() and .pop() methods for adding to and removing from the top of the stack, respectively:
"""
stack_example = ["a", "b", "c"]
print(stack_example)
# Output: ['a', 'b', 'c']

stack_example.append(1)
stack_example.append(2)
stack_example.append(3)
print(stack_example)
# Output: ['a', 'b', 'c', 1, 2, 3]

stack_example.pop()
stack_example.pop()
print(stack_example)
# Output: ['a', 'b', 'c', 1]
"""
Queues follow a “first-in, first-out” insertion order and also utilize the .append() and .pop() methods:
"""
queue_example = ["a", "b", "c"]
print(queue_example)
# Output: ['a', 'b', 'c']

queue_example.append(1)
queue_example.append(2)
print(queue_example)
# Output: ['a', 'b', 'c', 1, 2]

queue_example.pop(0)
print(queue_example)
# Output: ['b', 'c', 1, 2]
"""
While using a list as a queue is possible, it is not efficient because applying .pop() to the first item requires shifting all remaining items by one spot and reassigning indices. Instead, a deque object from the collections module should be used to efficiently add/remove from a queue.
Lists

.append()
    Adds an item to end of the list.
.clear()
    Removes all items from the list.
.copy()
    Returns a shallow copy of a list.
.count()
    Searches a list for a particular item and returns the number of matching entries found.
.extend()
    Adds list elements to end of the list.
.index()
    Finds the first occurence of a particular value within the list.
.insert()
    Adds an item at a specified index in the list.
.pop()
    Removes an item from a list while also returning it.
.remove()
    Removes an item from a list by passing in the value of the item to be removed as an argument.
.reverse()
    Reverse the elements in the list.
.sort()
    Sorts the contents of the list it is called on.

Interested in helping build Docs? Read the Contribution Guide or share your thoughts in this feedback form.
Edit on GitHub
"""
