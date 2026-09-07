class Student:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Constructor called")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

    # Destructor
    def __del__(self):
        print("Destructor called")

s1 = Student("Om", 21)
s1.display()
del s1