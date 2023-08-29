# Given a variable temperature with a value of 25°C, write an if statement to check if the temperature is above 30°C using the greater than (>) operator.
# temp =int(input("Enter temperature: "))
temp = 25
if temp > 30:
    print(f"temperature above 30°C: {temp}")
else:
    print (f"Temperature below 30°C: {temp}")


#Create a dictionary called stock with items as keys and their quantities as values. Write an if-else statement to check if the quantity of "apples" is zero using the equality (==) operator. 
stock = {"apples":5, "mangos":3, "oranges":12}
if stock["apples"] == 0:
    print("No apples")
else:
    print(f"{stock['apples']} Apples in stock")


#Declare a list called even_numbers containing integers. Write an if statement to check if the first element of the list is an even number using the modulo (%) operator
numbers = [2, 4, 6, 8, 10]
mod = numbers[0] % 2
if(mod == 0):
    print('even')
else:
    print ('odd')


#Imagine you have a list employees containing dictionaries with keys "name", "hours_worked", and "hourly_rate". Write a code snippet using  if statements to calculate the salary for an employee named "Alice" based on her hours worked and hourly rate.
employees = [{"name":"Purity", "hours_worked":10, "hourly_rate":5}, {"name":"Cyrus", "hours_worked":15, "hourly_rate":7}, {"name":"Alice", "hours_worked":10, "hourly_rate":5}, {"name":"Daniel", "hours_worked":12, "hourly_rate":5}]
if(employees[2]['name'] == "Alice"):
    salary = employees[2]['hours_worked'] *employees[2]['hourly_rate']
    print(f"salary is {salary}")
else:
    print("Not found")


# Create a dictionary book_ratings with book titles as keys and their ratings as values. Write an if-elif-else statement to find out if a book "The Adventure" has a rating of 5 or is rated below 2.
book_ratings = {"Harry potter":4, "The great gatsby":5, "The archive":4, "The Adventure" : 4}
if(book_ratings["The Adventure"] == 5):
    print(f"The Adventure has a rating of {book_ratings['The Adventure']}")
elif(book_ratings["The Adventure"] < 2):
    print(f"The Adventure has a rating of {book_ratings['The Adventure']}")

#Suppose you have two sets: set_x and set_y. Write a code snippet using conditional statements to check if the symmetric difference between the two sets is not empty, using the ^ (symmetric difference) operator
set_x = {1,2, 3, 4,5,6,7,8 ,9}
set_y = {11, 12, 13, 14, 15 ,16}

if set_x ^ set_y:
    print (True) # at least one element is different between the sets.
else:
    print(False)
    
# print()