import pandas as pd


# Q1: Create a dictionary containing the following info for 5 students:
# Student ID, Student Name, Python Marks, DBMS Marks, Mathematics Marks.
students = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Student_Name": ["Amit", "Neha", "Ravi", "Priya", "Karan"],
    "Python": [80, 70, 90, 65, 85],
    "DBMS": [75, 80, 88, 70, 90],
    "Mathematics": [85, 72, 92, 68, 82]
}
df = pd.DataFrame(students)
print(df)
df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df["Total"] / 3
print(df)
print(df[df["Average"] > 75])


# Q2: Create a dictionary containing Employee ID, Employee Name, Department,
# Salary, and Experience. Convert it into a DataFrame. 
employees = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Employee_Name": ["Amit", "Neha", "Ravi", "Priya", "Karan"],
    "Department": ["CSE", "HR", "IT", "CSE", "Finance"],
    "Salary": [45000, 60000, 75000, 52000, 48000],
    "Experience": [2, 5, 7, 4, 3]
}
df = pd.DataFrame(employees)
print(df)
print(df[df["Salary"] > 50000])
print("Average salary:", df["Salary"].mean())
print("Highest salary:", df["Salary"].max())
print(df[df["Experience"] == df["Experience"].max()])


# Q3: Create a dictionary containing Product ID, Product Name, Category, Price,
# and Quantity. Convert it into a DataFrame, calculate Total Amount = Price x Quantity,
# and find the product having the highest total sales.
products = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
    "Price": [50000, 500, 1200, 12000, 2000],
    "Quantity": [2, 10, 5, 3, 4]
}
df = pd.DataFrame(products)
df["Total_Amount"] = df["Price"] * df["Quantity"]
print(df)
print(df[df["Total_Amount"] == df["Total_Amount"].max()])


# Q4: Create a dictionary containing Patient ID, Patient Name, Age, Disease,
# and Medical Charges. Convert it into a DataFrame and display patients above 60 years,
# average medical charge, maximum medical charge, and patients whose charges exceed Rs. 50,000.
patients = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Asha", "Rahul", "Meena", "Sagar", "Pooja"],
    "Age": [65, 45, 72, 30, 61],
    "Disease": ["Diabetes", "Fever", "Heart", "Cold", "Diabetes"],
    "Medical_Charges": [60000, 12000, 85000, 5000, 52000]
}
df = pd.DataFrame(patients)
print(df[df["Age"] > 60])
print("Average medical charge:", df["Medical_Charges"].mean())
print("Maximum medical charge:", df["Medical_Charges"].max())
print(df[df["Medical_Charges"] > 50000])


# Q5: Create a dictionary containing Order_ID, Customer, Product, Quantity,

orders = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Amit", "Neha", "Ravi", "Priya", "Karan"],
    "Product": ["Laptop", "Phone", "Mouse", "Monitor", "Tablet"],
    "Quantity": [1, 2, 5, 1, 2],
    "Price": [55000, 20000, 500, 12000, 15000],
    "Discount": [2000, 1000, 100, 500, 800]
}
df = pd.DataFrame(orders)
df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]
print(df)
print(df[df["Final_Amount"] > 5000])
print(df[df["Final_Amount"] == df["Final_Amount"].max()])
print("Average order value:", df["Final_Amount"].mean())


# Q6: Create a dictionary containing Student_ID, Name, Department, Total_Classes,

attendance = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Neha", "Ravi", "Priya", "Karan"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "IT"],
    "Total_Classes": [100, 100, 90, 100, 80],
    "Classes_Attended": [80, 65, 70, 95, 50]
}
df = pd.DataFrame(attendance)
df["Attendance_Percentage"] = df["Classes_Attended"] / df["Total_Classes"] * 100
print(df)
print(df[df["Attendance_Percentage"] < 75])


# Question 7: A retail shop has Product_ID, Product_Name, Category, Price, and Quantity.

