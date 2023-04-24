# str1 = 'Welcome'
#
# rev_upper = lambda string: string.upper()[::-1]
# print(rev_upper(str1))
#
# LIST COMPREHENSION WITH LAMBDA
# is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
#

# IF STATEMENT WITH LAMBDA
# Max = lambda a, b: a if (a > b) else b
#
# print(Max(1, 2))

# no need for a for loop to iterate
# li = [5, 6, 7, 8, 9, 10]
# final = list(filter(lambda x: (x % 2 == 0), li))
# print(final)

# if lambdas dont have, a num doesnt raise an error
# ages = [5, 2] #here it doesnt return shit
# ages = [13, 90, 18, 59, 21, 60, 5] #returns all above 18
# adults = list(filter(lambda age: age > 18, ages))
# print(adults)

# MAP returns every iteration, filter only return what fits the criteria
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final = list(map(lambda x: x * 2, li))
# print(final)

# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda  x, y: x * y), li)
# print(sum)

"""1. Write a lambda function that takes two lists of integers and returns a new list with the maximum value for each
index of the two lists. For example, given 1. Write a lambda function that takes two lists of integers and returns a
new list with the maximum value for each index of the two lists. For example, given [1, 3, 5] and [2, 4, 6],
the function should return [2, 4, 6]. and [2, 4, 6], the function should return [2, 4, 6]. """
import random

# l1 = [1, 3, 5]
# l2 = [2, 4, 6]
#
# result = lambda a, b: a if (a > b) else b
#
# print(result)
#
# max_list = lambda list1, list2: [max(x, y) for x, y in zip(list1, list2)]

#
# list1 = [1, 3, 5]
# list2 = [2, 4, 6]
#
# max_list = lambda list1, list2: [max(list1[i], list2[i]) for i in range(len(list1))]
#
# print(max_list(list1, list2))

"""2. Write a lambda function that takes a string of words separated by spaces, and returns a new string with the 
words in reverse order. For example, given the string "the quick brown fox", the function should return "fox brown 
quick the". """

#
# prompt = "the quick brown fox"

# str1 = lambda prompt: prompt for i in prompt i[::-1]
# sentence = "the quick brown fox"
#
# reverse_words = lambda sentence: ' '.join(sentence.split()[::-1])
# print(reverse_words(sentence))


# 333333333333333
# word = "racecar for race to race your ass"
# is_palindrome = lambda s: s == s[::-1]
#
# print(is_palindrome(word))
# def gen_func():
#     yield 1
#     yield 2
#     yield 3
#
#
# x = gen_func()
#
# print(next(x))
# print(next(x))
# print(next(x))

# def fib(limit):
#     a, b = 0, 1
#
#     while a < limit:
#         yield a
#         a, b = b, a + b
#
# x = fib(5)
#
# print(x)

"""Write a generator function that takes a list of numbers as input and yields 
only the even numbers."""

# def func(a):
#     for i in a:
#         if i % 2 == 0:
#             yield i
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = func(numbers)
#
# for num in even_nums:
#     print(num)
# vow = "aeiou"
#
#
# def string_gen(phrase):
#     lista = phrase.split
#     for i in lista:
#         for u in vow:
#             if i.startswith(u):
#                 yield i
#
# test_list = ["all", "love", "and", "get", "educated", "by", "gfg"]
# complete = string_gen(test_list)
#
# for i in complete:
#     print(i)

# def vowel_words(text):
#     vowels = {'a', 'e', 'i', 'o', 'u'}
#     for word in text.split():
#         if word[0].lower() in vowels:
#             yield word
#
#
# text = "The quick brown fox jumps over the lazy dog"
# vowel_words_gen = vowel_words(text)
#
# for word in vowel_words_gen:
#     print(word)

# over_18 = lambda people: [person['name'] for person in people if person['age'] > 18]
#
# people = [{'name': 'Alice', 'age': 25},
#           {'name': 'Bob', 'age': 17},
#           {'name': 'Charlie', 'age': 30},
#           {'name': 'David', 'age': 12}]
#
#
# print(over_18(people))

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


my_rect = Rectangle(10, 5)
print(str(my_rect))
print(repr(my_rect))
