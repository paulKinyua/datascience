import datetime

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

#Write a program that takes the date of birth of a person and the program 
# outputs the age in terms of years,months,days TODAY.
DOB = input("Enter Date of Birth(dd/mm/yyyy): ")
# age = date[-2:]+" "+str(((datetime.now() - datetime.strptime(date,'%d/%m/%Y')).days)/
today = datetime.datetime.now()
x = DOB.split("/")
dateOB = datetime.datetime(int(x[2]), int(x[1]), int(x[0]))
age = today-dateOB
print(f"Days: {age.days}")
years = age.days//365
print(f"Years: {years}")
months = years*12
print(f"Months: {months}")


#task 5 and task 12 are identical 
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if (num1>num2) and (num1>num3) and (num1>num4):
    print(f"Largest number is {num1}")
elif(num2>num1) and (num2>num3) and (num2>num4):
    print(f"Largest number is {num2}")
elif(num3>num1) and (num3>num2) and (num3>num4):
    print(f"Largest number is {num3}")
elif(num4>num1) and (num4>num2) and (num4>num3):
    print(f"Largest number is {num4}")

#task 13 and task 6 are similar
counter  = list(range(1,4))
for i in counter:
    password = (input("Enter password: "))
    email = (input("Enter email: "))
    if(password == "Admin@123"):
        if(email == "admin@mail.com"):
            print("Access Granted")
            break
        else:
            if(counter[2] == i):
                print('Account Locked') 
    else:
        if(counter[2] == i):
            print('Account Locked')

#Write a program that takes input of 2 values and adds them. 
# The program should only accept numbers and floats only 
# or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
range = list(range(0, 500))
for i in range:
    value_one=(input ("Please enter first value:"))
    value_two = (input ("Please enter second value:"))
    try:
        print(int(value_one) + int(value_two))
        break
    except:
        print("invalid character entered")

#Write a program that takes input of someone's basic salary and benefits, 
# adds them to find the gross salary then uses  the gross salary to find the NHIF. 
value_one=int((input ("Please enter basic salary:")))
value_two = int((input ("Please enter benefits:")))
total = value_one+value_two
if total <= 5999:
    nhif=150
    print("NHIF: 150")
elif total >= 6000 and total<=7999:
    nhif=300
    print("NHIF: 300")
elif total >= 8000 and total<=11999:
    print("NHIF: 400")
elif total >= 12000 and total<=14999:
    nhif=500
    print("NHIF: 500")
elif total >= 15000 and total<=19999:
    nhif=600
    print("NHIF: 600")
elif total >= 20000 and total<=24999:
    nhif=750
    print("NHIF: 750")
elif total >= 25000 and total<=29999:
    nhif=850
    print("NHIF: 850") 
elif total >= 30000 and total<=34999:
    nhif=900
    print("NHIF: 900")
elif total >= 35000 and total<=39999:
    nhif=950
    print("NHIF: 950")
elif total >= 40000 and total<=44999:
    nhif = 1000
    print("NHIF: 1,000")
elif total >= 45000 and total<=49999:
    nhif = 1100
    print("NHIF: 1,100")
elif total >= 50000 and total<=59999:
    nhif = 1200
    print("NHIF: 1,200")
elif total >= 60000 and total<=69999:
    nhif = 1300
    print("NHIF: 1,300")
elif total >= 70000 and total<=79999:
    nhif = 1400
    print("NHIF: 1,400")
elif total >= 80000 and total<=89999:
    nhif = 1500
    print("NHIF: 1,500")
elif total >= 90000 and total<=99999:
    nhif = 1600
    print("NHIF: 1,600")
elif total >= 100000:
    nhif = 1700
    print("NHIF: 1,700")

#Continue with the program above, then use  the gross salary to find the NSSF. 
#To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF.
nssf = (6/100)*total
if(nssf>18000):
    print("NSSF:18000")
else:
    print(nssf)

#Continue with the same program and calculate an individual’s NHDF using:
# i.e NHDF = gross_salary *  0.015
nhdf=(total*0.015)
print('NHDF:', nhdf )

#Calculate the taxable income.
#i.e taxable_income = gross salary - (NSSF + NHDF) 
taxable_income = total - (nssf + nhdf) 
print ("Taxable Income:", taxable_income)

#Continue with the same program and find the person's PAYEE using the taxable income above.
if(total<=24000):
    payee = 2400
    print("Personal Relief: 2,400")
elif(total>24000 and total<32333):
    payee = total * (25/100)
    print("PAYEES: ", total * (25/100) ) 
elif(total>32333):
    payee = total * (30/100)
    print("PAYEES: ", total * (30/100) )

#Continue with the same program and calculate an individual’s Net Salary using:
# net_salary = gross_salary - (nhif + nhdf +  nssf + payee)
net_salary=total-(nhif+nhdf+nssf+(payee))
print ('Net Salary', net_salary)