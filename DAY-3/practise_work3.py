''' CONDITONAL AND LOOP '''

#check age is >18

age=int(input('Enter your age'))
if age>18:
    print("eligible to vote")
else:
    print("not eligible")
    
    
#loop

#1.while 'loop'
i=0
while i<5:
    print(i)
    i=i+1
    
# #loop with list and else

l=[1,2,3,4,5,6]

for i in l:
    print(i)
else:
    print("loop with list and else ")
    
# #range

for i in range(0,6):
    print(i)
    
#break

for i in range(0,6):
    print(i)
    if(i==3):
        break
    
#continue 
for i in range(0,6):
    print(i)
    if(i==3):
        continue
    print (i)
    


