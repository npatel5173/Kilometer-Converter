#user input distance in km
#function convert km to m
#output in m
def convert(km):
  miles = km * 0.6214
  print(format(miles, '.2f'))

km = float(input('Enter a distance in kilometers: '))
convert(km)