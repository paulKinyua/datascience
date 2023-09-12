my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]

#Print KES
print(my_ds[3][2]['currency'])


#Print 560
print(my_ds[2])


#Print Maths
print(my_ds[3][1])


#In the dictionary with the key currency, add another key “amount” with value 90
my_ds[3][2]['amount'] = 90
print(my_ds)


#Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
# Hint: Strings can be reversed using [::]

#get the digits
num = my_ds[4]

#convert to string
num = str(num)

#reverse sequence
num = num[::-1]

#convert back to int and assign list value
num = int(num)
my_ds[4] = num
print(my_ds)


#Change the name “John” to “Jane” 
#convert tuple to list
ays_list = list(my_ds[5])

#change the value
ays_list[1] = "Jane"

#convert back to tuple
tuple(ays_list)

#reasing the value to the list
my_ds[5] = ays_list
print(my_ds)


