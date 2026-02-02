
                        # Functions in python


# def  hello(name):
#     print(f"Hello {name}")


# hello("Ibraheem")



    


                            # List

# a= [2,4,-2,3,-4,5,-3,3,-3.4,-5.4,74.2]


# a.insert(0,1)
# a.extend([100,200,300,400,500,600])
# a.remove(4)
# popped_item= a.pop(4)

# positive=[]
# negative=[]

# for i in range(len(a)):
#     if a[i] >=0:
#         positive.append(a[i])
#     else:
#         negative.append(a[i])


# print("Positive Numbers are: ", positive)
# print("Negative Numbers are: ", negative)





# Qno2: Mean of list elements

# def mean_of_list(lst):
#     sum=0
#     for i in lst:
#         sum+=i
#         mean= sum/len(lst)
#     return mean

# a= [2,4,6,8,10]
# print(mean_of_list(a))




                    # Qno3: Find Maximum element and its index

# a=[1000,13,14,15,16,17,18,19,20,1,2,3,4,5,6,7,8,9,1000]

# def findel(lst):
#     max= 0
#     indx=0
#     for i in range(len(lst)):
#         if max < lst[i]:
#             max= lst[i]
#             indx= i
#     print(f"Maximum Element is:{max} and located at index of  {indx}")

# findel(a)


#  Find the second greatest element?

# def second_greatest(lst):
#     max= SecMax= float('-inf')
#     for i in lst:
#         if i > max:
#             SecMax= max
#             max= i
#         elif i > SecMax and i != max:
#             SecMax= i
#     print(f"Greatest Element is: {max}")
#     print(f"Second Greatest Element is: {SecMax}")


# a=[4001,2,4,5,23,23,523,23,583,23,65,45,3485]

# second_greatest(a)

 
 
 
#  Qno4 Check list is sorted or not


# def check_sorted(lst):
    
#     for i in range(len(lst)-1):
#         if lst[i] < lst[i+1]:
#             continue
#         else:
#             print("Your list is not sorted")
#             break
#     else:
#         print("Your List  is Sorted")
        


# a= [12,13,14,23,24,32]

# check_sorted(a)





                    # Write a function to reverse a list.

# a=[-10,2,3,1,3,2,4,5]

# def reverse_lst(lst):
#     reversed_lst=[]
#     for i in range(len(lst)-1,-1,-1):
#         reversed_lst.append(lst[i])
    
#     print(reversed_lst)

# reverse_lst(a)


# 6. Create a tuple and prints its sume of  elements.


# a=(1,3,4,5,6,7,8,9,12,20,25,-50,50/2)

# def print_Sum(tupl):
#     sum=0
#     for i in range(len(tupl)):
#          sum+=tupl[i]
#     return sum

# print(f"Sum of Tuple is: {print_Sum(a)}")

# # Create set and perform it's methods

# A_set={1,2,3,4,2,4,2,34,1,3,5,8}

# # A_set.add("Hello") #Add to set varaible Element position based on hashing
# # A_set.remove(5) #Removes given element if not found raise error
# # A_set.discard(53) # Removes given element if not found no raise error
# # A_set.pop() #Removes random element
# A_set.clear()  # Removes all element make it empty set

# print(type(A_set))

# print(A_set)



#                         # Set Operations b/w two sets
                        
# a={1,2,3,4,5}
# b= {4,5,6,7,8}


# # se= a.union(b) #Union 
# # se= a|b # union Shortcut
# # se= a.intersection(b) #intersection
# # se= b-a # Diference
# se= a.symmetric_difference(b) # Sementric_Diference
# print(se)
# # print(type(se))


#                 #Dictionaries

# a= {
#     "name": "Ibraheem",
#     "department": "Information Technology",
#     "Semester": 5,
#     "HoD": "Dr. Sheeba Memon",
#     }
    
# a["greets"]= { 
#         "msg": f"hello {a["name"]} from Department of {a["department"]} Head of  Department: {a["HoD"]}, and currently in {a["Semester"]}Semester",
#         }
    
# print (a["greets"]["msg"])




# Qno2: Create a dictionary and print keys and values separately
# 9. Write a function to count the frequency of elements in a list.
# a=[1,2,3,3,4,3,2,2,3,2,3,2,2,3,2,2,2,2]

