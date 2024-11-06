
# loop

# def nForest(n):
#     for i in range(n):
#         for j in range (n):
#             print('*',end=' ')
#         print()
# nForest(4)



# def nForest(n):
#     for i in range(n):
#         for j in range(i+1):
#             print('*',end=' ')
#         print()
# nForest(5)


# def nTriangle(n):
#     for i in range(n):
#         for j in range(i+1):
#             print(j+1,end=' ')
#         print()
# nTriangle(5)


# def nTriangle(n):
#     for i in range(n):
#         for j in range(i+1):
#             print(i+1,end='')
#         print()
# nTriangle(5)



# def nTriangle(n):
#     for i in range(n):
#         for j in range(n-i):
#             print('*',end=' ')
#         print()
# nTriangle(5)



# def nTriangle(n):
#     for i in range(n):
#         for j in range(n-i):
#             print(j+1,end=' ')
#         print()
# nTriangle(5)



# def pyramid(n):
#     for i in range(1,n+1):
#         print(' ' * (n-i),end='')
#         print('* ' * i)
# pyramid(5)



# def pyramid(n):
#     for i in range(n,0,-1):
#         print(' ' *(n-i),end='')
#         print('* ' *i)
# pyramid(5)





# 1 .round the no


# import math
# def round_no(n):
#     return math.floor(n+0.5)
#     # print(round(n))
# print(round_no(50.4))




# n=50.5
# if n%1 >=0.5:
#     n= round(n+0.5)
# else:
#     n=round(n)
# print(n)



# 2. Sorting


# Bubble

# Bubble Sort compares adjacent elements and swaps them if they are in the wrong order.
# This process is repeated until the entire list is sorted.
# [3,9,1,4] -compare 39,91,94[3,1,4,9] -31,34,49[1,3,4,9]

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 # Swap if the element found is greater than the next element
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
# arr = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(arr)
# print("Sorted array:", arr)



# Selection

# find the minimum no for the list and swap the no to the first array,then fist element is sorted 
# then find minimum no in list and swap to second element and continue the steps
# [6,2,8,9,1]--[1,2,8,9,6]-[1,2,6,9,8]--[1,2,6,8,9]

# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_idx = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         # Swap the found minimum element with the first element
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
# arr = [64, 25, 12, 22, 11]
# selection_sort(arr)
# print("Sorted array:", arr)



# Insertion

# Insertion Sort builds a sorted array one element at a time by taking elements from the 
# unsorted part and inserting them into the correct position in the sorted part.
# [4,2,1,3,8]--[2,4,1,3,8]--[1,2,4,3,8]--[1,2,3,4,8]

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         # Move elements that are greater than the key to one position ahead
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j] 
#             j -= 1
#         arr[j + 1] = key
# arr = [12, 11, 13, 5, 6]
# insertion_sort(arr)
# print("Sorted array:", arr)



# Merge

# Merge Sort is a divide-and-conquer algorithm that splits the array into two halves, 
# recursively sorts each half, and then merges the sorted halves together.



# Quick 

