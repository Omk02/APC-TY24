# Q1. Write a Python program to create a file named student.txt and write the student's name, roll number, branch, and semester into the file.
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
branch = input("Enter branch: ")
semester = input("Enter semester: ")

with open("student.txt", "w") as file:
    file.write("Student Name: " + name + "\n")
    file.write("Roll Number: " + roll_no + "\n")
    file.write("Branch: " + branch + "\n")
    file.write("Semester: " + semester + "\n")

print("Student details written successfully to student.txt")


# Q2. Write a program to open a text file and display its complete contents.
with open("student.txt", "r") as file:
    content = file.read()

print(content)


# Q3. Write a program to append additional student information to an existing file without deleting its previous contents.
info = input("Enter additional information: ")

with open("student.txt", "a") as file:
    file.write(info + "\n")

print("Information appended successfully to student.txt")


# Q4. Write a program to read a text file line by line and display each line separately.
with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())


# Q5. Write a program to count and display the total number of lines present in a text file.
with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))


# Q6. Write a program to count the total number of words present in a text file.
with open("student.txt", "r") as file:
    content = file.read()

words = content.split()
print("Total number of words:", len(words))


# Q7. Write a program to count the total number of characters in a text file, including spaces.
with open("student.txt", "r") as file:
    content = file.read()

print("Total number of characters:", len(content))


# Q8. Write a program to read a text file and display its lines in reverse order.
with open("student.txt", "r") as file:
    lines = file.readlines()

print("File contents in reverse order:")
for line in reversed(lines):
    print(line.strip())


# Q9. Read a text file and count the number of vowels and consonants present in the file.
with open("student.txt", "r") as file:
    content = file.read().lower()

vowels = 0
consonants = 0
for ch in content:
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print("Total vowels:", vowels)
print("Total consonants:", consonants)


# Q10. Read a text file and calculate the number of alphabets, digits, spaces, and special characters.
with open("student.txt", "r") as file:
    content = file.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for ch in content:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        special += 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)


# Q11. Read a text file and find the longest word present in the file.
with open("student.txt", "r") as file:
    words = file.read().split()

longest_word = max(words, key=len)
print("Longest word in the file:", longest_word)


# Q12. Read a text file and count how many times each word occurs. Display the result using a dictionary.
with open("student.txt", "r") as file:
    words = file.read().split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word frequency:", word_count)


# Q13. Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears.
search_word = input("Enter word to search: ")

count = 0
line_numbers = []

