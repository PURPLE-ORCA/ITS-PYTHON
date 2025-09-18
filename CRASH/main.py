# print("hello world")


# full_name = 'purple orca'
# age = 19

# print(f"Hello {full_name}") 
# print(f"You are {age} years old")


# #INPUTS
# name = input('Enter your name: ')
# print(name)


#IF STATEMENTS
# age = int(input('Enter your age: '))
# is_human = False
# price = 0

# if age >= 18:
#     print('You are an adult')
#     price += 10
#     print(f'your price is :{price}')
# elif age < 0:
#     print('You are not born yet')
#     print(f"your price is : {price}")
# else:
#     print('You are a minor')
#     price += 999
#     print(f"your price is ;{price}")

# if is_human:
#     print('You are a human')
# else:
#     print('You are not a human')


#CONDITIONAL EXPRESSION
# num = -1  
# print('positive' if num > 0 else 'negative')
# age = 19
# print('adult' if age >= 18 else 'minorrrrr')

#Logical Operators = evaluate multiple conditions (or, and , not)
                    # or = at least one condition is True
                    # and = both conditions must be True
                    # not = inverts the condition (not False, not True)

# while loop = used to repeat a block of code as long as a condition remains 'True'
                        # we re-check the condition at the end of the 


# FOR LOOP
# for i in range(1, 13):
#     print(i)

# for i in range(1, 13 ,2):
#     print(i)

# name = "purple orca"
# for letter in name:
#     print(letter)

# for letter in name:
#     print(letter, end="&")

# import time
# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)
# print('Happy New Year!')



#LIST[] = mutable, most flexible
# Tuple () = immutable, faster
# Set {} = mutable (add/remove), unordered, NO duplicates, best for membership



#STRING METHODS
# print(help(str))


#SHOPPING CART PROGRAM
# waifus = []
# heads = []
# total = 0

# while True:
#     waifu = input('Enter waifu (Press q to quite):')
#     if waifu.lower() == 'q':
#         break
#     else :
#         price = float(input('Enter head :'))
#         waifus.append(waifu)
#         heads.append(heads)
#         total += price

# print(f"Your cart contains : {waifus}")
# print(f"Your total is : {total}")


#2D DIMENTIONAL LISTS
# num_pad = ((1,2,3),(4,5,6),(7,8,9),('*',0,'#'))

# for row in num_pad:
#     for num in row:
#         print(num, end=' ')
#     print()


#DICTIONARIES
# capitals = {
#     'USA': 'Washington DC',
#     'UK': 'London',
#     'Germany': 'Berlin'
# }
# print(dir(capitals))
# print(help(capitals))


# import random

# number = random.randint(1,4000)
# random.choice(options)

# number = random.randint(1, 5)
# guesses = 0
# while True:
#     guess = int(input("Enter your guess:"))
#     if guess == number:
#         print(f"{guess} is correct, you win!")
#         guesses += 1
#         print(f"You made {guesses} guesses")
#         break
#     else:
#         print(f"{guess} is incorrect, Try again")



#MESSAGE ENCTYPTION PROGRAM
# import random
# import string

# chars = " " +  string.punctuation + string.ascii_letters + string.digits
# chars = list(chars)
# key = chars.copy()

# random.shuffle(key)

# message = input('Enter your message:')
# ciphermsg = ''

# for letter in message:
#     index = chars.index(letter)
#     ciphermsg += key[index]

# print(f"Your original message is :{message}")
# print(f"Your encrypted message is :{ciphermsg}")


#FUNCTOINS
# def display_bill(name, mounth, amount, due_date):
#     print(f"Hello {name}")
#     print(f"Your bill for {mounth} is availiable with the price of {amount}DH, the last day to pay is {due_date}")

# display_bill('purple orca', 'January', 100, '31/01/2021')

# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# full_name = create_name('purple', 'orca')   
# print(full_name) 

# def hello(greeeting, title, first, last):
#     print(f"{greeeting} {title}, {first}, {last}")

# hello(greeeting='Hello',title='Mr',last='orca', first='purple')

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# print(add(1,2,3))