# Quick Sort is another divide-and-conquer algorithm that selects a "pivot"
# element and partitions the array into two subarrays: elements less than the pivot 
# and elements greater than the pivot.It then recursively sorts the subarrays.


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[len(arr) // 2]
#         left = [x for x in arr if x < pivot]
#         middle = [x for x in arr if x == pivot]
#         right = [x for x in arr if x > pivot]
#         return quick_sort(left) + middle + quick_sort(right)
# arr = [10, 7, 8, 9, 1, 5]
# sorted_arr = quick_sort(arr)
# print("Sorted array:", sorted_arr)


            

# Heap

# Heap Sort is a comparison-based algorithm that uses a binary heap data structure to sort elements.It first 
# builds a max-heap from the array and then repeatedly extracts the largest element (the root) and rebuilds the heap.



# number

# def sort_list(lst):
#     return sorted(lst)
# numbers = [64, 34, 25, 12, 22, 11, 90]
# print(sort_list(numbers))



# n=[34,56,98,21,12,4,5,42]
# numbers  =sorted(n)
# # n.sort()

# # n.sort(reverse=True)
# print(numbers)



# String

# def reverse(s):
#     return s[::-1]
# s='Hello'
# print(reverse(s))

# n='kavin'
# print (n[::-1])



# 3. Palindrome

# def is_palindrome(s):
#     return s == s[::-1]
# s = "madam"
# # print(s==s[::-1])
# print(is_palindrome(s))



# 4. Factorial   


# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result *=i
#     return result
# n=5
# print(factorial(n))




# 5. fibonacci sequence


# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=' ')
#         a, b = b, a + b
# n = 20
# fibonacci(n)



# 6. Prime Number

# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
# number = 24
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")



# 7. Armstrong

# def is_armstrong_number(number):
#     num_str = str(number)
#     num_digits = len(num_str)
#     total = 0
#     for i in num_str:
#         total += int(i) ** num_digits
#     return total == number
# number = int(input("Enter a number: "))
# if is_armstrong_number(number):
#     print( "Armstrong number.")
# else:
#     print("Not an Armstrong number.")


# 8 .Miximum and maximum

# def find_max_min(lst):
#     return max(lst), min(lst)
# numbers = [10,64, 34, 252, 12, 22, 11, 100]
# print(find_max_min(numbers))


# def max_value(lst):
#     max_value=0
#     for i in lst:
#         if i>max_value:
#             max_value=i
#     return max_value
# number=[10,64, 34, 25, 125, 22, 11, 100]
# print(max_value(number))
        




# # 9.Sum of Digits in a Number

# def digits(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     return total
# n = 1234
# print(digits(n))




# n = 1234
# digits = 0
# while n > 0:
#     digits += n % 10
#     n //= 10  
# if digits % 3 == 0:
#     print("The sum of digits is divisible by 3.")
# else:
#     print("The sum of digits is not divisible by 3.")




# Mutiple of numbers

# def solve(A):
#         if A==0:
#             return 0
#         product = 1
#         while A > 0:
#             digit = A % 10
#             product *= digit
#             A //= 10
#         return product
# A=1234
# print(solve(A))



# mutiple in list

# def multiply_list_elements(lst):
#     product = 1
#     for num in lst:
#         if num !=0:
#             product *= num
#     return product
# lst = [0,1, 2, 3,5]
# result = multiply_list_elements(lst)
# print(result)




# 10. GCD (Greatest Common Divisor) or HCF(Highest Common Factor)
# The GCD of two numbers is defined as the largest integer that divides both integers without any remainder. 
# divide

# def gcd(a, b):
#     while b !=0:
#         a, b = b, a % b
#     return a
# print(gcd(48, 18))


# 11. LCM (Least Common Multiple)
# The LCM of two numbers is defined as the smallest integer which is a multiple of both integers.
# LCM

# import math
# def lcm(a, b):
#     return abs(a*b) // math.gcd(a, b)
# print(lcm(12, 15))




# 12. Counting Number of Digits in a Number

# def count_digits(n):
#     return len(str(n))
# n = 12345098
# print(count_digits(n))




# decimal to binary

# def flip_bits(A):
#     binary_rep = bin(A)[2:]
#     flipped_bits = ''
#     for bit in binary_rep:
#         if bit == '0':
#             flipped_bits += '1'
#         else:
#             flipped_bits += '0'
#     result = int(flipped_bits, 2)
#     return result
# A1 = 7
# A2 = 5
# print(flip_bits(A1))  # Output: 0
# print(flip_bits(A2))  # Output: 2






# def move_zeros_to_end(A):
#     result = []
#     zero_count = 0
#     for num in A:
#         if num == 0:
#             zero_count += 1  # Count the zeros
#         else:
#             result.append(num)  # Append non-zero elements to result
#     result.extend([0] * zero_count)
#     return result
# A1 = [0, 1, 2, 3]
# A2 = [1, 0, 4,0, 0,5]
# print(move_zeros_to_end(A1))  # Output: [1, 2, 3, 0]
# print(move_zeros_to_end(A2))  # Output: [1, 0, 0, 0]






#Leap 

# def is_leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# class Solution:
#     def solve(self, A):
#         if (A % 4 == 0 and A % 100 != 0) or (A % 400 == 0):
#             return 1
#         else:
#             return 0 



# def sum_of_natural_numbers(n):
    # return n * (n + 1) // 2



# def multiply_string_digits(s):
#     product = 1
#     for char in s:
#         product *= int(char)
#     return product

# # Multiply digits in the string '123'
# s = '123'
# result = multiply_string_digits(s)
# print(result)  # Output: 6 (1 * 2 * 3)



































# import math
# def countDigits(n):
#     cnt = int(math.log10(n) + 1)
#     return cnt

# # Main function
# if __name__ == "__main__":
#     N = 329823
#     print("N:", N)
#     digits = countDigits(N)
#     print("Number of Digits in N:", digits)
                                
                            












# Python: Python is a high-level, interpreted programming language that supports 
# multiple programming paradigms, including procedural, functional, and object-oriented programming.

# A simple Python script
# def greet(name):
#     return f"Hello, {name}!"
# print(greet("Alice"))


# oops mainly used in java 
# rarely used in python and C++

# OOP: Object-Oriented Programming is a paradigm that organizes software design around data, or
# objects, rather than functions and logic. OOP focuses on classes and objects to create models
# based on the real world.

# An example of OOP in Python
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return f"Hello, {self.name}!"
# p = Person("Alice")
# print(p.greet())



# numbers = input("Enter 4 numbers without spaces: ")
# total = 0
# l= []
# for digit in numbers:
#     total += int(digit)
#     l.append(int(digit))
# print("Sum of the numbers:",total)
# print("List of individual digits:",l)



# x=2123
# name='kavin'
# def add(x,name):
#     print('The sum is:',x+name)

# def Product(x,name):
#     print("The product is :",x*name)

##Basic of python

# mutable
# List
# append("orange"),   insert(1)
# pop(1) ,   remove("banana"),    del thislist[0] ,   clear()
# pop will remove last element 
# push will add last in the list


# immutable
# tuple ()

# tuples=("")
# y=list(tuples)
# y.append("apple")
# y.remove("apple")
# tuples=tuple(y)
# print(tuples)


# set {}

# set.add{"orange"}
# thisset.update(tropical) combine two sets
# set.remove("Orange")
# set.discard("Orange")
# pop also remove first element in set{} but it will be printed
# clear() 


# dict

# thisdict["color"] = "red"
# pop
# popitem -remove all the details
# clear
# thisdict.update({"color": "black"})

# i=0
# j=0
# for i in range (10):
#     for j in range(10):
#         print(i,j)


# for i in range(1,11):
#     print(i,"x 2 = ",i*2)


# years=["1st year","2nd year","3rd year","4th year"]
# for i in years:
#     sem=["1st sem","2nd sem"]
#     for j in sem:
#         print(f"{i} - {j} padiche aganum")





# total=0
# for i in [1,2,3,4,5]:
#     if i ==4:
#         break
#     total=total+i
# print(total)



# int=3534654
# string="any value" (Double arrow mark)
# float=34.44     #decimal value
# List=["kavin","jai",123,34]    #list inside string
# set={'nivash','pravin','kavin'}
# Dictionary={'name':'kavin','age':19,'gender':'male'}
# Tuple=("kavin","pravin","nivash")
#boolean=true,false

#String=Tuple= immutable(we cannot change the value)
#List= mutable 

# Booleans

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")           # b is not greater than a
# print(10>9)              # True
    

# string methods

# a = "Hello, World!"
# print(a[1])               # Ans :e             

# a = "Hello, World!"
# print(len(a))              #Ans: 13

# txt = "The best things in life are free!"
# print("free" in txt)          # True


# String Slicing 

# b = "Hello, World!"
# print(b[2:5])                   # Ans:llo

# b = "Hello, World!"
# print(b[-5:-2])                   Ans:rld


# s = "racecar"
# print(s==s[::-1]) 




# Modify String

# a = "Hello, World!"              
# print(a.upper())                 # Ans:HELLO, WORLD!
# print(a.lower())                 #   Ans:hello, world!
# a = " Hello, World! "
# print(a.strip())                 #  Hello, World!            
# a = "Hello, World!"
# print(a.replace("H", "J"))       #  Jello, World!

# etc

# concatenate string

# a = "Hello"
# b = "World"
# c = a + b
# print(c)                         # Ans :HelloWorld

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)                            #  Hello World

