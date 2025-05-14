# Student Bio Generator 🧑‍🎓

# Input Section
name = input("Enter your name: ")
age = input("Enter your age: ")
rollno = int(input("Enter your roll number: "))
address = input("Enter your address: ")
college = input("Enter your college name: ")

# Output Section
print(f"\n===== STUDENT BIOGRAPHY : {name.upper()} =====")
print(f"Name       : {name.upper()}")
print(f"Age        : {age}")
print(f"Roll No.   : {rollno}")
print(f"Address    : {address}")
print(f"College    : {college.title()}")

# Bio Description
print(f"\n{name} is a bright and intelligent student.")
print(f"He is {age} years old and studies at {college}.")
print(f"His roll number is {rollno}, and he lives in {address}.\n")