"""
Loops
List Comprehensions: Introduction

So far we have seen many of the ideas about using loops in our code. Python prides itself on allowing programmers to write clean and elegant code. We have already seen this with Python giving us the ability to write while and for loops in a single line.

In this exercise, we are going to examine another way we can write elegant loops in our programs using list comprehensions.

To start, let’s say we had a list of integers and wanted to create a list where each element is doubled. We could accomplish this using a for loop and a new list called doubled:
"""
numbers = [2, -1, 79, 33, -45]
doubled = []

for number in numbers:
  doubled.append(number * 2)

print(doubled)
"""
Would output:

[4, -2, 158, 66, -90]

Let’s see how we can use the power of list comprehensions to solve these types of problems in one line. Here is our same problem but now written as a list comprehension:
"""
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)
"""
Let’s break down our example in a more general way:

new_list = [<expression> for <element> in <collection>]

In our doubled example, our list comprehension:

    Takes an element in the list numbers
    Assigns that element to a variable called num (our <element>)
    Applies the <expression> on the element stored in num and adds the result to a new list called doubled
    Repeats steps 1-3 for every other element in the numbers list (our <collection>)

Our result would be the same:

[4, -2, 158, 66, -90]

Instructions
1.

We have been provided a list of grades in a physics class. Using a list comprehension, create a new list called scaled_grades that scales the class grades based on the highest score.

Since the highest score was a 90 we simply want to add 10 points to all the grades in the list.

Re-examine the general structure of a list comprehension:

new_list = [<expression> for <element> in <collection>]

In our case:

    <element> can be any name you want. Since each element represents a grade, it makes sense to call it grade

    The <expression> will be our formula using our grade variable plus ten extra points: grade + 10

    Our <collection> is the list we want to loop through: grades

2.

Print scaled_grades.

Your output should look like this:

[100, 98, 72, 86, 84, 99, 58, 67]

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    In this exercise, the variable from the list comprehension is used to calculate a value. Is it possible to call a function using the variable?

How can I practice outside Codecademy? (video)
Doesn’t 9/5 need to be in parenthesis?

Still have questions? View this exercise's thread in the Codecademy Forums.
"""