with open("student.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        occurrences = line.count(search_word)
        if occurrences > 0:
            count += occurrences
            line_numbers.append(line_number)

print("Word found", count, "times")
print("Found on lines:", line_numbers)


# Q14. Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file.
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

with open("student.txt", "r") as file:
    content = file.read()

content = content.replace(old_word, new_word)

with open("student_updated.txt", "w") as file:
    file.write(content)

print("Word replaced successfully. Saved to student_updated.txt")


# Q15. Read a Python source file and create another file after removing single-line comments.
with open("sample.py", "r") as file:
    lines = file.readlines()

cleaned_lines = []
for line in lines:
    if line.strip().startswith("#"):
        continue
    if "#" in line:
        line = line[:line.index("#")].rstrip() + "\n"
    cleaned_lines.append(line)

with open("sample_no_comments.py", "w") as file:
    file.writelines(cleaned_lines)

print("Comments removed successfully. Saved to sample_no_comments.py")


# Q16. Read a text file and create another file containing the same text in uppercase.
with open("student.txt", "r") as file:
    content = file.read()

with open("student_upper.txt", "w") as file:
    file.write(content.upper())

print("Uppercase file created successfully: student_upper.txt")


# Q17. Create a file containing student records (RollNo,Name,Marks). Display all records, find the student with the highest marks, calculate average marks, display students who scored more than 80.
with open("students.csv", "w") as file:
    file.write("RollNo,Name,Marks\n")
    file.write("101,Amit,85\n")
    file.write("102,Priya,92\n")
    file.write("103,Rahul,78\n")

with open("students.csv", "r") as file:
    lines = file.readlines()[1:]

records = []
for line in lines:
    roll, name, marks = line.strip().split(",")
    records.append((roll, name, int(marks)))

print("All records:")
for r in records:
    print(r)

topper = max(records, key=lambda r: r[2])
print("Student with highest marks:", topper)

average_marks = sum(r[2] for r in records) / len(records)
print("Average marks:", average_marks)

print("Students who scored more than 80:")
for r in records:
    if r[2] > 80:
        print(r)


# Q18. Store employee ID, name, department, and salary in a file. Display all employees, find the highest-paid employee, calculate average salary, display employees earning above a given salary.
with open("employees.csv", "w") as file:
    file.write("ID,Name,Dept,Salary\n")
    file.write("1,Ravi,IT,55000\n")
    file.write("2,Sneha,HR,48000\n")
    file.write("3,Kiran,IT,72000\n")

with open("employees.csv", "r") as file:
    lines = file.readlines()[1:]

employees = []
for line in lines:
    emp_id, name, dept, salary = line.strip().split(",")
    employees.append((emp_id, name, dept, int(salary)))

print("All employees:")
for e in employees:
    print(e)

highest_paid = max(employees, key=lambda e: e[3])
print("Highest paid employee:", highest_paid)

average_salary = sum(e[3] for e in employees) / len(employees)
print("Average salary:", average_salary)

threshold = int(input("Enter salary threshold: "))
print("Employees earning above", threshold, ":")
for e in employees:
    if e[3] > threshold:
        print(e)


# Q19. Store student attendance records in a file. Calculate the attendance percentage and display students having attendance below 75%.
with open("attendance.csv", "w") as file:
    file.write("Name,Present,Total\n")
    file.write("Amit,60,80\n")
    file.write("Priya,50,80\n")
    file.write("Rahul,78,80\n")

with open("attendance.csv", "r") as file:
    lines = file.readlines()[1:]

for line in lines:
    name, present, total = line.strip().split(",")
    percentage = int(present) / int(total) * 100
    if percentage < 75:
        print(name, ":", round(percentage, 2), "% - Below 75%")
    else:
        print(name, ":", round(percentage, 2), "% - OK")


# Q20. Store deposits and withdrawals in a file. Calculate total deposits, total withdrawals, final balance, largest transaction.
with open("transactions.txt", "w") as file:
    file.write("DEPOSIT,5000\n")
    file.write("WITHDRAW,2000\n")
    file.write("DEPOSIT,3000\n")
    file.write("WITHDRAW,1000\n")

total_deposit = 0
total_withdraw = 0
largest_transaction = 0

with open("transactions.txt", "r") as file:
    for line in file:
        transaction_type, amount = line.strip().split(",")
        amount = int(amount)
        if transaction_type == "DEPOSIT":
            total_deposit += amount
        else:
            total_withdraw += amount
        if amount > largest_transaction:
            largest_transaction = amount

print("Total deposits:", total_deposit)
print("Total withdrawals:", total_withdraw)
print("Final balance:", total_deposit - total_withdraw)
print("Largest transaction:", largest_transaction)


# Q21. Maintain book records (book ID, title, author, availability status). Add a book, search for a book, issue a book, return a book, display available books.
with open("books.csv", "w") as file:
    file.write("ID,Title,Author,Available\n")
    file.write("1,Python Basics,J.Doe,Yes\n")
    file.write("2,Data Structures,A.Smith,Yes\n")


def load_books():
    with open("books.csv", "r") as file:
        lines = file.readlines()[1:]
    return [line.strip().split(",") for line in lines]


def save_books(records):
    with open("books.csv", "w") as file:
        file.write("ID,Title,Author,Available\n")
        for r in records:
            file.write(",".join(r) + "\n")


def add_book(book_id, title, author):
    records = load_books()
    records.append([book_id, title, author, "Yes"])
    save_books(records)
    print("Book added successfully")


def search_book(book_id):
    for r in load_books():
        if r[0] == book_id:
            print("Book found:", r)
            return r
    print("Book not found")
    return None


def issue_book(book_id):
    records = load_books()
    for r in records:
        if r[0] == book_id:
            r[3] = "No"
    save_books(records)
    print("Book issued successfully")


def return_book(book_id):
    records = load_books()
    for r in records:
        if r[0] == book_id:
            r[3] = "Yes"
    save_books(records)
    print("Book returned successfully")


def display_available():
    print("Available books:")
    for r in load_books():
        if r[3] == "Yes":
            print(r)


search_book("1")
issue_book("1")
display_available()
return_book("1")
display_available()


# Q22. Read the contents of two text files and create a third file containing the contents of both files.
with open("file1.txt", "w") as file:
    file.write("Content of file 1.\n")

with open("file2.txt", "w") as file:
    file.write("Content of file 2.\n")

with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2, open("file3.txt", "w") as file3:
    file3.write(file1.read())
    file3.write(file2.read())

print("Files combined successfully into file3.txt")


# Q23. Compare two text files and display whether their contents are identical. If different, identify the first line where they differ.
with open("cmp1.txt", "w") as file:
    file.write("line1\nline2\nline3\n")

with open("cmp2.txt", "w") as file:
    file.write("line1\nlineX\nline3\n")

with open("cmp1.txt", "r") as file1, open("cmp2.txt", "r") as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

if lines1 == lines2:
    print("Files are identical")
else:
    for i in range(min(len(lines1), len(lines2))):
        if lines1[i] != lines2[i]:
            print("Files differ at line", i + 1)
            break


# Module Q1. Create a module calculator.py with add, subtract, multiply, divide. Import it in another program and perform calculations based on user input.
# calculator.py
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"


# main.py
# import calculator
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add/subtract/multiply/divide): ")

