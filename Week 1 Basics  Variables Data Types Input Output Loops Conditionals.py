#Type Conversion

                #int
# n= "2"
# n= int(n)
# print(type(n))
# print(n)
# print(type(n))



                #float() & Bool()

# n= 2.3
# n= bool(n)
# print(n)
# print(type(n))




                    #input & output

# name= input("Enter Your Name: ")
# age= input("Enter Your Age: ")

# age= int(age)

# print(f"Your Name is {name} and Your age is {age}")


# print(type(name))
# print(type(age))



                    #Operators

# a= 2
# b= 4

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)





                #Conditions

# money= int(input("Give me Money: "))

# if money >=10 and money <=20:
#     print("Give him a Cheegum")

# elif money >=20 and money <=30:
#     print("Give him a Cake")

# elif money >30:
#     print("Give him what hee want")
# else:
#     print("Go Back and Pick up some rupees")







                #Some Questions on Conditional Statements

#Qno1: Accept the two numbers and print greatest between them.


# a= int(input("Enter a Number: "))
# b= int(input("Enter a Number: "))


# if a > b:
#     print("A is Greater than B")

# else:
#     print("B is Greater than A")



# Qno2: Accept the gender and welcome as per gender status

# gender= input("Can you Please Tell us Your Gender (i.e: M/F): ")

# if gender=="M" or gender=="m":
#     print("Good Morning Sir")
# elif gender== "F"or gender=="f":
#     print("Good Morning Ma'am")
# else:
#     print("Enter a valid input Thanks😋")



# Qno3 Check the number is even or ODD

# num= int(input("Enter a Number"))


# if num% 2==0:
#     print(f"{num} is EVEN Number")
# else:
#     print(f"{num} is ODD Number")


                                    #loops


# a=  range(10, 50, 5)


# for i in a:
#     print(i)


# a= "Printing"

# for i in range(len(a)):
#     print(a[i])


# for i in range(1,31):
#     if i==4:
        
#         print("Break is Executed")
#         break
#     print(i)
# else:
#         print("Break is not Executed")



                        # Questions on Loop

# Qno1: 

# n= int(input("Give an Integer: "))

# for i in range(1,n+1):
#     print("Hello World")




# Qno2: Print Natural Natural Numbers up to n

# n= int(input("Tell me an Integer: "))

# for i in range(1,n+1):
#     print(i)


# Qno3: Reverser For Loop and print n to 1:

# n= int(input("Tell me an Integer: "))

# for i in range(n, 0, -1):
#     print(i)


# Qno4 Take a Number and print its Table

# n= int(input("Tell me an Integer: "))

# for i in range(1,11):
#     if i>10:
#         break
#     else:
#         print(f"{n}x{i} = {n*i}")


# Qno5 Sum of All Integers numbers till n

# n= int(input("Tell me an Integer: "))

# sum= 0

# for i in range(1,n+1):
#     sum+=i

# print(sum)

# Qno6 Factorial of a Number

# n= int(input("Tell me an Integer: "))

# factorial=1

# for i in range(1, n+1):
#     factorial*=i

# print(f"Factorial of {n} is {factorial}")


# Qno7 Find the sum of Even and ODD numbers Seperately

# n= int(input("Tell me an Integer: "))

# Even= 0
# Odd=0


# for i in range(1, n+1):
#     if i % 2==0:
#         Even+=i
#     else:
#         Odd+=i


# print(f"Sum of All Even Numbers Till {n} is  : {Even}")
# print(f"Sum of All Odd Numbers Till {n} is  : {Odd}")



# Qno7 Find Factors of a Number

# n= int(input("Tell me an Integer: "))

# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i

# if sum==n:
#     print(f"{n} is Perfect Number ")
# else:
#     print(f"{n} is not Perfect Number ")
    


# Qno8 Check Number is Prime or Not

# n= int(input("Tell me an Integer: "))

# Factors=0


# for i in range(1,n+1):
#     if n%i==0:
#         Factors+=1


# if Factors==2:
#     print(f"{n} is a Prime Number")
# else:
#     print(f"{n} is a Composite Number")


# Qno9: Reverse an String

# string= str(input("Give me String That You want to Reverse: "))

# ubti=""

# for i in range(len(string)-1, -1, -1):
#     ubti+=string[i]
# print(ubti)



# Qn10: Check string is Pallindrome or not


# string= str(input("Check String is Pallindrome or Not:- ")).lower()
# reverse=""

# for i in range(len(string)-1,-1,-1):
#     reverse+=string[i]


# print(string)
# if string==reverse:
#     print("String is Pallindrome")
# else:
#     print("String is not Pallindrome")


