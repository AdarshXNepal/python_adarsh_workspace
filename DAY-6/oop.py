
#accessing class values 
class Employee():
    company="Microsoft"
    salary="Rs 12000"

adarsh=Employee() #object  instantaion 
print(f"Adarsh \ncompany:{adarsh.company}\nsalary:{adarsh.salary}")

#adding instance object values 
class Employee():
    company="Microsoft"
    salary="Rs 12000"

adarsh=Employee() #object  instantaion 
adarsh.language="C++"
print(f"Adarsh \ncompany:{adarsh.company}\nsalary:{adarsh.language}")


'''self parameter - refers to object '''

'''constrctuor - initialze the object and prints as a object is created'''

class operation():
    def __init__(self,number):
        self.number=number
        
    def sqr(self):
        print(f" hello world{self.number**2}")

square=operation(5)
square.sqr()

class Calculator():
    def __init__(self,number): ##dunder method calls when object is created 
        self.number=number
        
    def sqr(self):
        print(f"{self.number**2}")

    @staticmethod
    def greet():
        print("Hello")

a=Calculator(2)
a.sqr()
a.greet()


'''class programmer for storing  information of few programmersworking at microseft'''

class programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name,
        self.salary=salary,
        self.pin=pin
    
p1=programmer("adarsh",12343,231)
print(f" {p1.name} {p1.company} {p1.salary} {p1.pin}" )


class card():
    @staticmethod
    def greet():
        print("Hello there")
adarsh=card()
adarsh.greet()
ramesh=card()
ramesh.greet()