# Format string
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))                  # My name is John, and I am 36



# Operators

# +   Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y	
# Python Assignment Operators
# Assignment operators are used to assign values to variables:

# Operator	Example	Same As	Try it
# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3	
# Python Comparison Operators
# Comparison operators are used to compare two values:

# Operator	Name	Example	Try it
# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y	



# List
# append,insert
# pop ,remove,del

# thislist = ["apple", "banana", "cherry"]
# print(thislist)                            #   ['apple', 'banana', 'cherry']


# Changes item  LIST

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)                         #  ['apple', 'blackcurrant', 'cherry']


# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)                          #  ['apple', 'banana', 'watermelon', 'cherry']


# Add item list

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)                       # ['apple', 'banana', 'cherry', 'orange']
 
 
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)                        #   ['apple', 'orange', 'banana', 'cherry']
 
 
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)                  # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)                    # ['apple', 'banana', 'cherry', 'kiwi', 'orange']
 
 
# Remove item

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)                     #  ['apple', 'cherry']


# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)                  # ['apple', 'cherry']      
 
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)                   # ['apple', 'banana']

 
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)                     # ['banana', 'cherry']
 
# thislist = ["apple", "banana", "cherry"]
# del thislist                          # Empty


# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)                          # []

# Looping 


# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

 
#  Sort the list

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()                            # [23, 50, 65, 82, 100]
# print(thislist)


