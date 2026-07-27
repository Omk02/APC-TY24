
# -----> For loop  ------------->

# Q.1 print natural numbers up to n ?
def Q1_natural_numbers():

  n = int(input("Enter n:"))
  for i in range(1, n+1):
    print(i)

# Q.2 print even number up to n ?
def Q2_even_numbers():

  n = int(input("enter n: "))
  for i in range(2, n+1,2):
   print(i)

# Q.3 print odd number up to n ?
def Q3_odd_numbers():

 n = int(input("enter n: "))
 for i in range(1, n+1,2):
  print(i)

# Q.4 print the series 1 2 4 8 16... up to n terms ?
def Q4_series():

 n = int(input("enter n: "))
 x=1
 for i in range(n):
    print(x,end=" ")
    x=x*2

# Q.5 print sum the given sequence 1 + 1/1! + 1/2! + 1/3! +.....+1/n! ?
def Q5_Sequence():

 n = int(input("Enter n:"))
 fact = 1
 sun = 1
 for i in range(1, n+1):
    fact  = fact*i
    sum = sum + (1/fact)
    print("sum = ",sum)

# Q.6 Produce design A B C
                #    A B C
                #    A B C
def Q6_Design1():

 for i in range(3):
    for j in range(65,68):
        print(chr(j),end="")
        print()

# Q.7 Produce design A  
                #    A B 
                #    A B C
def Q7_design2():

 n=5
 for i in range(1,n+1):
  for j in range(65,65+i):
   print(chr(j),end="")
   print()

# Q.8 Produce design A B C
                #    A B 
                #    A 
def Q8_Design3():

 n=5
 for i in range(n,0,-1):
  for j in range(65,65+i):
   print(chr(j),end="")
   print()

# Q.9 Compute the cosine series
def Q9_cosine_series():

 cos(x) = 1 − x²/2! + x⁴/4! − x⁶/6! + ...?
 x = float(input("Enter x: "))
 n = int(input("Enter number of terms: "))
 sum = 1
for i in range(1, n):
    fact = 1
    power = 2 * i
    for j in range(1, power + 1):
        fact = fact * j
    term = (x ** power) / facts
    if i % 2 == 1:
        sum = sum - term
    else:
        sum = sum + term
    print("cos(x) =", sum)

# Q.10 Check whether the square root of a number is prime
def Q1_square_root():
 import math
 n = int(input("Enter number: "))
 root = int(math.sqrt(n))
 count = 0
for i in range(1, root + 1):
    if root % i == 0:
        count += 1
    if count == 2:
      print("Square root is prime")
    else:
      print("Square root is not prime")

      