# ***************WHILE LOOP PRACTICE PROGRAMS*******************

# Q1. Print natural numbers up to n

def Q1_natural_numbers():
    n = int(input("Enter n: "))
    i = 1
    while i <= n:
        print(i)
        i += 1

 
# Q2. Print even numbers up to n

def q2_even_numbers():
    n = int(input("Enter n: "))
    i = 2
    while i <= n:
        print(i)
        i += 2

# Q3. Print odd numbers up to 
def q3_odd_numbers():
    n = int(input("Enter n: "))
    i = 1
    while i <= n:
        print(i)
        i += 2

# Q4. Print sum of natural numbers up to 
def q4_sum_natural_numbers():
    n = int(input("Enter n: "))
    i = 1
    total = 0
    while i <= n:
        total += i
        i += 1
    print("Sum =", total)

# Q5. Print sum of odd numbers up to 
def q5_sum_odd_numbers():
    n = int(input("Enter n: "))
    i = 1
    total = 0
    while i <= n:
        total += i
        i += 2
    print("Sum =", total)

# Q6. Print sum of even numbers up to 
def q6_sum_even_numbers():
    n = int(input("Enter n: "))
    i = 2
    total = 0
    while i <= n:
        total += i
        i += 2
    print("Sum =", total)

# Q7. Print natural numbers in reverse orde
def q7_reverse_natural_numbers():
    n = int(input("Enter n: "))
    while n >= 1:
        print(n)
        n -= 1

# Q8. Fibonacci series up to n term
def q8_fibonacci_series():
    n = int(input("Enter number of terms: "))
    a = 0
    b = 1
    count = 1
    while count <= n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        count += 1
    print()

# Q9. Find factorial of a numbe
def q9_factorial():
    n = int(input("Enter number: "))
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    print("Factorial =", fact)


# Q10. Check whether a number is prime
def q10_check_prime():
    n = int(input("Enter number: "))
    i = 2
    count = 0
    while i < n:
        if n % i == 0:
            count += 1
        i += 1
    if count == 0 and n > 1:
        print("Prime")
    else:
        print("Not Prime")


# Q11. Find sum of digits
def q11_sum_of_digits():
    n = int(input("Enter number: "))
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    print("Sum =", total)


# Q12. Check palindrome number
def q12_check_palindrome():
    n = int(input("Enter number: "))
    temp = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    if temp == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")


# Q13. Reverse a number
def q13_reverse_number():
    n = int(input("Enter number: "))
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    print("Reverse =", rev)


# Q14. Multiplication table
def q14_multiplication_table():
    n = int(input("Enter number: "))
    i = 1
    while i <= 10:
        print(n, "x", i, "=", n * i)
        i += 1


# Q15. Largest of n numbers
def q15_largest_of_n_numbers():
    n = int(input("How many numbers? "))
    i = 1
    largest = None
    while i <= n:
        num = int(input("Enter number: "))
        if largest is None or num > largest:
            largest = num
        i += 1
    print("Largest =", largest)


# Q16. Smallest of n numbers
def q16_smallest_of_n_numbers():
    n = int(input("How many numbers? "))
    i = 1
    smallest = None
    while i <= n:
        num = int(input("Enter number: "))
        if smallest is None or num < smallest:
            smallest = num
        i += 1
    print("Smallest =", smallest)