operations = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}
result = operations[operation](a, b)

print("Result:", result)


# Module Q2. Create a module student.py with functions to calculate total marks, percentage, grade. Import it and generate a student's result.
# student.py
def total_marks(marks_list):
    return sum(marks_list)


def percentage(marks_list, max_per_subject=100):
    return total_marks(marks_list) / (len(marks_list) * max_per_subject) * 100


def grade(pct):
    if pct >= 90:
        return "A+"
    elif pct >= 75:
        return "A"
    elif pct >= 60:
        return "B"
    elif pct >= 40:
        return "C"
    else:
        return "Fail"


# main.py
marks = [85, 78, 92, 66, 74]
pct = percentage(marks)

print("Total marks:", total_marks(marks))
print("Percentage:", pct)
print("Grade:", grade(pct))


# Module Q3. Create a module number_utils.py with functions to check prime, palindrome, Armstrong, perfect number. Import required functions into a main program.
# number_utils.py
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)


def is_perfect(n):
    return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n


# main.py
number = int(input("Enter a number: "))

print(number, "is prime:", is_prime(number))
print(number, "is palindrome:", is_palindrome(number))
print(number, "is Armstrong:", is_armstrong(number))
print(number, "is perfect:", is_perfect(number))


# Module Q4. Create a module string_utils.py with functions to count vowels, reverse a string, check palindrome, count words, remove spaces.
# string_utils.py
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")


def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_words(s):
    return len(s.split())


def remove_spaces(s):
    return s.replace(" ", "")


# main.py
text = input("Enter a string: ")

print("Vowel count:", count_vowels(text))
print("Reversed string:", reverse_string(text))
print("Is palindrome:", is_palindrome(text))
print("Word count:", count_words(text))
print("Without spaces:", remove_spaces(text))


# Module Q5. Create a module with functions to calculate gross salary, deductions, and net salary for an employee.
# payroll.py
def gross_salary(basic, hra, da):
    return basic + hra + da


def deductions(gross, pf_rate=0.12, tax_rate=0.10):
    return gross * pf_rate + gross * tax_rate


def net_salary(basic, hra, da):
    gross = gross_salary(basic, hra, da)
    return gross - deductions(gross)