#  Join the list

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)                             # ['a', 'b', 'c', 1, 2, 3]
 
 
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)
# print(list1)                         #  ['a', 'b', 'c', 1, 2, 3]
 
 
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)                          #  ['a', 'b', 'c', 1, 2, 3]
 
 
 
#  Tuple 


# thistuple = tuple(("apple", "banana", "cherry"))
# print(thistuple)                      #  ('apple', 'banana', 'cherry')


# change tuple values

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)                            # ('apple', 'kiwi', 'cherry')

# Add items

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# print(thistuple)                   #  ('apple', 'banana', 'cherry', 'orange')

    
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)                     #   ('apple', 'banana', 'cherry', 'orange')
    

# Remove items


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)                        # ('banana', 'cherry')

# Looping

# thistuple = ("apple", "banana", "cherry")                 #Ans:  apple
                                                            #     banana
                                                            #     cherry
# # for x in thistuple: 
#   print(x)


# i=1
# while i<10:
#     print(i)
#     if i==6:
#         break;
#     i+=1
    
    
# While loop

# thistuple = ("apple", "banana", "cherry")
# i = 0                                                   # apple
# while i < len(thistuple):                                # banana
#   print(thistuple[i])                                     # cherry
#   i = i + 1



# Dictionary
 
 
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])                  # Ford
 
 
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)                       #  {'name': 'John', 'age': 36, 'country': 'Norway'}
 

   
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.keys()
# print(x) #before the change
# car["color"] = "white"
# print(x)                       #dict_keys(['brand', 'model', 'year'])
                                   # dict_keys(['brand', 'model', 'year', 'color'])



# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.values()
# print(x) #before the change
# car["year"] = 2020
# print(x)                         #  dict_values(['Ford', 'Mustang', 1964])
# #                                    #  dict_values(['Ford', 'Mustang', 2020])#           

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.items()
# print(x) #before the change
# car["year"] = 2020
# print(x)                         # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
#                                    # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:                  # Yes, 'model' is one of the keys in the thisdict dictionary
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018
# print(thisdict)                           # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# print(thisdict)                          # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Add item

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)                           # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})
# print(thisdict)                          #  {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)                           # {'brand': 'Ford', 'year': 1964}


# Delete item

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)                         # {'brand': 'Ford', 'model': 'Mustang'}

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)                           # {'brand': 'Ford', 'year': 1964}


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)                           #  {}
# 


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)                    #   {'brand': 'Ford', 'year': 1964}


# Nested loop  Dictionary

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
                    #Ans:  {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007},
                    #    'child3': {'name': 'Linus', 'year': 2011}}
# print(myfamily)



# sets

# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)                         # {'banana', 'apple', 'cherry'} 


# Add set item

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)                                 # apple
                                            # banana
                                            # cherry
  
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)                             # {'cherry', 'orange', 'banana', 'apple'}
 

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)                       # {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}            




# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)                        # {'banana', 'cherry', 'apple', 'orange', 'kiwi'}                    


