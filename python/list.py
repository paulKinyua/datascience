# declare an empty list 
dummy_list = [2]

# list properties
#length len(list)
print(len(dummy_list))

# concatination
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c"]
print(list1+list2)

#repitition
print(list1 * 2)

# membership, not sure how it works 
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#“Wednesday” in daysOfTheWeek

# Delete element in a list
del weekdays[6]
print(weekdays)

#Update values in a list
dummy_list[0]=1


#Adding a value at end of list
dummy_list.append("new values")
print(dummy_list)

# you can add to a specific index as well 
#list.insert(index, value)

#create a list called cars and include a number of brands
cars = ["ford", "audi", "BMW", "Toyota", "oranges", "apples", 1, "banana"]
print(cars[2])

#Get values in a section, range or a specific index using colon --- mylist[index where to start : count where to stop]
print(cars[3:5])
print(cars[0:3])
print(cars[:5])
print(cars[5:])
print(cars[-5:7])
print(cars[-5:-1])

#negative indexing

# Create a List of days of the Week. Print the day today using an index.
print(weekdays[1])

new_cars=["Volvo", "Ford", ["Toyota", "Mercedes", ["mazda", "Subaru"]], "Audi"]
model = ["SUV", "Minivan", "Sedan"]
owners = ["Allan", "Ken", "Ivy"]
#insert audi between mazda and Subaru
new_cars[2][2].insert(1,"audi")
print (new_cars)

#adding 2 lists to each other
# use extend function
# use add function 
new_cars.extend(model)
#new_cars.__add__(owners)
print(new_cars)

#remove from a list
#options :
#remove , pop or del
#remove will specify what you exactly want to remove
new_cars.remove("Ford")
print(new_cars)

#pop will remove the specific index, if index is not specified, it will remove the last item on the list
new_cars.pop()
print(new_cars)

#del will remove a specific index as well or clear the entire list
del new_cars
#print(new_cars)

#symmetric difference finds the unique difference between 2 different sets