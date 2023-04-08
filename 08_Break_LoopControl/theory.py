"""
Loops
Loop Control: Break

Loops in Python are very versatile. Python provides a set of control statements that we can use to get even more control out of our loops.

Let’s take a look at a common scenario that we may encounter to see a use case for loop control statements.

Take the following list items_on_sale as our example:
"""
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
"""
It’s often the case that we want to search a list to check if a specific value exists. What does our loop look like if we want to search for the value of "knit dress" and print out "Found it" if it did exist?

It would look something like this:
"""
for item in items_on_sale:
  if item == "knit dress":
    print("Found it")
"""
This code goes through each item in items_on_sale and checks for a match. This is all fine and dandy but what’s the downside?

Once "knit_dress" is found in the list items_on_sale, we don’t need to go through the rest of the items_on_sale list. Unfortunately, our loop will keep running until we reach the end of the list.

Since it’s only 5 elements long, iterating through the entire list is not a big deal in this case but what if items_on_sale had 1000 items? What if it had 100,000 items? This would be a huge waste of time for our program!

Thankfully you can stop iteration from inside the loop by using break loop control statement.

When the program hits a break statement it immediately terminates a loop. For example:
"""
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

print("Checking the sale list!")

for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break

print("End of search!")
"""
This would produce the output:

Checking the sale list!
blue shirt
striped socks
knit dress
End of search!

When the loop entered the if statement and saw the break it immediately ended the loop. We didn’t need to check the elements of "red headband" or "dinosaur onesie" at all.

Now let’s break some loops!
Instructions
1.

You have a list of dog breeds you can adopt, dog_breeds_available_for_adoption.

Using a for loop, iterate through the dog_breeds_available_for_adoption list and print() out each dog breed.

Use the <temporary variable> name of dog_breed in your loop declaration.

Remember the structure of a for loop:

for <temporary variable> in <list>:
  <action>

For our loop:

for dog_breed in dog_breeds_available_for_adoption:
  <action>

What action do we want to perform on each iteration of the loop?
2.

Inside your for loop, after you print each dog breed, check if the current element inside dog_breed is equal to dog_breed_I_want. If so, print "They have the dog I want!"

We can put conditional logic in our loops.
"""
num_list = [1, 2, 3, 4]
for num in num_list:
  if num == 2:
    print("We have a 2!")
"""
What might the condition in our loop be to determine if dog_breed_I_want is inside of our list dog_breeds_available_for_adoption?
3.

Add a break statement when your loop has found dog_breed_I_want so that the rest of the list does not need to be checked once we have found our breed.

Think about at what point we want our loop to break. Will it be before or after our print("They have the dog I want!")
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    In this exercise, a break statement is used as the last line in the for loop. If there was any additional code in the for loop after the break, would it execute?

Why does my print statement not need to be indented?

Still have questions? View this exercise's thread in the Codecademy Forums.
"""
