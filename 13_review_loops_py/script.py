# Your code below:
single_digits = range(0,10)

squares = []

for element in single_digits :
  print(element)
  squares.append(element**2)

print(squares)

cubes = [element**3 for element in single_digits ]
print(cubes)
