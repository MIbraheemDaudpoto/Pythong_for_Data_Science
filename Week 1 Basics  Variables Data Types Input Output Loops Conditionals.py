"""
===========================================================
                PYTHON BASICS - PART 01
===========================================================

Topics Covered:
1. Type Conversion
2. Input & Output
3. Operators
4. Conditional Statements
5. Loops
6. Practice Questions

Author : Muhammad Ibraheem
===========================================================
"""

# =========================================================
# 1. TYPE CONVERSION
# =========================================================

# ---------- Integer Conversion ----------

# n = "2"
# n = int(n)
# print(type(n))
# print(n)

# ---------- Float & Boolean Conversion ----------

# n = 2.3
# n = bool(n)
# print(n)
# print(type(n))


# =========================================================
# 2. INPUT & OUTPUT
# =========================================================

# name = input("Enter Your Name: ")
# age = input("Enter Your Age: ")

# age = int(age)

# print(f"Your Name is {name} and Your Age is {age}")

# print(type(name))
# print(type(age))


# =========================================================
# 3. OPERATORS
# =========================================================

# a = 2
# b = 4

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Modulus:", a % b)
# print("Floor Division:", a // b)
# print("Exponent:", a ** b)


# =========================================================
# 4. CONDITIONAL STATEMENTS
# =========================================================

# money = int(input("Give me Money: "))

# if 10 <= money <= 20:
#     print("Give him a Cheegum")

# elif 20 <= money <= 30:
#     print("Give him a Cake")

# elif money > 30:
#     print("Give him what he wants")

# else:
#     print("Go Back and Pick up some Rupees")


# =========================================================
# CONDITIONAL STATEMENTS - PRACTICE QUESTIONS
# =========================================================

# ---------------------------------------------------------
# Q1. Find the Greatest Number
# ---------------------------------------------------------

# a = int(input("Enter First Number: "))
# b = int(input("Enter Second Number: "))

# if a > b:
#     print("A is Greater than B")
# else:
#     print("B is Greater than A")


# ---------------------------------------------------------
# Q2. Welcome User According to Gender
# ---------------------------------------------------------

# gender = input("Enter Gender (M/F): ")

# if gender == "M" or gender == "m":
#     print("Good Morning Sir")

# elif gender == "F" or gender == "f":
#     print("Good Morning Ma'am")

# else:
#     print("Please Enter a Valid Input")


# ---------------------------------------------------------
# Q3. Check Even or Odd
# ---------------------------------------------------------

# num = int(input("Enter a Number: "))

# if num % 2 == 0:
#     print(f"{num} is an EVEN Number")
# else:
#     print(f"{num} is an ODD Number")


# =========================================================
# 5. LOOPS
# =========================================================

# ---------- range() ----------

# for i in range(10, 50, 5):
#     print(i)


# ---------- Loop Through String ----------

# text = "Printing"

# for i in range(len(text)):
#     print(text[i])


# ---------- break & else ----------

# for i in range(1, 31):

#     if i == 4:
#         print("Break Executed")
#         break

#     print(i)

# else:
#     print("Break Not Executed")


# =========================================================
# LOOP PRACTICE QUESTIONS
# =========================================================

# ---------------------------------------------------------
# Q1. Print "Hello World" N Times
# ---------------------------------------------------------

# n = int(input("Enter an Integer: "))

# for i in range(1, n + 1):
#     print("Hello World")


# ---------------------------------------------------------
# Q2. Print Natural Numbers
# ---------------------------------------------------------

# n = int(input("Enter an Integer: "))

# for i in range(1, n + 1):
#     print(i)


# ---------------------------------------------------------
# Q3. Reverse Counting
# ---------------------------------------------------------

# n = int(input("Enter an Integer: "))

# for i in range(n, 0, -1):
#     print(i)


# ---------------------------------------------------------
# Q4. Multiplication Table
# ---------------------------------------------------------

# n = int(input("Enter an Integer: "))

# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")


# ---------------------------------------------------------
# Q5. Sum of Numbers
# ---------------------------------------------------------

# n = int(input("Enter an Integer: "))

# total = 0

# for i in range(1, n + 1):
#     total += i

# print(total)


# ---------------------------------------------------------
# Q6. Factorial
# ---------------------------------------------------------

# n = int(input("Enter an Integer: "))

# factorial = 1

# for i in range(1, n + 1):
#     factorial *= i

# print(f"Factorial of {n} is {factorial}")


# ---------------------------------------------------------
# Q7. Sum of Even & Odd Numbers
# ---------------------------------------------------------

# n = int(input("Enter an Integer: "))

# even = 0
# odd = 0

# for i in range(1, n + 1):

#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i

# print("Even Sum:", even)
# print("Odd Sum:", odd)


# ---------------------------------------------------------
# Q8. Perfect Number
# ---------------------------------------------------------

# n = int(input("Enter an Integer: "))

# total = 0

# for i in range(1, n):

#     if n % i == 0:
#         total += i

# if total == n:
#     print("Perfect Number")

# else:
#     print("Not a Perfect Number")


# ---------------------------------------------------------
# Q9. Prime Number
# ---------------------------------------------------------

# n = int(input("Enter an Integer: "))

# factors = 0

# for i in range(1, n + 1):

#     if n % i == 0:
#         factors += 1

# if factors == 2:
#     print("Prime Number")

# else:
#     print("Composite Number")


# ---------------------------------------------------------
# Q10. Reverse a String
# ---------------------------------------------------------

# text = input("Enter a String: ")

# reverse = ""

# for i in range(len(text) - 1, -1, -1):
#     reverse += text[i]

# print(reverse)


# ---------------------------------------------------------
# Q11. Palindrome Check
# ---------------------------------------------------------

# text = input("Enter a String: ").lower()

# reverse = ""

# for i in range(len(text) - 1, -1, -1):
#     reverse += text[i]

# if text == reverse:
#     print("Palindrome")

# else:
#     print("Not a Palindrome")