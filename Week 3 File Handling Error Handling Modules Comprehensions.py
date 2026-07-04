"""
===========================================================
            PYTHON BASICS - PART 03
===========================================================

Topics Covered:
1. File Handling
2. File Modes
3. Exception Handling
4. File Handling Practice

Author : Muhammad Ibraheem
===========================================================
"""


# =========================================================
# 1. FILE HANDLING
# =========================================================

# Python provides built-in functions to create, read,
# write, append, and manage files.


# =========================================================
# FILE MODES
# =========================================================

# r  -> Read (File must exist)
# w  -> Write (Creates file if not exists, overwrites data)
# a  -> Append (Adds new content at the end)
# x  -> Create (Fails if file already exists)
# r+ -> Read & Write
# w+ -> Write & Read
# a+ -> Append & Read


# =========================================================
# EXAMPLE 1 : APPEND MODE ('a')
# =========================================================

# try:
#
#     file = open("sample.txt", "a")
#
#     file.write("\nHello! This line was appended.")
#
#     file.close()
#
#     print("Content appended successfully.")
#
# except Exception as error:
#
#     print(error)


# =========================================================
# EXAMPLE 2 : WRITE MODE ('w')
# =========================================================

# try:
#
#     file = open("sample.txt", "w")
#
#     file.write("Hello! This file was created using write mode.")
#
#     file.close()
#
#     print("File written successfully.")
#
# except Exception as error:
#
#     print(error)


# =========================================================
# EXAMPLE 3 : READ MODE ('r')
# =========================================================

# try:
#
#     file = open("sample.txt", "r")
#
#     print(file.read())
#
#     file.close()
#
# except Exception as error:
#
#     print(error)


# =========================================================
# EXAMPLE 4 : CREATE MODE ('x')
# =========================================================

# try:
#
#     file = open("new_file.txt", "x")
#
#     file.write("This file was created using 'x' mode.")
#
#     file.close()
#
#     print("File created successfully.")
#
# except Exception as error:
#
#     print(error)


# =========================================================
# EXAMPLE 5 : READ LINE BY LINE
# =========================================================

# try:
#
#     file = open("sample.txt", "r")
#
#     for line in file:
#         print(line.strip())
#
#     file.close()
#
# except Exception as error:
#
#     print(error)


# =========================================================
# EXAMPLE 6 : READ ALL LINES
# =========================================================

# try:
#
#     file = open("sample.txt", "r")
#
#     lines = file.readlines()
#
#     print(lines)
#
#     file.close()
#
# except Exception as error:
#
#     print(error)


# =========================================================
# EXAMPLE 7 : WITH STATEMENT (Recommended)
# =========================================================

# try:
#
#     with open("sample.txt", "r") as file:
#
#         print(file.read())
#
# except Exception as error:
#
#     print(error)


# =========================================================
# EXCEPTION HANDLING
# =========================================================

# try:
#
#     file = open("sample.txt", "r")
#
# except FileNotFoundError:
#
#     print("File does not exist.")
#
# except PermissionError:
#
#     print("Permission denied.")
#
# except Exception as error:
#
#     print(error)


# =========================================================
# FILE HANDLING PRACTICE
# =========================================================

# ---------------------------------------------------------
# Q1. Create a File
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q2. Write Data into a File
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q3. Read Data from a File
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q4. Append Data into a File
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q5. Count Number of Lines in a File
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q6. Count Number of Words in a File
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q7. Copy Content from One File to Another
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q8. Search a Word in a File
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q9. Count Frequency of Characters
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q10. Read File Line by Line
# ---------------------------------------------------------

# ...


# =========================================================
# MINI PROJECT
# =========================================================

# File Handling Project
#
# Ideas:
#
# 1. Student Record Management System
# 2. Contact Book
# 3. To-Do List
# 4. Notes Manager
# 5. Expense Tracker