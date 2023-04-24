# class Dog:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age
#
#     def bark(self):
#         print(r"""
#                 __      _
#         \.'---.//|
#          |\./|  \/
#         _|.|.|_  \
#        /(  ) ' '  \
#       |  \/   . |  \
# jrjc   \_/\__/| |
#         V  /V / |
#           /__/ /
#           \___/\"""")
#
#     def info(self):
#         print(f"Name of the dog: {self.name}\n Breed: {self.breed}\n Age: {self.age}")
#
#
# d1 = Dog("Rocky", "Rotweiler", 4)
# d1.bark()
#
#
#
# """1. Create a Dog class with the following attributes: name, breed, and age.
# The class should also have the following methods: bark() and info()."""


# class Person:
#
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#
#
# class BankAccount(Person):
#     def __init__(self, name, lastname, account_number, balance=0):
#         super().__init__(name, lastname)
#         self.account_number = account_number
#         self.balance = balance
#
#     def __str__(self):
#         return f"Client: {self.name} {self.lastname}\nAcoount Balance {self.account_number}: ${self.balance}"
#
#     def depositar(self, deposit):
#         self.balance += deposit
#         print("Deposito aceptado")
#
#     def withdraw(self, withdraw):
#         if self.balance >= withdraw:
#             self.balance -= withdraw
#             print("Withdraw succesful")
#         else:
#             print("Insufficient funds")
#
#
# def crear_cliente():
#     nombre_cl = input("Please, write your name: ")
#     apellido_cl = input("Please, write your last name: ")
#     numero_cuenta = input("Type your account number: ")
#     client = BankAccount(nombre_cl, apellido_cl, numero_cuenta)
#     return client
#
#
# def Initiate():
#     my_client = crear_cliente()
#     print(my_client)
#     option = 0
#
#     while option != 'E':
#         print('Choose: Deposit (D), Withdraw (W), or Exit (E)')
#         option = input()
#
#         if option == 'D':
#             monto_dep = int(input("Deposit Amount: "))
#             my_client.depositar(monto_dep)
#         elif option == 'W':
#             monto_ret = int(input("Withdrawn Amount: "))
#             my_client.withdraw(monto_ret)
#         print(my_client)
#
#     print("Thanks to operate with Brainnest Bank")
#
#
# Initiate()

# matrix = [[j for j in range(3)] for i in range(3)]
# print(matrix)
#
# mat = []
# for i in range(3):
#     for j in range(3):
#         mat.append(j)
# print(mat)
# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# flattened_list = [item for sublist in nested_list for item in sublist]
# print(flattened_list)

"""2. Write a list comprehension to generate a list of all possible pairs of numbers from two given lists."""

# list1 = [1, 2]
# list2 = [3, 4]
# # Output: [(1, 3), (1, 4), (2, 3), (2, 4)]
#
# res = []
# for i in list1:
#     for j in list2:
#         res.append((i,j))
# print(res)
#
# result = [(i,j) for i in list1 for j in list2]
# print(result)

# list1 = [1, 2]
# list2 = [3, 4]
# result = [(i,j) for i in list1 for j in list2]
# print(result)

"""3. Write a list comprehension to find all the prime numbers between 1 and 100."""
primes_1 = []
for val in range(2, 101):
    if val > 1:
        for i in range(2, val):
            if (val % i) == 0:
                break
        else:
            primes_1.append(val)


primes = [ val for val in range(2, 101) if val > 1 for i in range (2, val) if (val % 1) == 0 break]

primes_1 = [val for val in range(2, 101) if all(val % i != 0 for i in range(2, val))]
