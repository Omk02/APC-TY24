# Q1: Factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))


# Q2: Check if number is even or odd
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(check_even_odd(7))


# Q3: Greater of two numbers
def greater_number(a, b):
    return a if a > b else b

print(greater_number(10, 20))


# Q4: Simple interest calculation
def simple_interest(p, r, t):
    return (p * r * t) / 100

print(simple_interest(1000, 5, 2))


# Q5: Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(29))


# Q6: Area of a circle
def area_of_circle(radius):
    return 3.14159 * radius * radius

print(area_of_circle(7))


# Q7: Sum of first n natural numbers
def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

print(sum_of_natural_numbers(10))


# Q8: Power (base ^ exponent)
def power(base, exponent):
    return base ** exponent

print(power(2, 10))


# Q9: Largest element in a list (without max())
def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(find_largest([3, 9, 2, 45, 10]))


# Q10: Count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

print(count_vowels("Hello World"))


# Q11: Reverse a string
def reverse_string(s):
    return s[::-1]

print(reverse_string("python"))


# Q12: Check if string/number is a palindrome
def is_palindrome(value):
    s = str(value)
    return s == s[::-1]

print(is_palindrome("madam"))
print(is_palindrome(12321))


# Q13: Average of a list of numbers
def average_of_list(numbers):
    return sum(numbers) / len(numbers)

print(average_of_list([10, 20, 30, 40]))


# Q14: Count occurrences of an element in a list
def count_occurrences(lst, element):
    return lst.count(element)

print(count_occurrences([1, 2, 2, 3, 2, 4], 2))


