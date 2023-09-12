trainees = ["John", [2, ["James","Mary"]]]

#question 1
print(trainees[1][0])

#question 2
print(trainees[1][1][0])

#question 3
trainees.append(56)
print(trainees)

#question 4
#option 1, use insert to specify the index
trainees[1][1].insert(1,"Mike")

#option 2
#reasign mary to mike then append mary
#trainees[1][1][1] = "Mike"
#trainees[1][1].append("Mary")
print(trainees)

#question 5
trainees[1][0] = 8
print(trainees)

#question 6
del trainees[1][1][2]
del trainees[0]
print(trainees)

#question 7 
print(len(trainees))