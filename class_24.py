# Q1: Student class
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        percentage = sum(self.marks) / len(self.marks)
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Percentage: {percentage:.2f}%")


s1 = Student(1, "Amit", [80, 90, 85])
s2 = Student(2, "Priya", [70, 75, 88])
s1.display()
s2.display()
print()


# Q2: Employee class
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return 0.20 * self.basic_salary

    def calculate_da(self):
        return 0.30 * self.basic_salary

    def gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()


e1 = Employee(101, "Ravi", 30000)
print(f"Gross Salary of {e1.name}: {e1.gross_salary()}")
print()


# Q3: Rectangle class
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r1 = Rectangle(10, 5)
print(f"Rectangle Area: {r1.area()}, Perimeter: {r1.perimeter()}")
print()


# Q4: Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14159 * self.radius


c1 = Circle(7)
print(f"Circle Area: {c1.area():.2f}, Circumference: {c1.circumference():.2f}")
print()


# Q5: Book class
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Price: {self.price}")


b1 = Book(1, "Python Basics", "John Doe", 350)
b2 = Book(2, "Data Structures", "Jane Roe", 500)
b3 = Book(3, "Algorithms", "Alan Kay", 450)
for b in (b1, b2, b3):
    b.display()
print()


# Q6: ElectricityBill class
class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        units = self.units
        if units <= 100:
            bill = units * 5
        elif units <= 200:
            bill = 100 * 5 + (units - 100) * 7
        else:
            bill = 100 * 5 + 100 * 7 + (units - 200) * 10
        return bill


eb1 = ElectricityBill("C001", "Sita", 250)
print(f"Electricity Bill for {eb1.consumer_name}: {eb1.calculate_bill()}")
print()


# Q7: MobilePhone class
class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specs(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Price: {self.price}")

    def price_after_discount(self, discount_percent):
        return self.price - (self.price * discount_percent / 100)


m1 = MobilePhone("Samsung", "Galaxy", 128, 20000)
m1.display_specs()
print(f"Price after 10% discount: {m1.price_after_discount(10)}")
print()


# Q8: Patient class
class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display_info(self):
        print(f"ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Disease: {self.disease}")

    def total_bill(self, extra_charges=0):
        return self.consultation_fee + extra_charges


p1 = Patient(1, "Ramesh", 45, "Fever", 500)
p1.display_info()
print(f"Total Bill: {p1.total_bill(200)}")
print()


# Q9: ATM class
class ATM:
    def __init__(self, account_no, name, balance=0):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print(f"Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New Balance: {self.balance}")

    def display_account(self):
        print(f"Account No: {self.account_no}, Name: {self.name}, Balance: {self.balance}")


atm1 = ATM("AC123", "Suresh", 5000)
while True:
    print("1.Check Balance 2.Deposit 3.Withdraw 4.Display 5.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        atm1.check_balance()
    elif choice == "2":
        atm1.deposit(float(input("Enter amount: ")))
    elif choice == "3":
        atm1.withdraw(float(input("Enter amount: ")))
    elif choice == "4":
        atm1.display_account()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
print()


# Q10: Vehicle class
class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, availability=True):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability

    def rent_vehicle(self, days):
        if self.availability:
            self.availability = False
            return self.rental_rate * days
        else:
            print("Vehicle not available")
            return 0

    def return_vehicle(self):
        self.availability = True
        print(f"Vehicle {self.vehicle_no} returned")


v1 = Vehicle("KA01AB1234", "Swift", 1000)
print(f"Rental Charge: {v1.rent_vehicle(3)}")
v1.return_vehicle()
print()


# Q11: ShoppingCart class
class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = {}

    def add_product(self, product, price):
        self.products[product] = price

    def remove_product(self, product):
        if product in self.products:
            del self.products[product]

    def total_bill(self):
        return sum(self.products.values())

    def __del__(self):
        print(f"Shopping cart {self.cart_id} for {self.customer_name} destroyed")


sc1 = ShoppingCart("Neha", "CART01")
sc1.add_product("Shoes", 1500)
sc1.add_product("Bag", 800)
print(f"Total Bill: {sc1.total_bill()}")
del sc1
print()


# Q12: FoodOrder class
class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self, tax_percent=5):
        subtotal = self.quantity * self.price
        return subtotal + (subtotal * tax_percent / 100)

    def __del__(self):
        print(f"Order {self.order_id} completed. Thank you!")


fo1 = FoodOrder(1, "Kiran", "Pizza", 2, 250)
print(f"Total Bill with tax: {fo1.total_bill()}")
del fo1
print()


# Q13: StudentResult class
class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def grade(self):
        pct = self.percentage()
        if pct >= 90:
            return "A"
        elif pct >= 75:
            return "B"
        elif pct >= 60:
            return "C"
        else:
            return "D"

    def __del__(self):
        print(f"Result processing for {self.name} completed")


sr1 = StudentResult("Anjali", [85, 90, 78, 92, 88])
print(f"Total: {sr1.total()}, Percentage: {sr1.percentage():.2f}%, Grade: {sr1.grade()}")
del sr1
