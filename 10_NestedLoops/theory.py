"""
Loops
Nested Loops

Loops can be nested in Python, as they can with other programming languages. We will find certain situations that require nested loops.

Suppose we are in charge of a science class, that is split into three project teams:

project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

Using a for or while loop can be useful here to get each team:

for team in project_teams:
  print(team)

Would output:

["Ava", "Samantha", "James"]
["Lucille", "Zed"]
["Edgar", "Gabriel"]

But what if we wanted to print each individual student? In this case, we would actually need to nest our loops to be able to loop through each sub-list. Here is what it would look like:

# Loop through each sublist
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student)

This would output:

Ava
Samantha
James
Lucille
Zed
Edgar
Gabriel

Let’s practice writing a nested loop!
Instructions
1.

We have provided the list sales_data that shows the number of scoops sold for different flavors of ice cream at three different locations: Scoopcademy, Gilberts Creamery, and Manny’s Scoop Shop.

We want to sum up the total number of scoops sold across all three locations. Start by defining a variable scoops_sold and set it to zero.
2.

Loop through the sales_data list using the following guidelines:

    For our temporary variable of the for loop, call it location.
    print() out each location list.

Since we have a two-dimensional list, our first loop will iterate over the three sublists. Let’s revisit the structure of a for loop:

for <temporary variable> in <collection>:
  <action>

Our <temporary variable> will need to be called location and we will be iterating over our sales_data collection. What will be our action?

Also, if you added additional print statements while working on your loop, remove or comment them out to continue.
3.

Within our sales_data loop, nest a secondary loop to go through each location sublist element and add the element value to scoops_sold.

By the end, you should have the sum of every number in the sales_data nested list.

We want one loop inside of another:

for location in sales_data:
  # Some Action
  for <temporary variable> in location
    # Some Action

4.

Print out the value of scoops_sold outside of the nested loop.

Don’t forget to unindent the print() statement, otherwise, it may run as part of your loop. Also, if you added any extra print statements while working on your loop, remove or comment them out to continue.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
Community Forums

Here are some helpful links to the top questions asked by coders about this exercise:

    This exercise shows the nested loop using the variable from the outer loop. Does the nested loop always need to use the variable from the outer loop?

How does += work?

Still have questions? View this exercise's thread in the Codecademy Forums.
"""
