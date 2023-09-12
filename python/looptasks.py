#Write a program that displays a numbers 1 to 50 inside a list.
numbers = list(range(1,51))
for i in numbers:
    print(i)

#From 1 above display the ones divisible by 7 or 5 inside a list.
seven = []
five = []
for i in numbers:
    five_check=i%5
    seven_check=i%7
    if( five_check== 0):
        #divisible by 5
        five.append(i)
    if(i%7 == 0):
        #divisible by 7
        seven.append(i)
print(five)
print(seven)

#Find sum and average of values in the range between 10 to 40.
numbers = list(range(10, 40))
size = len(numbers)
total = 0
average = 0
for i in numbers:
    total = total + i
average = total/size
print(f"total: {total}")
print(f"average: {average}")

#Put in a list the first 10 odd numbers between 10 to 50.
numbers = list(range(10, 50))
odd = []
for i in numbers:
    size = len(odd)
    if(size<10):
        #less than 10
        if(i%2 > 0):
            #not even
            odd.append(i)
    else:
        break

print(odd)