#prompt a user to input a list of 3 cars
car1=input("Enter first car: ")
car2=input("Enter second car: ")
car3=input("Enter third car: ")

#initialise an empty list 
cars = []

#store the cars in a list
cars.append(car1)
cars.append(car2)
cars.append(car3)

#print out the list of items
print(cars)

#remove one car from the list
cars.pop()

#empty the list
cars = []

#delete the list
del cars