# Remove set item

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)                               # {'apple', 'cherry'}


# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)                              # {'cherry', 'apple'}


# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x) #removed item
# print(thisset) #the set after removal             #  cherry
                                                   # {'apple', 'banana'}


# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)                                  # set()


# If else

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")             #  a is greater than b

# While Loop

# i = 1
# while i < 6:
#   print(i)
#   i += 1                         #  1 2 3 4 5              

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1                     #   1 2 3 

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)                 # 1 2 3 4 5 6


# Looping

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:                      #   apple
                                        #    banana
                                        #  cherry
#   print(x)                            








# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x) 
#   if x == "banana":                  #   apple
#                                     #   banana
#     break


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         break
#     print(x)                    #    apple


# Range Function

# for x in range(6):
#   print(x,end= " ")               #  0 1 2 3 4 5


# Function

# def my_function(*kids):
#   print("The youngest child is " + kids[2])
# my_function("Emil", "Tobias", "Linus")              #   The youngest child is Linus


# def my_function(**kid):
#   print("His last name is " + kid["lname"])
# my_function(fname = "Tobias", lname = "Refsnes")        # His last name is Refsnes


# def my_function(food):
#   for x in food:
#     print(x)
# food = ["apple", "banana", "cherry"]
# my_function(food)


# def my_function(x):
#   return 5 * x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))                   #  15 25 45


# # Inside function Argument or parameter

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")                    # Emil Refsnes




# Time complexity

# # Big 0 notation
# 0(1)  constant 
# 0(n)  Linear 
# 0(logN)  lograthmic
# 0(NlogN)  Linear lograthmic
# 0(n^2)  Quadratic
# 0(n^3)
# 2^n

# omega 
# Theta


# # 0(1)  It will print Exactly 10 'Hi' so it is constant term
# print("Hi")
# print("Hi")
# print("Hi")
# print("Hi")
# print("Hi")

# a=2
# b=20
# c=a+b
# print(c)
# print(2+20)

# l=[1,2,3,4,5]
# a=2
# print(l[0])
# print(l[1])



# # 0(n) The length of the list is n numbers 
# ,so it is o(n)

# l=[1,2,3,4,5]
# for i in l:
#     print(i)
# print(l)

# Best case  (It shows at fist itself)
# Average case   (It shows at middle)
# wrost case    (it shows at last)

# l=[1,2,3,4,5,]
# for i in l:
#     if i==2:
#         print("True")
#         break


# 0(logN) 


# 0(NlogN)  Merge sort



# 0(n^2)

# l=[1,2,3,4,5]
# for i in l:
#     for j in l:
#         print(i,j)
    






##variable 

# print ("hello world")    # print()- inbulit function
# name="kavin22012004"     # name= variable (we can store the values)  # string ("set of character")-command 
# print("Hi" + name)
# name="john" 
# print ("hi",name )
# price=45
# amount=34.5             #float value
# child = False           #booleam
# print(child)
# print(price)


###string handling

# code="python learning"
# work="'string'"
# name="in github"
# print(work)    
 
# # print(code.upper())         # fully captial letter 
# print(code.lower())         #fully small letter
# print(code.capitalize())    #first letter capital
# print(code.title())         #first letter and space after the letter is capital
# print(code +" " + name + work)   #connecting the words or numbers
# print(code+" "+name)        #space of the words
# print("python \nlearning")    #this will print in next line
# print("python \t learning") #giving the the double space of the words
# print(code.isupper())        #if all the letter is upper(true)
# print(code.islower())        #if all the letter is lower ()
# print(len(code))             #finding the index of the word
# print(code.find("n"))        #finding the letter (n)
# print(code.count("n"))      #counting the letter (n)
# print(code.replace("a","s")) #replacing the words
# print(code.isalpha())        #finding all the the letter is alpha letter
# print(code.isdigit())
# print(code*5 )              


# ## multiple assignment in single line

# name,age ,weight="kavin",19,52    #types of variable in one line
# print(weight)
# like=dislike=65
# print(dislike) 
# print(like/dislike)
# print(like*dislike)


###Type casting

#otp=3252363
#otp=str(otp)     #type casting
#print("Your otp is" + str(otp))
#print(type(otp))
#count,number=199,"199"
#print(count+1)
# #count="199"
# print(number+"1")

