#A tuple is a data structure that is used to hold multiple values but the values can not be changed or removed . 
#We say a tuple is immutable. The data inside the tuple is fixed.

days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")

#1. Find wednesday using an index
print(days[2])

#2. Using a function a find the length of the tuple.
print(len(days))

#3. Replace Thursday with Thur
#convert to a list
days_list = list(days)

#manipulate list
days_list[3] = "Thur"

#convert back into tuple and print out resultant days variable
print(tuple(days_list))