#MEMBERSHIP OPERATORS used to test wheteher a value or variable is found in a sequence 
                                                        #1 in 
                                                        #2 not in
# tech_stack = ['python', 'java', 'c++', 'c#', 'ruby']

# tech = input('Enter a tech name:')
# if tech in tech_stack:
#     print(f"{tech} is in the stack")
# else:
#     print(f"{tech} is not in the stack")


# #MODULES
# print(help("module")) 

# import math
# import math as m
# from math import e 
 

#BANKING SYSTEM
# sum_even_digits = 0
# sum_odd_number = 0
# total = 0

# card_number = input("Enter your card number:")
# card_number = card_number.replace("-", "")
# card_number = card_number.replace(" ", "")
# card_number = card_number[::-1]

# for x in card_number[::2]:
#     sum_odd_number += int(x)

# for x in card_number[1::2]:
#     x = int(x) * 2
#     if x >= 10:
#         sum_even_digits += (1 + (x % 10))
#     else:
#         sum_even_digits += x

# total = sum_even_digits + sum_odd_number

# if total % 10 == 0:
#     print("VALID")
# else:
#     print("INVALID")

# def main():
#     def show_balance(balance):
#         print(f"Your balance is : ${balance:.2f}")
#     def deposite():
#         amount = float(input("Enter the amount to deposite:"))

#         if amount < 0:
#             print("That's not a valid amount")
#             return 0
#         else:
#             return amount
#     def withraw(balance):
#         amount = float(input("Enter the amount to withdraw :"))

#         if amount > balance:
#             print("Insufficient funds")
#             return 0
#         elif amount < 0:
#             print("That's not a valid amount")
#             return 0
#         else:
#             return amount 
        

#     balance = 0
#     is_running = True

#     while is_running:
#         print("1. Show balance")
#         print("2. Deposite")
#         print("3. Withraw")
#         print("4. Exit")

#         choice = input("Enter your choice:")
#         if choice == '1':
#             show_balance(balance)
#         elif choice == '2':
#             balance += deposite()
#         elif choice == '3':
#             balance -= withraw(balance)
#         elif choice == '4':
#             is_running = False
#         else:
#             print("Invalid choice") 
# main()



#CALCULATE EXECCUTION TIME
# import time
# start_time = time.perf_counter()

# for i in range (100000000):
#     pass

# end_time = time.perf_counter()

# elapsed_time = end_time - start_time
# print(f"Execution time: {elapsed_time:.1f} seconds")



# import datetime

# date = datetime.date(2025, 1, 2)
# today = datetime.date.today()

# time = datetime.time(12, 30, 0)
# now = datetime.datetime.now()

# now = now.strftime("%H:%M:%S %m-%d-%Y")

# target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
# current_datetime = datetime.datetime.now()

# if target_datetime < current_datetime:
#     print("Target date has passed")
# else:
#     print("Target date has NOT passed")



# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                               Good for I/O bound tasks like reading files or fetching data from APIs

# import threading
# import time

# def walk_dog(first, last):
#    time.sleep(8)
#    print(f"You finish walking {first} {last}")

# def take_out_trash():
#    time.sleep(2)
#    print("You take out the trash")

# def get_mail():
#    time.sleep(4)
#    print("You get the mail")

# chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
# chore1.start()

# chore2 = threading.Thread(target=take_out_trash)
# chore2.start()

# chore3 = threading.Thread(target=get_mail)
# chore3.start()

# # .join() ensures that all tasks are completed before proceeding
# chore1.join()
# chore2.join()
# chore3.join()

# print("All chores are complete!")


# FETCHING DATA WITH API's
# import requests

# base_url = "https://pokeapi.co/api/v2/"

# def get_pokemon_info(name):
#     url = f"{base_url}/pokemon/{name}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         pokemon_data = response.json()
#         return pokemon_data
#     else:
#         print(f"Failed to retrieve data {response.status_code}")

# pokemon_name = "drowzee"
# pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info:
#     print(f"Name: {pokemon_info["name"].capitalize()}")
#     print(f"Id: {pokemon_info["id"]}")
#     print(f"Height: {pokemon_info["height"]}")
#     print(f"Weight: {pokemon_info["weight"]}")