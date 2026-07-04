"""
===========================================================
            PYTHON BASICS - PART 02
===========================================================

Topics Covered:
1. Functions
2. Lists
3. Tuples
4. Sets
5. Dictionaries
6. Practice Questions

Author : Muhammad Ibraheem
===========================================================
"""


# =========================================================
# 1. FUNCTIONS
# =========================================================

# ---------------------------------------------------------
# Example 1: Simple Function
# ---------------------------------------------------------

# def hello(name):
#     print(f"Hello {name}")

# hello("Ibraheem")


# =========================================================
# 2. LISTS
# =========================================================

# ---------------------------------------------------------
# List Example 1: Separate Positive & Negative Numbers
# ---------------------------------------------------------

# list1 = [2, 4, -2, 3, -4, 5, -3, 3, -3.4, -5.4, 74.2]

# def positive_negative(lst):
#
#     positive = []
#     negative = []
#
#     for item in lst:
#         if item >= 0:
#             positive.append(item)
#         else:
#             negative.append(item)
#
#     print("Positive:", positive)
#     print("Negative:", negative)

# positive_negative(list1)


# ---------------------------------------------------------
# List Example 2: Mean of List
# ---------------------------------------------------------

# numbers = [10, 20, 30, 40]

# def mean(lst):
#
#     total = 0
#
#     for num in lst:
#         total += num
#
#     return total / len(lst)

# print(mean(numbers))


# ---------------------------------------------------------
# List Example 3: Greatest Element
# ---------------------------------------------------------

# elements = [3, 2, 5, 32, 43, 54]

# def greatest_element(lst):
#
#     greatest = lst[0]
#
#     for item in lst:
#         if item > greatest:
#             greatest = item
#
#     return greatest

# print(greatest_element(elements))


# ---------------------------------------------------------
# List Example 4: Second Greatest Element
# ---------------------------------------------------------

# elements = [-33, -4, -3, -2, -53]

# def second_greatest(lst):
#
#     first = float("-inf")
#     second = float("-inf")
#
#     for item in lst:
#
#         if item > first:
#             second = first
#             first = item
#
#         elif second < item < first:
#             second = item
#
#     return second

# print(second_greatest(elements))


# ---------------------------------------------------------
# List Example 5: Move Zeros to End
# ---------------------------------------------------------

# def move_zeros(lst):
#
#     write_index = 0
#
#     for i in range(len(lst)):
#
#         if lst[i] != 0:
#             lst[write_index] = lst[i]
#             write_index += 1
#
#     for i in range(write_index, len(lst)):
#         lst[i] = 0
#
#     return lst

# numbers = [0, 9, 0, 3, 4, 0, 2]

# print(move_zeros(numbers))


# =========================================================
# LIST PRACTICE QUESTIONS
# =========================================================

# ---------------------------------------------------------
# Q1. Mean of List
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q2. Maximum Element & Index
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q3. Second Greatest Element
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q4. Check List is Sorted
# ---------------------------------------------------------

# ...

# ---------------------------------------------------------
# Q5. Reverse a List
# ---------------------------------------------------------

# ...


# =========================================================
# 3. TUPLES
# =========================================================

# ---------------------------------------------------------
# Example 1: Sum of Tuple Elements
# ---------------------------------------------------------

# tuple1 = (1, 3, 4, 5, 6)

# def tuple_sum(data):
#
#     total = 0
#
#     for value in data:
#         total += value
#
#     return total

# print(tuple_sum(tuple1))


# =========================================================
# 4. SETS
# =========================================================

# ---------------------------------------------------------
# Example 1: Set Methods
# ---------------------------------------------------------

# numbers = {1, 2, 3, 4, 5}

# numbers.add(10)
# numbers.remove(5)
# numbers.discard(100)
# numbers.pop()
# numbers.clear()

# print(numbers)


# ---------------------------------------------------------
# Example 2: Set Operations
# ---------------------------------------------------------

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# print(a | b)
# print(a & b)
# print(a - b)
# print(a.symmetric_difference(b))


# =========================================================
# 5. DICTIONARIES
# =========================================================

# ---------------------------------------------------------
# Example 1: Basic Dictionary
# ---------------------------------------------------------

# student = {
#     "name": "Ibraheem",
#     "department": "Information Technology",
#     "semester": 5
# }

# print(student)

