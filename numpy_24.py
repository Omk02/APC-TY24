import numpy as np


# Q1: 1D array of 10 integers - array, size, dtype, ndim
a = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
print(a)
print("Size:", a.size)
print("Data type:", a.dtype)
print("Dimensions:", a.ndim)

# Q2: Two arrays of 5 integers - arithmetic operations
x = np.array([10, 20, 30, 40, 50])
y = np.array([1, 2, 3, 4, 5])
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)

# Q3: Max, min, sum, average of 10 numbers
a = np.array([12, 45, 7, 23, 89, 34, 56, 78, 90, 11])
print("Max:", a.max())
print("Min:", a.min())
print("Sum:", a.sum())
print("Average:", a.mean())

# Q4: Numbers 1-20 - even and odd using Boolean indexing
a = np.arange(1, 21)
print("Even:", a[a % 2 == 0])
print("Odd:", a[a % 2 != 0])

# Q5: 1-12 reshaped into 2x6, 3x4, 4x3
a = np.arange(1, 13)
print("2 x 6:\n", a.reshape(2, 6))
print("3 x 4:\n", a.reshape(3, 4))
print("4 x 3:\n", a.reshape(4, 3))

# Q6: Two 3x3 matrices - addition
m1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(m1 + m2)

# Q7: Matrix multiplication
m1 = np.array([[1, 2, 3], [4, 5, 6]])       # 2x3
m2 = np.array([[7, 8], [9, 10], [11, 12]])  # 3x2
print(np.dot(m1, m2))

# Q8: 3x4 matrix - transpose
m = np.arange(1, 13).reshape(3, 4)
print("Original:\n", m)
print("Transpose:\n", m.T)

# Q9: 4x4 array - first row, last column, diagonal, 2nd & 3rd rows
m = np.arange(1, 17).reshape(4, 4)
print(m)
print("First row:", m[0])
print("Last column:", m[:, -1])
print("Diagonal:", np.diag(m))
print("Second and third rows:\n", m[1:3])

# Q10: 4x4 matrix - row sums and column sums
m = np.arange(1, 17).reshape(4, 4)
print("Row sums:", m.sum(axis=1))
print("Column sums:", m.sum(axis=0))

# Q11: 1-20 slicing
a = np.arange(1, 21)
print("First 5:", a[:5])
print("Last 5:", a[-5:])
print("Alternate:", a[::2])
print("Reverse:", a[::-1])

# Q12: Replace elements > 50 with 0
a = np.array([10, 55, 30, 75, 20, 90, 45, 60, 5, 51])
a[a > 50] = 0
print(a)

# Q13: Sort ascending and descending
a = np.array([42, 7, 19, 88, 3, 56, 27])
print("Ascending:", np.sort(a))
print("Descending:", np.sort(a)[::-1])

# Q14: Unique elements
a = np.array([1, 2, 2, 3, 4, 4, 4, 5, 6, 6])
print(np.unique(a))

# Q15: Horizontal and vertical concatenation
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("Horizontal:\n", np.hstack((a, b)))
print("Vertical:\n", np.vstack((a, b)))

# Q16: Marks of 10 students - statistics
marks = np.array([78, 85, 92, 67, 74, 88, 95, 60, 81, 70])
print("Highest:", marks.max())
print("Lowest:", marks.min())
print("Average:", marks.mean())
print("Median:", np.median(marks))
print("Standard deviation:", marks.std())

# Q17: Marks of 20 students - above class average
marks = np.array([55, 67, 78, 89, 90, 45, 62, 71, 83, 94,
                  58, 66, 74, 81, 92, 49, 63, 77, 85, 96])
avg = marks.mean()
print("Class average:", avg)
print("Above average:", marks[marks > avg])

# Q18: 3D array (2,3,4) with 1-24
a3 = np.arange(1, 25).reshape(2, 3, 4)
print(a3)
print("Dimensions:", a3.ndim)
print("Shape:", a3.shape)
print("Size:", a3.size)

# Q19: 3D array access
a3 = np.arange(1, 25).reshape(2, 3, 4)
print("First element:", a3[0, 0, 0])
print("Last element:", a3[-1, -1, -1])
print("Element [0,1,2]:", a3[0, 1, 2])
print("Element [1,2,3]:", a3[1, 2, 3])

# Q20: 3D array sums
a3 = np.arange(1, 25).reshape(2, 3, 4)
print("Sum of all elements:", a3.sum())
print("Sum of each layer:", a3.sum(axis=(1, 2)))
print("Sum along rows:\n", a3.sum(axis=1))
print("Sum along columns:\n", a3.sum(axis=2))

# Q21: Random 3D array - replace > 50 with 0
r = np.random.randint(1, 101, size=(2, 3, 4))
print("Original:\n", r)
r[r > 50] = 0
print("Modified:\n", r)

# Q22: Random (3,4,5) - statistics
r = np.random.rand(3, 4, 5)
print("Mean:", np.mean(r))
print("Median:", np.median(r))
print("Standard deviation:", np.std(r))
print("Variance:", np.var(r))
print("Minimum:", np.min(r))
print("Maximum:", np.max(r))

# Q23: Flatten 3D array
a3 = np.arange(1, 25).reshape(2, 3, 4)
print("Original:\n", a3)
print("Flattened:", a3.flatten())

# Q24: 3D array 1-27 - flatten and calculate
a3 = np.arange(1, 28).reshape(3, 3, 3)
f = a3.flatten()
print("Flattened:", f)
print("Sum:", f.sum())
print("Average:", f.mean())
print("Maximum:", f.max())
print("Minimum:", f.min())

# Q25: Random (3,4,5) - flatten, filter
r = np.random.randint(1, 101, size=(3, 4, 5))
f = r.flatten()
print("Flattened:", f)
print("Greater than 50:", f[f > 50])
print("Even numbers:", f[f % 2 == 0])
print("Less than average:", f[f < f.mean()])


