# '''Write a program to read the files poems txt 
# and find out whether it containsthe word twinkle'''

# with open("poems.txt") as f:
#    a=f.read()
#    if "twinkle" in a:
#        print("yes the word twinkle is present")
#    else :
#        print("the word is not present")
       
# '''A file Contains a word "Donkey" muliple times: you need to write a program which reblaces this wotd
# with ###### by updating the sane file. '''

# with open("spam.txt") as f:
#    b=f.read()
#    print(b)
#    if "donkey" in b:
#        print(b.replace("donkey","##"))
       
'''Write va program to find out the line number
Where python is present '''

with open("linefind.txt", 'r') as f:
    i = 1  # Start line number from 1
    while True:
        line = f.readline()
        if not line:  # End of file
            break
        if "python" in line.lower():  # .lower() handles case-insensitivity
            print(f"'python' is present in line {i}")
        i += 1
   
# Copy content from source.txt to copy.txt

with open("source.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as copy:
    copy.write(content)

print("✅ File copied successfully.")

# Check if file1.txt and file2.txt are identical

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    content1 = f1.read()
    content2 = f2.read()

if content1 == content2:
    print("✅ The files are identical.")
else:
    print("❌ The files are different.")

# Wipe out all content in the file

with open("target.txt", "w") as f:
    f.write("")  # Writing empty string clears the file

print("🧹 File content wiped successfully.")
