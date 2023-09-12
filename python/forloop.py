#A for loop is used to perform a repetitive task over and over. 
#You can also loop through a list and get individual values as below

#An example of how you can loop through all numbers between a certain range
x= list(range(2,10))
det = 0
for i in x:
  if i % 2 == 0:
   #print(i)
   det = i


#write a loop that prints numbers 0 - 90
x = list(range(0, 90))
det = 0
for i in x:
#   print (i)
    det = i

#write a loop that adds numbers from 0 - 90
sum = 0
x = list(range(0,90))
for i in x:
  sum += i
#print(sum)

# store the first 10 odd numbers between 0 and 50
odd = []
x = list(range(0, 51))
for i in x:
    #check size of list
    if len(odd)<10 :
        #check if number is odd
        if i%2 > 0:
            odd.append(i)
    elif len(odd) == 10:
       break
print(odd)