#A set is a data structure that is used to hold only unique values. 
#Values in a set are not usually stored in their original order,
# therefore use set to store values you do not have to access their index.

days = {"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
print(days)

#Remove friday and sunday from the set using methods.
days.remove("friday") #removes first occurrence of value
days.remove("sunday") 
print (days)

#Add them back to the set
days.add('friday')
days.add ('sunday')
print(days)