##Assignment 1
# name="Anand"
# leave="15 days"
# year=2021
# print(name,leave,year)

###Assignment 1               #This is correct method
###Dear Anand,
###You have 15 days of Leave Balance for this
###Year(2021)
# name, leave, year ="Anand",15,2021
# print("Dear " + name + ",\nYou have " + str(leave) + " days of Leave Balance for this\nYear("+ str(year)+")")

# name, leave, year ="Anand",15,2021      #### this code is space error beacuse of (,) this  kama
# print("Dear " , name , ",\nYou have " , str(leave) , " days of Leave Balance for this\nYear(", str(year),")")


### Getting the input from the user

# name=input(" Enter your name:")
# print("Hello"+ name)
# height=float(input("Enter the height:"))
# print(type(height))
# height="{:.4f}".format(height/2.54)     ##{} this is for after the float value, 2 digit {:.2},4 digit {:.4}
# print("Your height is "+ str(height) + "cm")
# #print("Your are " + str(height/2.54) + "inches")
# print("Your are " + height + " inches tall")


###Assignment 2
 
# ## Get user input
# ## Name,Email ID and phone number.print the information like this
# ##  ****************************
# ##  UserName: XXXXX
# ##  Email   : XXXXX
# ##  ph      : XXXXX
# ##  ***************************

# Name=input("Enter the name : ")
# Email=input("Enter the email id :")
# Phoneno=input("Enter the Phone Number :")
 
# print("*****************************")

# print("UserName:",Name)
# print("Email :",Email)
# print("Ph :",Phoneno)

# print("*****************************")


# ## This is another type of code 
# ## Assignment 2

# Name=input("Enter the name : ")
# Email=input("Enter the email id :")
# Phoneno=input("Enter the Phone Number :")

# print("*****************************")

# print("UserName :" + Name + "\n   Email :" + Email + "\n      Ph :" + Phoneno )

# print("*****************************")


### Math operation

# a=20
# b=10
# print(a+b , a-b , a*b , a/b , a/50 , b/30 , (a+b)*40 , a+b*30)      ##give output in float (/) division
# print(10/2 , 20*3)
# a=23.5
# print(round(a))      # round is the absolute correct answer
# a=-5
# print(abs(a))        # ABS is the absolute value of a
# a=5
# print(abs(a))
# print(pow(a,4))      # pow is the power of a
# print(a**4)          # this is another mothod of power term
 
# a=55
# b=32
# print(max(a,b))       # maximum value of a,b
# print(min(a,b))       # minimum value of a,b
 
# import math  # math module
# a=45.6
# print(math.ceil(a))    # ceil is the decimal value of a=5
# print(math.floor(a))   # floor is the decimal value of a=4
# print(math.factorial(9))   # factorial of 9
# a=6
# print(a%2)       # it will find the remainder
# print(a%5)
# print(a%9)

### Assignment 3

## Get user input 
## Get the number n fron user.compute and print the follwoing values
## 1.log2(n)
## 2.cos(n)
## 3.e**n
                        
# # print(math.log2(16))
# # print(math.cos(16))
# # print(math.e**16)
# m=input("User input :")
# n=int(m)
# print("1.",int(math.log2(n)), "2.",int(math.cos(n)),"3.",int(math.e**n))


 ### If Else (true/False)conditional 
 
# pwd_correct= True
# if pwd_correct:        #conditional statement
#     print("logged in")
# else:
#     print("incorrect pwd")

## Relational operator

# num=35
# if num<30:            # < lower number           #  == is it equal
#     print("true")     # > higher number          #  != is it not equal
# else:                 # <= same number or lower number
#      print("false")   # >= same number or higher number 

# num=14
# if num%5==0:       # it is divisible by 5 means ,print true
#     print("Multiple of 10")
# else:
#     print("Not multiple of 10")

##Elif ladder

# ind_score=150
# if ind_score>=150:
#     print("india won")
# elif ind_score>=100:
#     print("pak win")
# elif ind_score>=90:
#     print("Aus win")
# else:
#     print("jap win ")

## Nested if
 
