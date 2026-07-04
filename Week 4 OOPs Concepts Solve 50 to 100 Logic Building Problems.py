"""
===========================================================
            PYTHON BASICS - PART 04
===========================================================

Topics Covered:
1. Classes & Objects
2. Constructors
3. Instance Methods

Author : Muhammad Ibraheem
===========================================================
"""


# =========================================================
# 1. CLASSES & OBJECTS
# =========================================================

# A class is a blueprint for creating objects.
# An object is an instance of a class.


# ---------------------------------------------------------
# Example 1: Book Class
# ---------------------------------------------------------

# class Book:
#
#     def __init__(self, name, publisher, price):
#
#         self.name = name
#         self.publisher = publisher
#         self.price = price


# book1 = Book("English W/B-1", "Emaan Printers", 1040)
# book2 = Book("English W/B-2", "Emaan Printers", 2000)
# book3 = Book("English W/B-3", "Emaan Printers", 1440)
# book4 = Book("English W/B-4", "Emaan Printers", 1640)
# book5 = Book("English W/B-5", "Emaan Printers", 1350)

# print(f"{book1.name} : Rs. {book1.price}")
# print(f"{book2.name} : Rs. {book2.price}")
# print(f"{book3.name} : Rs. {book3.price}")
# print(f"{book4.name} : Rs. {book4.price}")
# print(f"{book5.name} : Rs. {book5.price}")


# =========================================================
# 2. CONSTRUCTORS (__init__)
# =========================================================

# The constructor (__init__) is automatically called
# whenever a new object is created.


# ---------------------------------------------------------
# Example 2: Bag Class
# ---------------------------------------------------------

# class Bag:
#
#     def __init__(self, color, zips, material):
#
#         self.color = color
#         self.zips = zips
#         self.material = material
#
#     def details(self):
#
#         print(
#             f"Bag Color : {self.color}\n"
#             f"Zips      : {self.zips}\n"
#             f"Material  : {self.material}"
#         )


# new_bag = Bag("White", 3, "Leather")

# new_bag.details()


# =========================================================
# PRACTICE QUESTIONS
# =========================================================

# ---------------------------------------------------------
# Q1. Create a Student Class
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q2. Create an Employee Class
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q3. Create a Car Class
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q4. Create a Mobile Class
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q5. Create a Bank Account Class
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q6. Create a Rectangle Class
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q7. Create a Circle Class
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q8. Create a Library Book Class
# ---------------------------------------------------------

# ...