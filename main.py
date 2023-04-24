import random

# def computegrade(score):
#     try:
#         score = float(score)
#         if score >= 0.9:
#             grade = "A"
#         elif score >= 0.8:
#             grade = "B"
#         elif score >= 0.7:
#             grade = "C"
#         elif score >= 0.6:
#             grade = "D"
#         elif score >= 0:
#             grade = "F"
#         else:
#             grade = "Invalid input. Score cannot be negative."
#     except:
#         grade = "Invalid input. Please enter a valid score."
#     return grade
#
#
# score = input("Enter a score between 0.0 and 1.0: ")
# print("Grade: ", computegrade(score))


# def greet_feeling_timeofday(timeofday):
#     greetings = ['Good morning!', 'Good afternoon!', 'Good evening!']
#     greeting = random.choice(greetings)
#     print(greeting)
#     print('How are you feeling?')
#     feeling = input()
#     print('I am happy to hear that you are feeling ' + feeling + '.')
#     if timeofday == 'morning' and greeting == 'Good morning!':
#         return
#     greet_feeling_timeofday(timeofday)
#
# greet_feeling_timeofday('afternoon')


# count = 0
# total = 0
#
# while True:
#     try:
#         user_input = input("Enter a number (or 'done' to exit): ")
#         if user_input == 'done':
#             break
#         number = float(user_input)
#         count += 1
#         total += number
#     except ValueError:
#         print('Invalid input. Please enter a number or "done".')
#
# if count == 0:
#     print('No numbers were entered.')
# else:
#     average = total / count
#     print('Total:', total)
#     print('Count:', count)
#     print('Average:', average)

# string = "Write a program that takes a string"
#
#
# def program(words):
#     for i in words.split():
#         print(i)
#
#
# program(string)


# How to connect to a FTP server
# from ftplib import FTP
# #Define credentials
#
#
# FTP_USER = "u736684440"
# FTP_PASS = "Fumaporro.123"
# ftp = FTP("zegeteam.com")
# print(ftp.login(FTP_USER, FTP_PASS))
# print(ftp.dir())
# print(ftp.retrlines('LIST'))
# #Connect to FTP server

# Python3 code to find largest prime
# factor of number

# def is_palindrome(num):
#     num_str = str(num)
#     return num_str == num_str[::-1]
#
#
# largest_palindrome = 0
#
# # Loop through all 4-digit numbers
# for i in range(1000, 1000000):
#     # Check if the number is a palindrome
#     if is_palindrome(i):
#         # If it is, update the largest palindrome if necessary
#         if i > largest_palindrome:
#             largest_palindrome = i
#
# print(largest_palindrome)

# def get_triangle_number_with_n_divisors(n_divisors):
#     i = 1
#     while True:
#         triangle_number = i * (i+1) // 2
#         factors = get_factors(triangle_number)
#         if len(factors) > n_divisors:
#             return triangle_number
#         i += 1
#
# def get_factors(n):
#     factors = []
#     i = 1
#     while i*i <= n:
#         if n % i == 0:
#             factors.append(i)
#             if i != n // i:
#                 factors.append(n // i)
#         i += 1
#     return factors
#
# print(get_triangle_number_with_n_divisors(500))
#
#


fhandle = open("/Class 3/mbox-short.txt")
print(fhandle.readline())
fhandle.close()