# #check if the number is three digit number                      # A     B    And       OR     NOT
# #logical operation -and (or) or      # this method is 'and'
#                                                                  T     T     T        T       0 = 1
# num= int(input("Enter the number :"))                          # T     F     F        T       1 = 0
# if num>99 and num<1000 :                                       # F     T     F        T
#     if num%2==0:                                               # F     F     F        F
#         print(str(num),"is the three digit number")
# else:
#     print(str(num) ,"is not a three digit number")  

##This method is OR
# name="kavin"
# if name[0]=="k" or name[0]=="K":
#     print("the name starts with s")


###Bitwise operator
## And , OR , Not , Exor , Leftshift , Rightshift
#  left shift                                                 # Exor
#  00001100 12<<1    it will leave the first no                  # a^b
#  00011000 =24                                                  #  0 0 =0
# Right shift                                                    #  1 0 =1
# 00001100   12>>1                                               #  0 1 =1
# 00000110 = 6                                                   #  1 1 =0


###String slicing

# name="kangani patti"
# print(name[9])              #this will print the index value
# print(name[0:7])
# print(name[2:11])
# print(name[1:12:2])       # this will print one after another value
# print(name[-4])          # this will print in back side
# print(name[::-1])
# print(name[2:-2])
# x=slice(2,-2)
# print(name[x])

####Assignment 4
#str="Happy"
# H                 y
# Ha                py
# Hap               ppy
# Happ              appy
# Happy             Happy

# print("H          "+"y")
# print("Ha         "+"py")
# print("Hap        "+"ppy")
# print("Happ       "+"appy")
# print("Happy      "+"Happy")
# str="Happy"
# print(str[0])
# print(str[:2])
# print(str[:3])
# print(str[:4])
# print(str[:5])
# print(str[-1])
# print(str[-2:])
# print(str[-3:])
# print(str[-4:])
# print(str[-5:])


###List

# cities=["chennai","madurai","thricy" ,"coimbatore","salem"  ]
# val=[1,5,8,5,4,7]
# list=["salem",3 ,"namakkal"]
# print(list[2])
# print(val[4])
# print(cities[3])
# print(cities[:4])
# print(val[-4])
# print(cities)
# cities[2]="Thrichy"         # this will change the letter
# print(cities)      
# cities.append("sivakasi")    #inserting the element in last
# print(cities)
# cities.insert(2,"karur")     # inserting the element inside the place
# print(cities)
# delete=cities.pop()         # this will delete the last element and also say which element is deleted
# print(delete,"has been deleted")
# print(cities)
# del cities[2]             #this will delete the element
# print(cities)
# cities.remove("salem")   # we are giving the place to delete
# print(cities)
# print(sorted(cities))    # this will print in accending order
# print(sorted(val))
# cities.sort()         # this is also sorting  
# print(cities)
# cities.reverse()
# print(cities)       #  we can find how many value in list 
# print(len(cities))


###While Loop

# letter=' '
# while letter.isalpha():
#  letter= input("enter the alphabet:")
# print("You have entered "+letter)

##To print 1 t0 100
# num=0
# while num<=99:
#   num+=1
#   print(num,end=',')


### For loop

# for i in range (1,100):
#     print(i,end=',')

# list=[22,456,34234,566,345]
# for i in list:
#     print(i*i)

# string=(2,35,"kavin",34,556)
# for i in string:
#     print(i)


### simple Game
### I am chossing the number below 10
### reandomly I am chosing any number
### its correct it will print
### its wrong try again

# import random
# n=input("enter the limit:")
# num=random. randint(1,10)
# guess=int(input("can u guess the no I am thinking "))
# while num!=guess :
#     if len(guess)==0:
#         print("list is full")
#     if guess>num:                                                              ### dout
#         print("your guess is higher")
#     else:
#         print("your guess is lower")
#         guess=int(input("try again :"))
# print("you won") 


### Assignment 

##1.Get input number n from user. print all the factor of n
##2. Get a list of to do task from the user and add it to a to_do list.print the list
##3.Given an array of intrgers.find a peak element in it .An array element is the peak if it is NOT samller than its neighbours.
## For corner element ,we need to consider only one neighbour.  Eg in..[3,4,6,7,5] -7 is a peak element.
##4.List=[3,4,5,-2,-1,2,8,0,-4].Move all negative number to the end of list.