# def Freq_count(lst, n):
#     return a.count(n)

# print(Freq_count(a,3))

# 10. Create a dictionary of squares of numbers from 1 to 10.

# def square_dic(fr,to):
#     sq={}
#     to+=1
#     for i in range(fr,to):
#         sq[i]= i*i
#     return sq
    

# print(square_dic(10,100))



# # 11. Create a nested dictionary to represent a student with details like name, age, and subjects (each subject with its own dictionary of marks).
# try:
#     import random

#     class_result={
#     1:{
#         "name": "Hamza",
#         "age": 23,
#         "subjects":{
#             "DB": random.randint(40,100),
#             "Web": random.randint(40,100),
#             "P&S": random.randint(40,100),
#             "DS": random.randint(40,100),
#             "OS": random.randint(40,100),
#             "CN": random.randint(40,100)
#         }
#     },
#     2: {
#         "name": "Salman",
#         "age": 22,
#         "subjects":{
#             "DB": random.randint(40,100),
#             "Web": random.randint(40,100),
#             "P&S": random.randint(40,100),
#             "DS": random.randint(40,100),
#             "OS": random.randint(40,100),
#             "CN": random.randint(40,100)
#         }
#     },
#     3:{
#         "name": "Sheroze",
#         "age": 25,
#         "subjects":{
#             "DB": random.randint(40,100),
#             "Web": random.randint(40,100),
#             "P&S": random.randint(40,100),
#             "DS": random.randint(40,100),
#             "OS": random.randint(40,100),
#             "CN": random.randint(40,100)
#         }
#     },
#     4:{
#         "name": "Taha",
#         "age": 23,
#         "subjects":{
#             "DB": random.randint(40,100),
#             "Web": random.randint(40,100),
#             "P&S": random.randint(40,100),
#             "DS": random.randint(40,100),
#             "OS": random.randint(40,100),
#             "CN": random.randint(40,100)
#         }
#     },
#     5:{
#         "name": "Aswad",
#         "age": 23,
#         "subjects":{
#             "DB": random.randint(40,100),
#             "Web": random.randint(40,100),
#             "P&S": random.randint(40,100),
#             "DS": random.randint(40,100),
#             "OS": random.randint(40,100),
#             "CN": random.randint(40,100)
#         }
#     },
#     6:{
#         "name": "Zubair",
#         "age": 23,
#         "subjects":{
#             "DB": random.randint(40,100),
#             "Web": random.randint(40,100),
#             "P&S": random.randint(40,100),
#             "DS": random.randint(40,100),
#             "OS": random.randint(40,100),
#             "CN": random.randint(40,100)
#         }
#     },
#     7:{
#         "name": "Shaheer",
#         "age": 23,
#         "subjects":{
#             "DB": random.randint(40,100),
#             "Web": random.randint(40,100),
#             "P&S": random.randint(40,100),
#             "DS": random.randint(40,100),
#             "OS": random.randint(40,100),
#             "CN": random.randint(40,100)
#         }
#     },
#     8:{
#         "name": "Uzair",
#         "age": 23,
#         "subjects":{
#             "DB": random.randint(40,100),
#             "Web": random.randint(40,100),
#             "P&S": random.randint(40,100),
#             "DS": random.randint(40,100),
#             "OS": random.randint(40,100),
#             "CN": random.randint(40,100)
#         }
#     },
#     9:{
#         "name": "Sahil",
#         "age": 23,
#         "subjects":{
#             "DB": random.randint(40,100),
#             "Web": random.randint(40,100),
#             "P&S": random.randint(40,100),
#             "DS": random.randint(40,100),
#             "OS": random.randint(40,100),
#             "CN": random.randint(40,100)
#         }
#     },
#     10:{
#         "name": "Sheeraz",
#         "age": 24,
#         "subjects":{
#             "DB": random.randint(40,100),
#             "Web": random.randint(40,100),
#             "P&S": random.randint(40,100),
#             "DS": random.randint(40,100),
#             "OS": random.randint(40,100),
#             "CN": random.randint(40,100)
#         }
#     }
# }