# Q15: Unique elements from a list
def unique_elements(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(unique_elements([1, 2, 2, 3, 3, 4]))


# Q16: Second largest number in a list
def second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

print(second_largest([10, 20, 4, 45, 99, 99]))


# Q17: First n Fibonacci numbers
def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

print(fibonacci(10))


# Q18: Student percentage and grade from 5 subject marks
def student_result(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"
    return percentage, grade

print(student_result(90, 85, 78, 92, 88))


# Q19: Electricity bill using slabs
def electricity_bill(units):
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    elif units <= 300:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 7
    else:
        bill = 100 * 3 + 100 * 5 + 100 * 7 + (units - 300) * 10
    return bill

print(electricity_bill(250))


# Q20: Gross salary from basic salary (HRA + DA)
def gross_salary(basic):
    hra = 0.20 * basic
    da = 0.15 * basic
    return basic + hra + da

print(gross_salary(30000))


# Q21: Total bill with discount
def total_bill(prices, quantities, discount_percent):
    total = sum(p * q for p, q in zip(prices, quantities))
    discount = total * discount_percent / 100
    return total - discount

print(total_bill([100, 200, 50], [2, 1, 3], 10))


# Q22: Min, max, sum, average of a list
def list_stats(numbers):
    return {
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
    }

print(list_stats([12, 45, 7, 89, 34]))


# Q23: Student records: total, percentage, grade, class average, highest/lowest scorer
def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total, num_subjects=5):
    return total / num_subjects

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"

def process_student_records(students):
    results = []
    for student in students:
        total = calculate_total(student["marks"])
        percentage = calculate_percentage(total)
        grade = calculate_grade(percentage)
        results.append({
            "name": student["name"],
            "roll_no": student["roll_no"],
            "total": total,
            "percentage": percentage,
            "grade": grade,
        })
    class_average = sum(r["percentage"] for r in results) / len(results)
    highest_scorer = max(results, key=lambda r: r["total"])
    lowest_scorer = min(results, key=lambda r: r["total"])
    return results, class_average, highest_scorer, lowest_scorer

students = [
    {"name": "Amit", "roll_no": 1, "marks": [80, 75, 90, 85, 70]},
    {"name": "Neha", "roll_no": 2, "marks": [60, 65, 70, 55, 75]},
    {"name": "Ravi", "roll_no": 3, "marks": [95, 92, 88, 91, 89]},
]
results, class_average, highest_scorer, lowest_scorer = process_student_records(students)
print(results)
print("Class Average:", class_average)
print("Highest Scorer:", highest_scorer["name"])
print("Lowest Scorer:", lowest_scorer["name"])


# Q24: Bank account: deposit, withdraw, balance, transaction history
bank_account = {"balance": 0, "transactions": []}

def deposit(account, amount):
    account["balance"] += amount
    account["transactions"].append(f"Deposited {amount}")
    return account["balance"]

def withdraw(account, amount):
    if amount > account["balance"]:
        account["transactions"].append(f"Failed withdrawal of {amount} - Insufficient balance")
        return "Insufficient balance"
    account["balance"] -= amount
    account["transactions"].append(f"Withdrew {amount}")
    return account["balance"]

def balance_enquiry(account):
    return account["balance"]

def transaction_history(account):
    return account["transactions"]

deposit(bank_account, 5000)
withdraw(bank_account, 2000)
withdraw(bank_account, 10000)
print(balance_enquiry(bank_account))
print(transaction_history(bank_account))


# Q25: Library system: add, issue, return, search, display books
library = {}

def add_book(title, quantity):
    library[title] = library.get(title, 0) + quantity

def issue_book(title):
    if library.get(title, 0) > 0:
        library[title] -= 1
        return f"{title} issued"
    return f"{title} not available"

def return_book(title):
    library[title] = library.get(title, 0) + 1
    return f"{title} returned"

def search_book(title):
    return title in library

def display_available_books():
    return {book: qty for book, qty in library.items() if qty > 0}

add_book("Python Basics", 3)
add_book("Data Structures", 2)
issue_book("Python Basics")
print(display_available_books())
print(search_book("Data Structures"))
return_book("Python Basics")
print(display_available_books())


# Q26: Modular electricity bill with fixed charges, tax, discount
def calculate_units_charge(units):
    if units <= 100:
        return units * 3
    elif units <= 200:
        return 100 * 3 + (units - 100) * 5
    elif units <= 300:
        return 100 * 3 + 100 * 5 + (units - 200) * 7
    else:
        return 100 * 3 + 100 * 5 + 100 * 7 + (units - 300) * 10

def calculate_fixed_charges():
    return 50

def calculate_tax(amount):
    return amount * 0.05

def calculate_discount(amount, units):
    return amount * 0.02 if units < 100 else 0

def generate_electricity_bill(units):
    units_charge = calculate_units_charge(units)
    fixed_charge = calculate_fixed_charges()
    tax = calculate_tax(units_charge)
    discount = calculate_discount(units_charge, units)
    total = units_charge + fixed_charge + tax - discount
    return total

print(generate_electricity_bill(150))


# Q27: Hospital billing: consultation, lab, medicine, room charges
def consultation_charges():
    return 500

def laboratory_charges(tests):
    return tests * 300

def medicine_charges(items):
    return sum(items)

def room_charges(days, rate_per_day):
    return days * rate_per_day

def apply_discount(amount, category):
    discounts = {"senior_citizen": 0.15, "regular": 0.05, "staff": 0.25}
    return amount * discounts.get(category, 0)

def final_bill(tests, medicines, days, rate_per_day, category):
    consultation = consultation_charges()
    lab = laboratory_charges(tests)
    medicine = medicine_charges(medicines)
    room = room_charges(days, rate_per_day)
    subtotal = consultation + lab + medicine + room
    discount = apply_discount(subtotal, category)
    return subtotal - discount

print(final_bill(2, [200, 150, 100], 3, 1000, "senior_citizen"))


# Q28: Shopping cart: add/remove product, subtotal, coupon, GST, invoice
cart = []

def add_product(name, price, quantity):
    cart.append({"name": name, "price": price, "quantity": quantity})

def remove_product(name):
    global cart
    cart = [item for item in cart if item["name"] != name]

def calculate_subtotal():
    return sum(item["price"] * item["quantity"] for item in cart)

def apply_coupon_discount(subtotal, coupon_percent):
    return subtotal * coupon_percent / 100

def calculate_gst(amount, gst_percent=18):
    return amount * gst_percent / 100

def generate_invoice(coupon_percent=0):
    subtotal = calculate_subtotal()
    discount = apply_coupon_discount(subtotal, coupon_percent)
    taxable_amount = subtotal - discount
    gst = calculate_gst(taxable_amount)
    total = taxable_amount + gst
    return {
        "subtotal": subtotal,
        "discount": discount,
        "gst": gst,
        "total": total,
    }

add_product("Shirt", 500, 2)
add_product("Shoes", 1500, 1)
print(generate_invoice(coupon_percent=10))


# Q29: Recursive binary search
def binary_search(lst, target, low=0, high=None):
    if high is None:
        high = len(lst) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        return binary_search(lst, target, mid + 1, high)
    else:
        return binary_search(lst, target, low, mid - 1)

print(binary_search([1, 3, 5, 7, 9, 11], 7))


# Q30: Decimal to binary using recursion
def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)

print(decimal_to_binary(42))


# Q31: Check palindrome using recursion
def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

print(is_palindrome_recursive("madam"))


# Q32: Pass functions as arguments (add, subtract, multiply, divide)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

def calculate(operation, a, b):
    return operation(a, b)

print(calculate(add, 10, 5))
print(calculate(subtract, 10, 5))
print(calculate(multiply, 10, 5))
print(calculate(divide, 10, 5))


# Programs on Lambda Function