# main.py
basic = float(input("Enter basic salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))

print("Gross salary:", gross_salary(basic, hra, da))
print("Deductions:", deductions(gross_salary(basic, hra, da)))
print("Net salary:", net_salary(basic, hra, da))


# Module Q6. Create a module with recursive functions for factorial, Fibonacci series, sum of digits, binary conversion. Import and use these functions from another program.
# recursive_utils.py
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


def fibonacci_series(n):
    def fib(k):
        return k if k <= 1 else fib(k - 1) + fib(k - 2)
    return [fib(i) for i in range(n)]


def sum_of_digits(n):
    n = abs(n)
    return n % 10 if n < 10 else n % 10 + sum_of_digits(n // 10)


def to_binary(n):
    if n == 0:
        return "0"
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)


# main.py
num = int(input("Enter a number: "))
terms = int(input("Enter number of Fibonacci terms: "))

print("Factorial:", factorial(num))
print("Fibonacci series:", fibonacci_series(terms))
print("Sum of digits:", sum_of_digits(num))
print("Binary form:", to_binary(num))


# Package Q7. Create a package mathutils with basic.py (arithmetic), number.py (prime/Armstrong/palindrome), statistics.py (mean/max/min). Main program imports functions from each module.
# mathutils/__init__.py
# (empty file, makes mathutils a package)

# mathutils/basic.py
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b if b != 0 else "Error: Division by zero"


# mathutils/number.py
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)


def is_palindrome(n):
    return str(n) == str(n)[::-1]


# mathutils/statistics.py
def mean(values):
    return sum(values) / len(values)


def maximum(values):
    return max(values)


def minimum(values):
    return min(values)


# main.py
# from mathutils import basic, number, statistics
values = [10, 20, 30, 40]

print("5 + 3 =", basic.add(5, 3))
print("Is 29 prime:", number.is_prime(29))
print("Mean:", statistics.mean(values))
print("Maximum:", statistics.maximum(values))
print("Minimum:", statistics.minimum(values))


# Package Q8. Create a package student with marks.py (total/percentage), grade.py (grade), attendance.py (eligibility). Main program generates a student report.
# student/__init__.py
# (empty file, makes student a package)

# student/marks.py
def total(marks_list):
    return sum(marks_list)


def percentage(marks_list, max_per_subject=100):
    return total(marks_list) / (len(marks_list) * max_per_subject) * 100


# student/grade.py
def calculate_grade(pct):
    if pct >= 90:
        return "A+"
    elif pct >= 75:
        return "A"
    elif pct >= 60:
        return "B"
    elif pct >= 40:
        return "C"
    else:
        return "Fail"


# student/attendance.py
def is_eligible(present, total, threshold=75):
    pct = present / total * 100
    return pct >= threshold, pct


# main.py
# from student import marks, grade, attendance
student_marks = [80, 70, 90, 65]
pct = marks.percentage(student_marks)
eligible, att_pct = attendance.is_eligible(68, 80)

print("Total marks:", marks.total(student_marks))
print("Percentage:", pct)
print("Grade:", grade.calculate_grade(pct))
print("Attendance percentage:", att_pct)
print("Eligible:", eligible)


# Package Q9. Develop a package banking with account.py (account/balance), transaction.py (deposit/withdraw), loan.py (loan calculation). Main program uses the package.
# banking/__init__.py
# (empty file, makes banking a package)

# banking/account.py
accounts = {}


def create_account(acc_id, name, initial_balance=0):
    accounts[acc_id] = {"name": name, "balance": initial_balance}
    print("Account created successfully")


def get_balance(acc_id):
    return accounts.get(acc_id, {}).get("balance", 0)


# banking/transaction.py
# from . import account
def deposit(acc_id, amount):
    accounts[acc_id]["balance"] += amount
    return accounts[acc_id]["balance"]


def withdraw(acc_id, amount):
    if accounts[acc_id]["balance"] >= amount:
        accounts[acc_id]["balance"] -= amount
        return accounts[acc_id]["balance"]
    return "Error: Insufficient balance"


# banking/loan.py
def calculate_emi(principal, annual_rate, years):
    r = annual_rate / (12 * 100)
    n = years * 12
    return round(principal * r * (1 + r) ** n / ((1 + r) ** n - 1), 2)


# main.py
# from banking import account, transaction, loan
account.create_account("A1", "Ravi", 1000)

print("Balance after deposit:", transaction.deposit("A1", 500))
print("Balance after withdrawal:", transaction.withdraw("A1", 300))
print("Monthly EMI:", loan.calculate_emi(100000, 10, 2))


# Package Q10. Create a package texttools with cleaning.py (remove punctuation/spaces), tokenization.py (tokenize), frequency.py (word-frequency). Main program uses the package.
# texttools/__init__.py
# (empty file, makes texttools a package)

# texttools/cleaning.py
import string


def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


def remove_extra_spaces(text):
    return " ".join(text.split())


# texttools/tokenization.py
def tokenize(text):
    return text.split()


# texttools/frequency.py
def word_frequency(tokens):
    freq = {}
    for t in tokens:
        freq[t.lower()] = freq.get(t.lower(), 0) + 1
    return freq


# main.py
# from texttools import cleaning, tokenization, frequency
raw_text = input("Enter text to process: ")
cleaned_text = cleaning.remove_extra_spaces(cleaning.remove_punctuation(raw_text))
tokens = tokenization.tokenize(cleaned_text)

print("Cleaned text:", cleaned_text)
print("Tokens:", tokens)
print("Word frequency:", frequency.word_frequency(tokens))


# Directory Q11. Create structure college_project/main.py, student/(__init__.py, details.py, marks.py), faculty/(__init__.py, details.py). Import from both packages and display student and faculty info.
# student/details.py
def get_student_info():
    return {"name": "Amit", "roll_no": 101, "branch": "CSE"}


# student/marks.py
def get_marks():
    return {"Maths": 85, "Physics": 78}


# faculty/details.py
def get_faculty_info():
    return {"name": "Dr. Sharma", "department": "CSE", "designation": "Professor"}


# main.py
# from student import details as student_details
# from student import marks as student_marks
# from faculty import details as faculty_details
print("Student Info:", student_details.get_student_info())
print("Student Marks:", student_marks.get_marks())
print("Faculty Info:", faculty_details.get_faculty_info())


# Directory Q12. Create a library application with packages Books, Members, Transactions. Main program combines all functionality.
# books/catalog.py
books = {}


def add_book(book_id, title, author):
    books[book_id] = {"title": title, "author": author, "available": True}
    print("Book added successfully")


# members/registry.py
members = {}


def add_member(member_id, name):
    members[member_id] = {"name": name, "borrowed": []}
    print("Member added successfully")


# transactions/issue_return.py
# from books import catalog
# from members import registry
def issue_book(book_id, member_id):
    if books[book_id]["available"]:
        books[book_id]["available"] = False
        members[member_id]["borrowed"].append(book_id)
        print("Book issued successfully")
    else:
        print("Book not available")


def return_book(book_id, member_id):
    books[book_id]["available"] = True
    members[member_id]["borrowed"].remove(book_id)
    print("Book returned successfully")


# main.py
# from books import catalog
# from members import registry
# from transactions import issue_return
add_book("B1", "Python Basics", "J.Doe")
add_member("M1", "Ravi")
issue_book("B1", "M1")
print(books)
print(members)
return_book("B1", "M1")
print(books)
print(members)


# Directory Q13. Create ecommerce directory with packages Products, Customers, Orders, Payments, each with at least two modules.
# products/catalog.py
products = {}


def add_product(pid, name, price):
    products[pid] = {"name": name, "price": price}


# products/inventory.py
stock = {}


def add_stock(pid, qty):
    stock[pid] = stock.get(pid, 0) + qty


# customers/profile.py
customers = {}


def add_customer(cid, name, email):
    customers[cid] = {"name": name, "email": email}


# customers/address.py
addresses = {}


def add_address(cid, address):
    addresses[cid] = address


# orders/order.py
orders = {}


def place_order(order_id, cid, items):
    orders[order_id] = {"customer": cid, "items": items, "status": "Placed"}


# orders/tracking.py
def update_status(order_id, status):
    orders[order_id]["status"] = status


# payments/payment.py
payments = {}


def make_payment(order_id, amount, method):
    payments[order_id] = {"amount": amount, "method": method, "status": "Paid"}


# payments/refund.py
def issue_refund(order_id):
    if order_id in payments:
        payments[order_id]["status"] = "Refunded"


# main.py
# from products import catalog, inventory
# from customers import profile, address
# from orders import order, tracking
# from payments import payment, refund
add_product("P1", "Laptop", 55000)
add_stock("P1", 10)
add_customer("C1", "Ravi", "ravi@example.com")
add_address("C1", "123 Main St")
place_order("O1", "C1", ["P1"])
make_payment("O1", 55000, "Card")
update_status("O1", "Shipped")

print("Orders:", orders)
print("Payments:", payments)

issue_refund("O1")
print("After refund:", payments)


# Directory Q14. Create a project with packages Patient management, Doctor management, Billing, Medical records. Access functions from main.py.
# patient_management/patient.py
patients = {}


def register_patient(pid, name, age):
    patients[pid] = {"name": name, "age": age}
    print("Patient registered successfully")


# doctor_management/doctor.py
doctors = {}


def add_doctor(did, name, specialization):
    doctors[did] = {"name": name, "specialization": specialization}
    print("Doctor added successfully")


# billing/bill.py
def generate_bill(consultation_fee, medicine_cost, other_charges=0):
    return consultation_fee + medicine_cost + other_charges


# medical_records/records.py
records = {}


def add_record(pid, diagnosis, prescription):
    records[pid] = {"diagnosis": diagnosis, "prescription": prescription}
    print("Medical record added successfully")


# main.py
# from patient_management import patient
# from doctor_management import doctor
# from billing import bill
# from medical_records import records
register_patient("P1", "Amit", 30)
add_doctor("D1", "Dr. Sharma", "Cardiology")
add_record("P1", "Mild fever", "Paracetamol")
total_bill = generate_bill(consultation_fee=500, medicine_cost=200)

print("Patients:", patients)
print("Doctors:", doctors)
print("Medical Records:", records)
print("Total bill:", total_bill)
