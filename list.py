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