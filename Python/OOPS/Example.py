# with open('number.txt','r') as file:
#     data= file.readline()

# print(data)
# # mylist=[1,2,3,4,56,7,8,9]
# mylist= data.split(',')
# mylist.append(10)
# print(mylist)
# mylist.insert(2,22)
# print(mylist)
# print(mylist.pop(1))
# # mylist.remove(2)
# # del mylist[1]
# print(mylist)
# mylist1=[33,44,67,89,89]

# mylist.extend(mylist1)
# print(mylist)

# print(mylist.index('7'))
# mylist.sort()
# print(mylist)





# D={"id":123,"name":'kavin',"gender":'male'}
# keys=D.keys()
# print(keys)
# print("**********")
# D.clear()
# print(D)
# print("**********")
# items=D.items()
# print(items)
# print("**********")





        
     

           
        # Python program to print the Fibonacci sequence

# # function to generate Fibonacci sequence
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# # user input for number of terms
# nterms = int(input("Enter the number of terms: "))

# # check if the number of terms is valid
# if nterms <= 0:
#     print("Please enter a positive integer")
# else:
#     print("Fibonacci sequence:")
#     for i in range(nterms):
#         print(fibonacci(i))




# # Armstrong number in python

# num = int(input("Enter a number: "))
 
# # determine the number of digits
# num_digits = len(str(num))
 
# # initialize the sum variable
# sum = 0
 
# # find the sum of the digits raised to the power of num_digits
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** num_digits
#    temp //= 10
 
# # check if the number is an Armstrong number
# if num == sum:
#    print(num, "is an Armstrong number")
# else:
#    print(num, "is not an Armstrong number")



# # leap year

# year = int(input("Enter a year: "))

# if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")





    
    # palindrome

# def palindrome(a):
#     str=a[::-1]
#     return str==a

# text=input("enter the element:")
# Ans=palindrome(text)

# if Ans==True:
#     print(text,"is palindrome")
    
# else:
#     print(text,"is not a palindrome")



# # prime number

# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")




def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted strings are equal
    return sorted(str1) == sorted(str2)

# Example usage
string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams!")
else:
    print(f"{string1} and {string2} are not anagrams.")













# ex={"item":"cholate","s":"kavin"}
# print(ex['item'])



# import time


# green_duration = 5
# yellow_duration = 2
# red_duration = 5


# state = "green"

# while True:
#     if state == "green":
#         print("GO")
#         time.sleep(green_duration)
#         state = "yellow"
#     elif state == "yellow":
#         print("SLOW DOWN")
#         time.sleep(yellow_duration)
#         state = "red"
#     elif state == "red":
#         print("STOP")
#         time.sleep(red_duration)
#         state = "green"







# # define the arithmetic operations as functions


# def add(x, y):
#     print(x + y)

# def subtract(x, y):
#     print(x - y)

# def multiply(x, y):
#     print(x * y)

# def divide(x, y):
#         if y==0:
#                 print(ValueError)
#                 return None
#         else:
#                 print(x/y)

    

# choice = input("Enter choice : ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# # perform the selected operation
# if choice == 'add':
#     result = add(num1, num2)
# elif choice == 'sub':
#     result = subtract(num1, num2)
# elif choice == 'multiple':
#     result = multiply(num1, num2)
# elif choice == 'divide':
#     result = divide(num1, num2)
# else:
#     print("Invalid input")




    
    
    
# # 3) Define a function CheckOddEven(num) that checks if the num is odd or
# # even; the function sets a flag accordingly and returns it. Use this function
# # to find the sum of even and odd numbers separately, from a
# # given input of N numbers.
    
    
# def CheckOddEven(num):
#     if (num%2==0):
#         flag="EVEN"
#     else :
#         flag="ODD"
#     return (flag)
# sum_even=0
# sum_odd=0
# N=int(input("Enter No. of Numbers : "))
# for i in range(1,N+1):
#     num=int(input("\nEnter Your Number : "))
#     flag=CheckOddEven(num)
#     if (flag=="EVEN"):
#         sum_even+= num
#         print ("\nNumber ",num,"is even ")
#     if (flag=="ODD"):
#         print ("\nNumber ",num,"is odd ")
#         sum_odd= num+sum_odd
# print("\nSum of Odd Numbers entered = ",sum_odd)
# print("Sum of Even Numbers entered = ",sum_even)





