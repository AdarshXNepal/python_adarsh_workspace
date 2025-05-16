#add two numbers

a=int(input("Enter first number:"))
b=int(input("enter second number:"))
c=a+b
print("sum of two numbers is:",c)

#remaninder of two numbers
c=int(input("Enter first number:"))
d=int(input("enter second number:"))
e=c%d
print(f"remainder is {e} ")

#check type of variable assined
a=input()
print(type(a))

#greater than or less than

x=int(input("enter first number:"))
y=int(input("enter second number:"))
if x>y:
    print(f"{x} is greater than {y}")
else:
    print(f"{y} is greater than {x}")

#find square of number 
a=int(input("enter number:"))
b=a**2
print(f"square of {a} is {b}")


# slicing string 

a="adarsh"
print(a[0:3]) #adar
print(a[0:4])

#slicing with skip value

a="adarshrajpoudel"
print(a[0:15:6])

#counting string

print(len(a))

#checking endswith

a.endswith("poudel")

#count occurance
a.count("a")

#captial
a.capitalize()

#find
a.find("raj")

print(
a.replace("raj","don")
)


#check double space in string 

a="adarsh  rajpoudel"
if a.find("  "):
    print("yes")
print(a.replace("  ","doublespace"))
