sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
locations = ["Scoopcademy", ["Gilberts Creamery"], ["Manny’s Scoop Shop"]]
scoops_sold = 0

for locations in sales_data:
  print(locations)
  for element in locations :
    scoops_sold += element

print(scoops_sold)
