# declaring a class
class Person():
    # declare variables in the class
    name=""
    nationalID=""
    dob=""
    gender=""
    email=""
    phone=0
    details =[]

    #constructor -A special inbuilt method used to 
    #instatiate initial values
    def __init__(self, n, g, e, p) :
        self.name=n
        self.email=e
        self.gender=g
        self.phone=p
        self.add()
        
    def add(self):
        self.details.append(self.name)
        self.details.append(self.email)
        self.details.append(self.gender)
        self.details.append(self.phone)
        pass

# p1 = Person("John", "Male", "John@gmail.com", 792664527)
# print(p1.phone)
# print(type(p1))
# print(p1.details)

# p1.add()
# print(p1.details)

p2=Person(input("Enter Name:"),
          input("Enter Gender:"),
          input("Enter Email:"),
          input("Enter Phone:")) 
# p2.add()
print(p2.details)