#     def marksheet(Roll):
#         if Roll in class_result:
#             print("\t\t\t\t***Marksheet****\n\n")
#             print(f"Name\t:\t {class_result[Roll]["name"]}")
#             print(f"Roll No\t:\t BSIT-2024-0{Roll}\n\n\n")
            
            
#             print(f"\t\t\t Sr.\t\t Subject\t\t\t Marks")
            
#             print(f"\t\t\t 1.\t\t\tDatabase\t\t\t\t {class_result[Roll]["subjects"]["DB"]}")
#             print(f"\t\t\t 2.\t\t\tWeb Tech\t\t\t\t {class_result[Roll]["subjects"]["Web"]}")
#             print(f"\t\t\t 3.\t\t\tStatistics\t\t\t\t {class_result[Roll]["subjects"]["P&S"]}")
#             print(f"\t\t\t 4.\t\t\tWeb Discrete\t\t\t {class_result[Roll]["subjects"]["DS"]}")
#             print(f"\t\t\t 5.\t\t\tOperating System\t\t {class_result[Roll]["subjects"]["OS"]}")
#             print(f"\t\t\t 6.\t\t\t Computer Networks\t\t {class_result[Roll]["subjects"]["CN"]}")
            
            
#         else:
#             print(f"Student with {Roll} this Roll number Not Found")

        


#     marksheet(2)

# except:
#       print("An exception occurred") 



# 8. Write a program to merge two dictionaries.


# a={1:10,2:20,30:300,}
# b={10:30,20:200,30:400,1:3}



# def merge_dict(a,b):
    
#     for i in b:
#         a[i]=b[i]
            

# print(merge_dict(a,b))
# print(a)
# print(b)



# Qno9: Create a dictionary from two lists (one for keys and another for values).

# a=[1,2,3,4,5,6,7,8,9,10]
# b=[1,4,9,16,25,36,49,64,81,100]


# def listToDict(a,b):
#     dictionry={}
#     for i in range(len(a)):
#         dictionry[a[i]]= b[i]
    
#     return dictionry


# print(listToDict(a,b))
# print(type(listToDict(a,b)))


# Qno10: Write a program to count occurrences of each word in a given string using a dictionary.

# a=str(input("Give me string: "))


# def count_words(str):
#     str.lower()
#     counts={}
    
#     words= str.split()
    
#     for word in words:
#         if word in counts:
#             counts[word]+=1
#         else:
#             counts[word]=1

#     return counts
    


# dicts= count_words(a)


# print(dicts)

# print(type(dicts))


# Qno11: Create a dictionary that maps each character in a string to its frequency.

# a="Hello I am Muhammad Ibraheem from Hyderabad and I am studing in GC University Hyderabad"


# def char_counts(str):
#     str.lower()
#     count={}
    
#     for chars in str:
#         if chars in count:
#             count[chars]+=1
#         else:
#             count[chars]=1
            
            
#     return count
    
    
# print(char_counts(a))
# print(type(char_counts(a)))


    # 12. Create a program to check if a key exists in a dictionary.
# a={
#     "name": "Ibraheem",   
#     "age": 23,
#     "department": "IT",
#     "semester": 5
# }
# key= str(input("Enter Key to check its existence in Dictionary: "))


# def search_Key(dic, key):
#     if key in dic:
#         print("Key is valid")
#         print(f"Value is of {key} is {dic[key]}")
#     else:
#         print("Invalid Key")
#         print(f"Not found any key about: {key}")


# search_Key(a,key)
   





# # 14. Write a function to find common elements in two lists.
# a=[65,1,2,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20]
# b=[3,4,5,6,7,8,9,10,12,14,65]


# def check_common(a,b):
#     common=[]
#     for i in range(len(a)):
#         if a[i] in b:
#             common.append(a[i])
#     return common        
            
# print(check_common(a,b))



# 15. Write a function to count vowels in a string.
# a=str(input("Give me String: "))

# def check_vowels(str):
#     vowels="aeiou"
#     count=0
#     for i in str:
#         if i in vowels:
#             count+=1
#     return count


# print(check_vowels(a))




# 16. Write a function to remove all punctuation from a string.

# a=str(input("Give me String: "))

# def removePunct(str):
#     all_symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#     for i in str:
#         if i in all_symbols:
#             str=  str.replace(i,"")
#     return str
    
# print(removePunct(a))
