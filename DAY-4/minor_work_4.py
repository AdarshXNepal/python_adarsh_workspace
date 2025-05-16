# '''How do you prevent a python print a new line''' 

# print("This a line",end="")
# print(" is continue of line in next line")

# '''Write a recursive function to calculate the sum ot first n natural numbers. '''

# def sum(num):
#     if num==1:
#         return 1
#     else:
#         return num+sum(num-1)

# print(sum(3))

'''Write a python function to print first n lines of the falbuing patletn
***
** for n=3
*   '''

# def pattern(num):
#     for i in range (1,num+1):
#         print("*"*num)
#         print("")
#         num -=1
# pattern(5)

''' Write a bython function to remove a given word from a list and add it at the same time'''

list=["Adarsh","Ramesh","Sanskar"]

def remove(word):
    list.remove(word)
    
def add(word):
    list.append(word)

print(list)
remove("Ramesh")
print(list)
add("Adarsh")
print(list)
    
    