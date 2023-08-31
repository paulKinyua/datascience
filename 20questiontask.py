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