# def mark_grade(name,student_id):
#     mark1=int(input("Enter Subject-1 Marks (out of 100): "))
#     mark2=int(input("Enter Subject-2 Marks (out of 100): "))
#     mark3=int(input("Enter Subject-3 Marks (out of 100): "))
#     mark4=int(input("Enter Subject-4 Marks (out of 100): "))
#     mark5=int(input("Enter Subject-5 Marks (out of 100): "))
#     total=mark1+mark2+mark3+mark4+mark5
#     average=total/5
#     if(90<average<=100):
#         grade="O"
#     elif(80<average<=90):
#         grade="A"
#     elif(70<average<=80):
#         grade="B"
#     elif(60<average<=70):
#         grade="C"
#     elif(50<average<=60):
#         grade= "D"
#     elif(0<=average<=50):
#         grade= "F"
#     else:
#         print(" You have entered invalid marks... ")
#         grade=" INVALID "
#     print("\n\n")
#     print("\t****** MARK SHEET ****** ")
#     print("\n\tNAME : ",name)
#     print("\tSTUDENT ID : ",student_id)
#     print("\n\tSubject-1 Marks : ",mark1)
#     print("\tSubject-2 Marks : ",mark2)
#     print("\tSubject-3 Marks : ",mark3)
#     print("\tSubject-4 Marks : ",mark4)
#     print("\tSubject-5 Marks : ",mark5)
#     print("\n\tTotal Marks Scored : ",total)
#     print("\n\tAverage : ",average)
#     print("\n\tGrade : ",grade)

# N=int(input("Enter No. of Students : "))

# for i in range(1,N+1):
#     name=input("\nEnter Student Name : ")
#     student_id=input("Enter Student ID : ")
#     mark_grade(name,student_id)



# with open('number.txt','r') as file:
#     data= file.read()

# print(data)
# mylist=[1,2,3,4,56,7,8,9]

# mylist.append(10)
# print(mylist)
# mylist.insert(2,22)
# print(mylist)
# print(mylist.pop(1))
# # mylist.remove(2)
# # del mylist[1]
# print(mylist)
# mylist1=[33,44,67,89,89]

# mylist.extend(mylist1)
# print(mylist)

# print(mylist.index(7))
# mylist.sort()
# print(mylist)




# # 18

# A=('2',3,'-6','-7',-9,)
# b,c,d,r,e=A
# print(d)

# b=(1,2,3,4,-5,-6,-7)
# for i in b:
    
#     if i>0:
        
#         print(i)

  
        
# thistuple = ("apple", "banana", "cherry") 
# y=("orange",) 
# thistuple +=y
# print(thistuple)   
        
        
# thistuple = ("apple", "banana", "cherry")
# y=list(thistuple)
# # y.append("orange")
# y[1]=("orange")
# thistuple = tuple(y)
# print(thistuple)


# dict={"name":"kavin","age":12,"gender":"male"}

# dict.pop('name')
# print(dict)
# dict1={"name":"kavin","age":12,"gender":"male"}
# dict1.popitem()
# print(dict1)

# dict1={"name":"kavin","age":12,"gender":"male"}
# dict1.clear()
# print(dict1)



# mylist=[1,2,3,4,5]
# for i in mylist:
#     print(i,end=" ")
    
    
    
    
#     # get input string from user
# string = input("Enter a string: ")

# # define a list of vowels
# vowels = ['a', 'e', 'i', 'o', 'u']

# # initialize a variable to count the number of vowels
# count = 0

# # loop through each character in the string
# for char in string:
#     # check if the character is a vowel
#     if char.lower() in vowels:
#         # if it is, increment the vowel count
#         count += 1

# # print the number of vowels in the string
# print("The number of vowels in the string is:", count)




# prices = []  # create an empty list to store prices

# # read prices of 5 items from user input
# for i in range(5):
#     price = float(input(f"Enter price {i+1}: "))
#     prices.append(price)

# # calculate the sum, product, and average of the prices
# price_sum = sum(prices)
# price_product = 1  # set to 1 initially to allow multiplication
# for price in prices:
#     price_product *= price
# price_average = price_sum / len(prices)

# # display the sum, product, and average of the prices
# print(f"Sum of prices: {price_sum:.2f}")
# print(f"Product of prices: {price_product:.2f}")
# print(f"Average price: {price_average:.2f}")




# L=['abs','Abb','ab','bbb']
# for i in L:
#     if i.endswith('b') and len(i)>2:
#         print(i)



# my_tuple = ("Hello", "world", "how", "are", "you")

# reversed_tuple = tuple([s[::-1] for s in my_tuple])
# print(reversed_tuple)
