# 🎓 STUDENT BIO MANAGER (2-student version, no loops)

# Step 1: Input student 1 data
name1 = input("Enter name of Student 1: ")
age1 = input("Enter age: ")
roll1 = input("Enter roll number: ")
address1 = input("Enter address: ")
lang1 = input("Enter favorite language: ")

# Step 2: Input student 2 data
name2 = input("\nEnter name of Student 2: ")
age2 = input("Enter age: ")
roll2 = input("Enter roll number: ")
address2 = input("Enter address: ")
lang2 = input("Enter favorite language: ")

# Step 3: Store both in a dictionary
students = {
    name1: {
        "age": age1,
        "roll": roll1,
        "address": address1,
        "language": lang1
    },
    name2: {
        "age": age2,
        "roll": roll2,
        "address": address2,
        "language": lang2
    }
}

# Step 4: Display all student bios
print("\n📘 ALL STUDENT BIOS:\n")
for student in [name1, name2]:
    print(f"🧑‍🎓 {student}")
    print(f"   🔸 Age     : {students[student]['age']}")
    print(f"   🔸 Roll No : {students[student]['roll']}")
    print(f"   🔸 Address : {students[student]['address']}")
    print(f"   🔸 Language: {students[student]['language']}\n")

# Step 5: Search by name
search_name = input("🔍 Enter a name to search student: ")
if search_name in students:
    s = students[search_name]
    print(f"\n✅ Found: {search_name}")
    print(f"   Age     : {s['age']}")
    print(f"   Roll No : {s['roll']}")
    print(f"   Address : {s['address']}")
    print(f"   Language: {s['language']}")
else:
    print("❌ Student not found.")


# Step 8: Stats
print("\n📊 STATS")
print("Total students:", len(students))

# Step 6: Update a field
name = input("\n✏️ Enter student name to update: ")
field = input("Which field to update (age/roll/address/language): ").lower()
value = input("Enter new value: ")

if name in students:
    if field in students[name]:
        students[name][field] = value
        print("✅ Updated successfully!")
    else:
        print("❌ Invalid field.")
else:
    print("❌ Student not found.")

# Step 7: Delete student
delete_name = input("\n🗑️ Enter name to delete: ")
if delete_name in students:
    del students[delete_name]
    print(f"✅ {delete_name}'s record deleted.")
else:
    print("❌ Student not found for deletion.")

# Step 8: Stats
print("\n📊 STATS")
print("Total students:", len(students))

