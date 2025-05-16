
''' CONDITONAL AND LOOP '''





'''1. Write a program to print multiplication table of a given number using for loop.'''

num=int(input(("enter number for mulipilcation table")))
for i in range (0,11):
    print(f"{num} x {i} = {num*i}\n")
    
'''2. greet person in list of visitors'''

visitor =['Adarsh',"Ramesh","Sanskar","Sandesh"]
for i in visitor:
    print(f"\n ❤️ Welcome {i} to the wedding ceremony\n")
    

'''4. Write a program to find whether a given number is prime or not.'''


num=int(input(("enter number")))
count=0
for i in range(1,num+1):
    if(num%i) ==0 :
        count=count+1
if(count==2):
    print("prime")
else:
    print(" not a prime number")
    
    
'''Write a program to print the following star pattern.
  *
 ***
***** for n = 3'''


n=int(input(("Enter number")))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")
    
'''8. Write a program to print the following star pattern:
*
**
*** for n = 3'''


# n=int(input(("Enter number")))
# for i in range (1,n+1):
#     print(" * "*(2*i-1),end="")
#     print("")

"""9. Write a program to print the following star pattern.
* * *
*   *  for n = 3
* * *  
* * * *
*     * 
*     * for n = 4
* * * * """

n=int(input(("Enter number")))

for i in range (1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")
    
#grade calcaulatoin 
marks=int(input("enter your marks"))

if(marks<=100 and marks>=90):
    print("O")
elif(marks<90 and marks>=80):
    print("E")
elif(marks<80 and marks>=70):
    print("A")
elif(marks<70 and marks>=60):
    print("B")
