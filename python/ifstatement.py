#take 3 inputs froma  user and print the largest of the numbers
num1 =int(input("Enter first number: "))
num2 =int(input("Enter second number: "))
num3 =int(input("Enter third number: "))

if (num1>num2 and num1>num3) :
    print(num1)
elif (num2>num1 and num2>num3) :
    print(num2)
elif(num3>num1 and num3>num2) :
    print(num3)

# write a program that checks if a number is divisible by 7
num =int(input("Enter number: "))
mod = num % 7
if mod == "" or mod == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")

#write a program that calculates electricity bill based on the folowing:
#First 50 units     Kshs.20 
#Next 50 units       Kshs.40
#After 100 units   Kshs.100

num1 = float(input("Enter Units: "))
if(num1 <= 50):
    print("KSH. 20")
elif(num1>50 and num1<=100):
    print("KSH. 40")
else:
    print("KSH. 100")