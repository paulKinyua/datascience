# Big O - How does a function behave when n grows?
# O(1) - takes the same time to execute the funtion
#O(n) - As n grows, so does the time it takes to execute the function 

# - Comprehension
# comprenhension is an effective way python uses to create data structures such as lists, dictionaries, and sets
# Comprehensions are often used to perform some operation or filtering on a data structure (e.g., a list or range) 
#and construct a new data structure from the results.

#examples of comprehension include:
# List Comprehension:
#    -Used to create lists.
#   - Syntax: [expression for element in iterable if condition]
#example
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers if x % 2 == 0]
print(squared_numbers)

# Dictionary Comprehensions :
#   - Used to create dictionaries.
#   - Syntax: {key_expression: value_expression for element in iterable if condition}
#example
names = ['Alice', 'Bob', 'Charlie']
name_lengths = {name: len(name) for name in names}
print(name_lengths)

#Set Comprehension:
#   - Used to create sets.
#   - Syntax: {expression for element in iterable if condition}
#example
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = {x for x in numbers}
print(unique_numbers)

#Generator Expression:

#   - Similar to list comprehensions but creates a generator object rather than a list.
#   - Syntax: (expression for element in iterable if condition)
numbers = [1, 2, 3, 4, 5]
squared_numbers_generator = (x**2 for x in numbers if x % 2 == 0)
print(squared_numbers)

#-------------------------------------------------------------------------------------------
# - Map
#this is a built-in function used for applying a specified function to each item in an iterable (e.g., a list, tuple, or string)
# and returning an iterable (typically a map object or a list) containing the results of applying that function.
# basic syntax would look like this:
# --- map(function, iterable, ...) ---

#   -function: This is the function that you want to apply to each element of the iterable.
#   -iterable: This is the iterable (e.g., a list, tuple, or string) whose elements you want to process with the function.

#Map Example# Define a function to double a number
def double(x):
    return x * 2

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use map() to apply the double function to each element in the list
doubled_numbers = map(double, numbers)

# Convert the map object to a list to see the results
result_list = list(doubled_numbers)

# Output: [2, 4, 6, 8, 10]
print(result_list)

#-------------------------------------------------------------------------------------------
# - lambda
# Lambda functions are anonymous functions and they can be used wherever regular functions are required.
#  They come with some restrictions which we will discuss later on.
#Lambda functions are used for creating small, simple functions without the need 
# to formally define a named function using the def keyword.
#Syntax : lambda arguments: expression
#   lambda: The lambda keyword is used to indicate the start of a lambda function.
#   arguments: These are the input parameters (arguments) that the lambda function takes. You can have zero or more arguments, separated by commas.
#   expression: This is the single expression or operation that the lambda function performs. The result of this expression is automatically returned by the lambda function.

#example
square = lambda x: x**2
result = square(5)  # result will be 25
print(result)

#using lambda with map
numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)

#using lambda with filter
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#-------------------------------------------------------------------------------------------
#test how long your program takes to loop through 10, 000 values against 10,000,000
def tenThousand():
    for i in range (1 , 10001 ):
        print(i)
    pass

def tenMillion():
    for i in range(1, 10000001):
        print(i)
    pass


#create a list with random values and sort the list in ascending order without using .sort
random = [4, 2, 1, 8, 3, 7, 9, 5]
sortedList = sorted(random)
print(sortedList)


#generate numbers between 1000 and 10,000 and write only the ones divisible by 7 in a .txt file
numbers = list(range(1000, 10001))
squared_numbers = [x for x in numbers if x % 7 == 0]
# result = ' '.join(squared_numbers)
#convert to string
result_string = ', '.join(map(str, squared_numbers))
file_path = 'divisible_by_7.txt'
with open(file_path, 'w') as file:
    # Write content to the file
    file.write(result_string)
    
# print(squared_numbers)