# Q33: Lambda: square of a number
square = lambda x: x ** 2
print(square(6))


# Q34: Lambda: cube of a number
cube = lambda x: x ** 3
print(cube(3))


# Q35: Lambda: check even number
is_even = lambda x: x % 2 == 0
print(is_even(8))


# Q36: Lambda: maximum of two numbers
maximum = lambda a, b: a if a > b else b
print(maximum(15, 20))


# Q37: Lambda: simple interest
simple_interest_lambda = lambda p, r, t: (p * r * t) / 100
print(simple_interest_lambda(1000, 5, 2))


# Q38: map() + lambda: squares of a list
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)


# Q39: map() + lambda: cubes of a list
cubes = list(map(lambda x: x ** 3, numbers))
print(cubes)


# Q40: map() + lambda: sum of two lists element-wise
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
sum_list = list(map(lambda a, b: a + b, list1, list2))
print(sum_list)


# Q41: filter() + lambda: even numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, nums))
print(even_numbers)


# Q42: filter() + lambda: prime numbers
def is_prime_check(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = list(filter(lambda x: is_prime_check(x), nums))
print(prime_numbers)


# Q43: filter() + lambda: positive numbers
mixed_numbers = [-5, 3, -2, 8, -1, 9]
positive_numbers = list(filter(lambda x: x > 0, mixed_numbers))
print(positive_numbers)


# Q44: filter() + lambda: numbers greater than 50
values = [10, 55, 30, 70, 45, 90]
greater_than_50 = list(filter(lambda x: x > 50, values))
print(greater_than_50)


# Q45: filter() + lambda: words longer than 5 characters
words = ["cat", "elephant", "dog", "giraffe", "ant", "monkey"]
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)


# Q46: Sort words by length using lambda
words_to_sort = ["banana", "kiwi", "apple", "fig", "watermelon"]
sorted_by_length = sorted(words_to_sort, key=lambda w: len(w))
print(sorted_by_length)


# Q47: Sort students by marks using lambda
students_marks = [("Amit", 85), ("Neha", 92), ("Ravi", 78)]
sorted_students = sorted(students_marks, key=lambda x: x[1])
print(sorted_students)


# Q48: Sort employees by salary using lambda
employees = [("Amit", 45000), ("Neha", 60000), ("Ravi", 35000)]
sorted_employees = sorted(employees, key=lambda x: x[1])
print(sorted_employees)


# Q49: Student marks: average, filter above 75, sort by marks
student_records = [("Amit", 85), ("Neha", 92), ("Ravi", 65), ("Priya", 78)]

# a) Calculate average marks
average_marks = sum(map(lambda x: x[1], student_records)) / len(student_records)
print(average_marks)

# b) Filter students scoring above 75
above_75 = list(filter(lambda x: x[1] > 75, student_records))
print(above_75)

# c) Sort students according to marks
sorted_by_marks = sorted(student_records, key=lambda x: x[1])
print(sorted_by_marks)


# Q50: Employee records: filter >50000, increase salary 10%, sort by salary
employee_records = [
    ("Amit", "IT", 55000),
    ("Neha", "HR", 45000),
    ("Ravi", "Finance", 65000),
    ("Priya", "IT", 40000),
]

# a) Find employees earning more than ₹50,000
high_earners = list(filter(lambda x: x[2] > 50000, employee_records))
print(high_earners)

# b) Increase salaries by 10%
increased_salaries = list(map(lambda x: (x[0], x[1], x[2] * 1.10), employee_records))
print(increased_salaries)

# c) Sort employees according to salary
sorted_by_salary = sorted(employee_records, key=lambda x: x[2])
print(sorted_by_salary)


# Q51: Products: total value, filter >1000, sort by total value
products = [
    ("Laptop", 55000, 1),
    ("Mouse", 500, 3),
    ("Keyboard", 1200, 2),
    ("Monitor", 8000, 1),
]

# a) Calculate total value of each product
total_values = list(map(lambda x: (x[0], x[1] * x[2]), products))
print(total_values)

# b) Filter products costing more than ₹1,000
costly_products = list(filter(lambda x: x[1] > 1000, products))
print(costly_products)

# c) Sort products according to total value
sorted_products = sorted(total_values, key=lambda x: x[1])
print(sorted_products)


# Q52: Words: length, filter >5 chars, sort by length
word_list = ["python", "is", "a", "powerful", "programming", "language"]

# a) Find the length of every word
word_lengths = list(map(lambda w: len(w), word_list))
print(word_lengths)

# b) Extract words having more than five characters
words_above_5 = list(filter(lambda w: len(w) > 5, word_list))
print(words_above_5)

# c) Sort words according to their length
sorted_words = sorted(word_list, key=lambda w: len(w))
print(sorted_words)