retail = {
    "Product_ID": [1, 2, 3, 4, 5],
    "Product_Name": ["Laptop", "Mouse", "Phone", "Monitor", "Keyboard"],
    "Category": ["Electronics", "Accessories", "Electronics", "Electronics", "Accessories"],
    "Price": [50000, 500, 18000, 12000, 1500],
    "Quantity": [2, 20, 3, 2, 10]
}
df = pd.DataFrame(retail)
df["Total_Sales"] = df["Price"] * df["Quantity"]
print(df)
print(df[df["Total_Sales"] > 10000])
print(df[df["Total_Sales"] == df["Total_Sales"].max()])
print("Average sales:", df["Total_Sales"].mean())


# Q8: Create a Pandas Series from a dictionary of student names and marks.
student_marks = {"Amit": 80, "Neha": 92, "Ravi": 68, "Priya": 75, "Karan": 88}
marks = pd.Series(student_marks)
print(marks)
print("Neha's marks:", marks["Neha"])
print("Maximum marks:", marks.max())
print("Minimum marks:", marks.min())
print("Average marks:", marks.mean())
print(marks[marks > 75])


# Q.9: Create a Pandas Series from a dictionary of employee names and salaries.
salary_data = {"Amit": 45000, "Neha": 60000, "Ravi": 75000, "Priya": 52000, "Karan": 48000}
salary = pd.Series(salary_data)
print(salary)
print("Highest salary:", salary.max())
print("Lowest salary:", salary.min())
print("Average salary:", salary.mean())
print(salary[salary > 50000])


# Q.10: Create a Pandas Series from a dictionary of product names and prices.

product_prices = {"Laptop": 50000, "Mouse": 500, "Keyboard": 1200, "Monitor": 12000}
prices = pd.Series(product_prices)
print(prices)
prices = prices * 1.10
print("Prices after 10% increase:")
print(prices)
print("Most expensive product:")
print(prices[prices == prices.max()])
print("Products costing above 1000:")
print(prices[prices > 1000])


# Q.11: Create a Pandas Series where patient IDs are the index and ages are values.
patient_ages = {101: 65, 102: 45, 103: 72, 104: 30, 105: 61}
ages = pd.Series(patient_ages)
print("Average age:", ages.mean())
print("Oldest patient:")
print(ages[ages == ages.max()])
print("Youngest patient:")
print(ages[ages == ages.min()])
print("Patients above 60:")
print(ages[ages > 60])


# Q.12: Create a Pandas Series from a dictionary of student names and attendance percentages.
student_attendance = {"Amit": 80, "Neha": 95, "Ravi": 68, "Priya": 72, "Karan": 92}
att = pd.Series(student_attendance)
print("Average attendance:", att.mean())
print("Attendance below 75%:")
print(att[att < 75])
print("Attendance above 90%:")
print(att[att > 90])
print("Highest attendance:")
print(att[att == att.max()])


# Q.13: Dataset students.
df = pd.read_csv("students.csv")
print(df.head())
print(df.tail())
df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3
print(df)
print(df[df["Average"] > 75])
print(df[df["Average"] == df["Average"].max()])
print(df[["Python", "DBMS", "Maths"]].mean())


# Q14: Dataset employees.
df = pd.read_csv("employees.csv")
print(df[df["Department"] == "CSE"])
print("Average salary:", df["Salary"].mean())
print("Highest salary:", df["Salary"].max())
print("Lowest salary:", df["Salary"].min())
print(df[df["Salary"] > 50000])
print(df.groupby("Department")["Salary"].mean())


# Q15: Dataset patients.
df = pd.read_csv("patients.csv")
print(df[df["Age"] > 60])
print("Average medical expense:", df["Medical_Expense"].mean())
print(df[df["Medical_Expense"] == df["Medical_Expense"].max()])
print(df["Disease"].value_counts())
print(df[df["Medical_Expense"] > 50000])


# Q16: Dataset weather.
df = pd.read_csv("weather.csv")
print("Maximum temperature:", df["Temperature"].max())
print("Minimum temperature:", df["Temperature"].min())
print("Average temperature:", df["Temperature"].mean())
print(df[df["Temperature"] > 35])
print(df.groupby("City")["Temperature"].mean())
