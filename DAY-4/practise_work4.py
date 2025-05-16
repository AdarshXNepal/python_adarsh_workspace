'''FUNCTION '''


def func1():
    print("Hello world")
    
func1()
func1()

#passing argument in function

def greeting(name):
    print(f"Good morning {name}🙏")

greeting("Adarsh")

#default

def greeting(name="Sir"):
    print(f"Good morning {name}🙏")

greeting("Adarsh")
greeting()

#factorial 

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(4))

