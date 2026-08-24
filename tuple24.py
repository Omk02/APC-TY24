# Create a tuple of five integers and display it.

numbers = (10, 20, 30, 40, 50)
print(numbers)

# Create a tuple containing five city names.

cities = ("Pune", "Mumbai", "Kolhapur", "Delhi", "Chennai")

print("First City:", cities[0])
print("Last City:", cities[-1])
print("Third City:", cities[2])

# Create a tuple of student names and display total students.

students = ("Amit", "Ravi", "Neha", "Priya", "Kiran")

print("Total Students:", len(students))

# Check whether a given color exists in the tuple.

colors = ("Red", "Blue", "Green", "Yellow")

color = input("Enter color: ")

if color in colors:
    print("Color Found")
else:
    print("Color Not Found")

# Create a tuple of fruits and display each fruit.

fruits = ("Apple", "Banana", "Mango", "Orange")

for fruit in fruits:
    print(fruit)

# Count how many times a number appears.

numbers = (1, 2, 3, 2, 4, 2, 5)

num = int(input("Enter number: "))

print("Count:", numbers.count(num))

# Find index of a given employee ID.

ids = (101, 102, 103, 104, 105)

eid = int(input("Enter Employee ID: "))

print("Index:", ids.index(eid))

# Concatenate two tuples.

t1 = (1, 2, 3)
t2 = (4, 5, 6)

t3 = t1 + t2

print(t3)

# Repeat tuple four times.

t = (1, 2, 3)

print(t * 4)

# Display first five, last five, middle four, alternate and reverse elements.

t = (1,2,3,4,5,6,7,8,9,10)

print("First 5:", t[:5])
print("Last 5:", t[-5:])
print("Middle 4:", t[3:7])
print("Alternate:", t[::2])
print("Reverse:", t[::-1])

# Convert tuple into list and add element.

t = (10, 20, 30)

lst = list(t)
lst.append(40)

print(lst)

# Accept five numbers and convert list into tuple.

lst = []

for i in range(5):
    lst.append(int(input("Enter number: ")))

t = tuple(lst)

print(t)

# Modify tuple by converting to list and back.

t = (10, 20, 30)

lst = list(t)
lst[1] = 25

t = tuple(lst)

print(t)

# Create a tuple and delete it.

t = (1, 2, 3)

del t

# Create nested tuple containing student details.

students = (
    (1, "Amit", 85),
    (2, "Ravi", 78),
    (3, "Neha", 90)
)

for student in students:
    print(student)

# Store ten numbers and calculate sum.

t = (1,2,3,4,5,6,7,8,9,10)

print("Sum:", sum(t))

# Find largest and smallest number in tuple.

t = (12, 45, 8, 67, 23)

largest = smallest = t[0]

for num in t:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)

# Calculate average of elements stored in tuple.

t = (10, 20, 30, 40, 50)

average = sum(t) / len(t)

print("Average:", average)

# Count even and odd numbers.

t = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

even = odd = 0

for num in t:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)

# Determine whether a number exists in tuple.

t = (10, 20, 30, 40, 50)

num = int(input("Enter number: "))

if num in t:
    print("Found")
else:
    print("Not Found")

# Store student details in tuple.

student = (101, "Amit", "CSE", 85)

print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])

# Store employee details.

employee = (101, "Rahul", 50000)

print("Employee ID:", employee[0])
print("Name:", employee[1])
print("Salary:", employee[2])

# Calculate bill details.

prices = (100, 200, 150, 250, 300)

print("Total Bill:", sum(prices))
print("Average Price:", sum(prices)/len(prices))
print("Highest Price:", max(prices))
print("Lowest Price:", min(prices))

# Analyze temperatures of seven days.

temp = (30, 32, 31, 35, 36, 33, 34)

print("Maximum:", max(temp))
print("Minimum:", min(temp))
print("Average:", sum(temp)/len(temp))

# Analyze runs scored in 10 matches.

runs = (45, 67, 120, 88, 150, 99, 55, 101, 34, 76)

print("Total Runs:", sum(runs))
print("Highest Score:", max(runs))
print("Lowest Score:", min(runs))
print("Average Score:", sum(runs)/len(runs))

# Find common elements between two tuples.

t1 = (1, 2, 3, 4, 5)
t2 = (3, 4, 5, 6, 7)

for item in t1:
    if item in t2:
        print(item)

# Merge two tuples and remove duplicates.

t1 = (1, 2, 3)
t2 = (3, 4, 5)

result = tuple(set(t1 + t2))

print(result)

# Count frequency of each element.

t = (1,2,2,3,3,3,4)

for item in set(t):
    print(item, ":", t.count(item))

# Convert tuple into sorted tuple.

t = (5, 2, 8, 1, 9)

ascending = tuple(sorted(t))
descending = tuple(sorted(t, reverse=True))

print("Ascending:", ascending)
print("Descending:", descending)

# Create patient records and perform operations.

patients = (
    (101, "Ram", 25, "A+"),
    (102, "Shyam", 30, "B+"),
    (103, "Amit", 22, "A+")
)

for patient in patients:
    print(patient)

pid = int(input("Enter Patient ID: "))

for patient in patients:
    if patient[0] == pid:
        print("Patient Found:", patient)

print("Total Patients:", len(patients))

blood = input("Enter Blood Group: ")

for patient in patients:
    if patient[3] == blood:
        print(patient)