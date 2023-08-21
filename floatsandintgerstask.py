# question 1
num = 56.8926
print(round(num))

# question 2
num = 56.8926
print(round(num, 2))

# question 3
num = 56.8926
print(round(num, 3))

#question 4
#explode the value using the .
num = str(56.8926)
x = num.split(".")
# split the string to 2 parts
num1 = x[1][0:1]
num2 = x[1][1:(len(x[1]))] #(-1))
print(num1+"."+num2)

