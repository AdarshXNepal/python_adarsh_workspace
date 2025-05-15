# --------------------------
# 📝 List (Mutable)
# --------------------------

print("\n--- LIST EXAMPLES ---")

# Define a mixed list
details = ['Adarsh', 'Siddhartha', 25, False]

# Indexing
print("First item:", details[0])

# Slicing
print("First two items:", details[0:2])  # elements 0 and 1

# List methods
l1 = [1, 2, 3, 9, 8, 7, 5, 6]

# Sort
l1.sort()
print("Sorted list:", l1)

# Reverse
l1.reverse()
print("Reversed list:", l1)

# Append an element
l1.append(10)
print("After appending 10:", l1)

students = []  # an empty list to store student names

students.append("Adarsh")
students.append("Rajan")

print(students)  # Output: ['Adarsh', 'Rajan']

# Insert 2 at index 1
l1.insert(1, 2)
print("After inserting 2 at index 1:", l1)

# Count occurrences of 2
print("Count of 2:", l1.count(2))

# Pop from index 1
l1.pop(1)
print("After popping index 1:", l1)

# Remove a specific element
l1.remove(10)
print("After removing 10:", l1)

# More list methods to try later:
# l1.extend([100, 200]) → adds all items from another list

# --------------------------
# 🔒 Tuple (Immutable)
# --------------------------

print("\n--- TUPLE EXAMPLES ---")

a = (1, 2, 3, 4)

# Print tuple
print("Tuple:", a)

# Index of a value
print("Index of 2:", a.index(2))

# Tuple features:
# - Ordered
# - Cannot be changed (immutable)
# - Can be used as keys in dictionaries

# --------------------------
# 🔑 Dictionary (Key-Value Pairs)
# --------------------------

print("\n--- DICTIONARY EXAMPLES ---")

a = {
    "key": "value",
    "harry": "male",
    "male": True,
    "list": ["adarsh", "male"]
}

print("Full dictionary:", a)

# Accessing a key
print("Value at 'list':", a["list"])

# Get all items
print("Items:", a.items())

# Get all keys
print("Keys:", a.keys())

# Update / Add new key-value
a.update({"ankita": "female"})
print("After adding Ankita:", a)

# Get value safely
print("Gender of harry:", a.get("harry"))


#can we add same interger and string value in set (answer is yes)
t=set()
num=int(input("Enter number 18 this is integer"))
t.add(num)
num=(input("Enter number 18 this is string "))
t.add(num)
print(t)

#CHECKING BASIC OF DICTANERY 

fav_lang = {
    "Adarsh": "Python",
    "Adarsh": "JavaScript"  # Overwrites the previous value
}
print(fav_lang)

# More features:
# a.pop("harry") → removes specific key
# a.clear() → clears entire dictionary

# --------------------------
# 📦 Set (Unordered, Unique Elements)
# --------------------------

print("\n--- SET EXAMPLES ---")

s = set()

# Adding elements
s.add(1)
s.add(2)
print("After adding 1 and 2:", s)

# Union (returns new set)
print("Union with {8, 11}:", s.union({8, 11}))

# Pop removes random item
s.pop()
print("After pop:", s)

# Clear the set
s.clear()
print("After clear:", s)

# Again union after clear
print("Union with {8, 11}:", s.union({8, 11}))

# More set methods:
# - s.intersection(set2)
# - s.difference(set2)
# - s.remove(val)

