'''FILE HANDLING '''


#openning a file

f=open("file1.txt","r")
text=f.read()
print(text)
f.close()

#openning a file and reading only 5 charachters

f=open("file1.txt","r")
text=f.read(5)
print(text)
f.close()


''' f·readline () - reads only one line'''

'''Modes of opening a file
r open for reading
w open for writing
a open for apending
+ open ofen for updating '''

#writing in a file (changes the current and overwrites in that)

f=open("file1.txt",'w')
f.write("Added text")
f.close()

'''BEST WAY TO OPEN FILE AND CLOSE'''

with open("file1.txt","r") as f:
    a=f.read()
    print(a)
    
