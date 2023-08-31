#Write a program that prompts the user to enter the base and height of a triangle and returns its area.
base = int(input("Enter Base: "))
height=int ( input (" Enter Height :"))
area=(1/2)*base*height  #Formula for Area of Triangle
print(f'Area is {area}')

#Write a program that prompts the user to enter a number. 
#Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
numb=int(input('enter any Number: '))   #Taking Input from User
if numb%2==0:#Checking if Even
    print ('Even')
else:
    print ('Odd')


#Write a program that prompts the user to enter a phone number.
#Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254…
number = input("Enter Phone number: ")
#find if the fist character is 0
# print(len(number))
# print(number[1:len(number)])
if(number[0:1] == 0 or number[0:1] == '0'):
    print(f"+254{number[1:len(number)]}")
elif(number[0:1] == '+'):
    print(number)
else:
    print("Invalid phone number")

#Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email.
mail = input("Enter Email Address: ")
if "@" not in mail:    #checking if @ symbol exists
    print("Invalid mail")
else:
    print("Valid email")

#Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. 
# Return the largest of the three. Do this without using the the inbuilt max () function!
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if (num1>=num2) and (num1>=num3):
    print(f"Largest number is {num1}")
elif(num2>=num1) and (num2>=num3):
    print(f"Largest number is {num2}")
else:
    print(f"Largest number is {num3}")

#Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. 
# If the password is correct access is granted. After you show them a message , the account is blocked.
# password = (input("Enter password: "))
# counter = 0
# if(password == "admin@123"):
#     print("access granted")
# else:
#     if(counter<4):
#         counter = counter+1
#         password = (input("Enter password: "))
#     else:
#         print ("Account locked!")

counter  = list(range(1,5))
for i in counter:
    password = (input("Enter password: "))
    if(password == "admin@123"):
        print("Access Granted")
        break
    else:
        if(counter[3] == i):
            print('Account Locked')

#Write that prompts the user to input student marks. The input should be between 0 and 100.
# Then output the correct grade: A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
grade = int(input("Enter marks: "))
if(grade < 0) and (grade > 100):
    print("invalid marks entered")
else:
    if((grade >=80)):
        print("Grade : A")
    elif(grade < 80) and (grade > 59):
        print("Grade : B")
    elif(grade <= 59) and (grade >= 49):
        print("Grade : C")
    elif(grade < 49) and (grade >= 40):
        print("Grade : D")
    elif(grade < 40):
        print("Grade : E")

#Write a program that takes as input the speed of a car e.g 80. 
# If the speed is less than 70, it should print “Ok”. 
# Otherwise, for every 5 km/s above the speed limit (70), 
# it should give the driver one demerit point and print the total number of demerit points.
speed = int(input("Enter speed: "))
if(speed<=70):
    print("ok")
else:
    #find difference
    differnce = speed-70
    #floor operation to find points
    points = differnce//5
    if(points >= 12 ):
        print("License suspended")
    else:
        print(f"Points: {points}")

#Write a program called stars. 
# It should prompt the user for a number, and it should print the number of stars till the number entered.
number_of_stars=int(input("Enter number of stars: "))
list = list(range(1,(number_of_stars+1)))
for i in list:
    print("*"*i)

#Write a program that calculates the total stock in a company from the array/list 
# below if we know that the stock is the last digit in every array/list.

prods = [["omo","30kshs","300"], ["milk","50kshs","200"],["bread","45kshs","359"], ["coffee","5kshs","79"]]
totalstock = int(prods[0][2]) + int(prods[1][2]) +int(prods[2][2]) + int(prods[3][2])
print(totalstock)

