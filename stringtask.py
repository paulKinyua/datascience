#first question
name=input("Enter name: ")
print(name.lower())

#second question
sentence_one = "The Dog Breed is German Shepherd"
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_one[8:23])
print(sentence_two[16:30])

#third question
split_string = "The lazy dog; ran so fast; it hit the wall."
x = split_string.split(";")
print(len(x))

#fourth question
special_string = input("Enter name: ") 
test_str = ''.join(letter for letter in special_string if letter.isalnum())
print(test_str)