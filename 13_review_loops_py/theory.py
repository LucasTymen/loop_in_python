"""
Loops
Review
https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-loops/cheatsheet
Good job! In this lesson, you learned

    How to write a for loop.
    How to use range in a loop.
    How to write a while loop.
    What infinite loops are and how to avoid them.
    How to control loops using break and continue.
    How to write elegant loops as list comprehensions.

Let’s get some more practice with these concepts!
Instructions
1.

Create a list called single_digits that consists of the numbers 0-9 (inclusive).

You can use the list() function with range(n) to make a list from 0 through n-1. The command:
"""
print(list(range(5)))
"""
yields:

[0, 1, 2, 3, 4]

2.

Create a for loop that goes through single_digits and prints out each one.

You can write a for loop through a list using this syntax:
"""
for element in list_to_iterate_through:
  print(element)
"""
3.

Before the loop, create a list called squares. Assign it to be an empty list to begin with.

Be sure to create the list before your for loop to get the following steps to work.
4.

Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.

You can square a number by either using:

number_to_square**2

(which takes it to the second power), or using:

number_to_square*number_to_square

which multiplies it by itself.

To append an element to a list, you can use the .append() method:

my_list.append(number_to_add)

5.

After the for loop, print out squares.

We want to print the entire list — call print(squares) outside of your loop
6.

Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.

You can cube a number by either using:

number_to_cube**3

(which takes it to the third power), or using:

number_to_cube*number_to_cube*number_to_cube

which multiplies it by itself twice.

Remember that a list comprehension looks like:

new_list = [element <OPERATED ON IN SOME WAY> for element in old_list]

7.

Print cubes.

Good job!
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    Can I have some more practice with an independent project on what I’ve learned so far?

I’ve heard “developer documentation” mentioned but what is that and how/when/why would I use it? (video)
Is it possible to have a for loop iterate over a list in reverse order without changing the list?

Still have questions? View this exercise's thread in the Codecademy Forums.
"""
