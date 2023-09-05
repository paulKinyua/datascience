# declaring a class
class Person():
    # declare variables in the class
    name=""
    nationalID=""
    dob=""
    gender=""
    email=""
    phone=""
    details =[]

    #constructor -A special inbuilt method used to 
    #instatiate initial values
    def __init__(self, n, g, e, p) :
        self.name=n
        self.email=e
        self.gender=g
        self.phone=p
        
    def add(self):
        self.details.append(self.name)
        pass

# calling functions from one class to another
class Fetcher():
    Person.name=""
    Person.dob="23/43/66"