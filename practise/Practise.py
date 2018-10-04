import random

#
# //Task 1
#
# print("Enter your Name ..")
# name = input()
#
# print("Enter your Age..")
# age = input()
#
#
# age = int(age)+100
#
# print(name, ", After hundred years you will be ", age, "years old")
#
#
#  //Task 2
# print("How many times you want to print it ?? ")
# print("Enter a Number")
# number = int(input())
# even_odd = number % 2
# multiple4 = number % 4
# if even_odd == 0:
#     print("The number is even")
#
# else:
#     print("the number is odd")
#
# if multiple4 == 0:
#     print("The number is divided by 4")

# // Task 3
#
# print("enter a number ....")
# limit = int(input())
# List_a = [1, 4, 5, 6, 7, 12, 21, 34, 55, 89]
# List_b = []
#
# for x in List_a:
#     if x <= limit:
#         print(x)
#         List_b.append(x)
#
#
# print(List_b)

# ///// Task 4


# print("Please enter a number")
# number = int(input())
# divisor = []
#
#
# for x in range(2, number):
#     if number % x == 0:
#         divisor.append(x)
#
# print(divisor)
#
#
#
# /// Task 5


# List_1 = [1, 2, 3, 4, 7, 8, 10, 14, 14]
# List_2 = [2, 3, 5, 6, 7, 8, 10, 11, 12, 14]
# List_3 = []
#
#
# for state in List_1:
#     if state in List_2:
#         List_3.append(state)
#
# print(List_3)


#
#
#
#  /// Task 6
# name = "HannaH"
# new_name = list(name)
#
# length = len(name)
# print(length)
# reverse_name = []
#
#
# for i in new_name[length+1::-1]:
#     reverse_name.append(i)
# print(reverse_name)
#
#
# if new_name == reverse_name:
#     print("the word is palindrome")
# else:
#     print("the Word is not ")

#
# //Task 8
# while True:
#
#     Player_1 = input("Enter Player 1 input (rock/paper/scissor): ")
#     Player_2 = input("Enter Player 2 input (rock/paper/scissor): ")
#
#     if Player_1 == "rock" and Player_2 == "paper":
#         print("player 2 is win")
#     elif Player_1 == "paper" and Player_2 == "scissor":
#         print("Player 2 is win")
#     elif Player_1 == "scissor" and Player_2 == "rock":
#         print("Player 2 wins")
#     else:
#         print("Player 1 wins")
#
#     restart = input("Wants play again (yes/No)")
#     if restart == "yes":
#         continue
#     else:
#         break

# // Task 9

# count = 0
# while True:
#
#     print("Generating a random number....")
#
#     number = random.randint(1, 9)
#     print(number)
#
#     print("Random number generated. Please guess the number in between 1 to 9!")
#
#     guess_number = int(input("Enter your Number.."))
#
#     if number == guess_number:
#         print("Congratulation!! You have guessed it right.")
#
#     elif guess_number > number:
#         greater = guess_number - number
#         print("You were close just " + str(greater) + " ahead")
#
#     else:
#         lower = number-guess_number
#         print("You were close just " + str(lower) + " short")
#
#     print("Do you want to exit ??(yes/no)")
#     ending = input()
#     count = count + 1
#
#     if ending == "yes":
#         print("you have tried " + str(count) + " times")
#         break
#     else:
#         continue

# // Task 10

# a = random.sample(range(20), 6)
# b = random.sample(range(30), 8)
#
# print(a)
# print(b)
#
#
# new_list = [x and y for x in a for y in b if x == y]
# print(new_list)
#


# // Task11

# def get_integer(help_text):
#     return int(input(help_text))
#
#
# def check_prime(number_input):
#
#     for i in range(2, number_input):
#         if number_input % i == 0:
#             return False
#
#     return True
#
#
# number = get_integer("Enter a number")
# if check_prime(number):
#     print("The number is prime")
# else:
#     print("The number is not prime")


# // Task 12
# print(new_list.append(given_list[0], given_list[size_1ist]))

# def get_input(text):
#     return int(input(text))
#
#
# def new_list_make(given_list, new_list):
#     size_1ist = len(given_list)
#     new_list.append(given_list[0])
#     new_list.append(given_list[size_1ist-1])
#     print(new_list)
#
#
# a = [5, 10, 15, 20, 25]
# b = []
#
# new_list_make(a, b)

# // Task 13

# def fibo(numb):
#     if numb == 0:
#         print("None")
#     elif numb == 1:
#         print(0)
#     else:
#         n1 = 0
#         print(n1)
#         n2 = 1
#         print(n2)
#         for a in range(0, numb-2):
#             n3 = n1+n2
#             n1 = n2
#             n2 = n3
#             print(n3)
#
#
# in_num = int(input("How many fibonacci number you want to print"))
#
# fibo(in_num)

# //Task 14

# def list_input():
#     length = int(input("How many number do you want to input"))
#     new_list = list()
#     while length > 0:
#         i = int(input())
#         .new_listappend(i)
#         length -= 1
#
#     return new_list


# def find_duplicate(main_list):
#     main_list = set(main_list)
#     main_list = list(main_list)
#
#     print(main_list)
#
#
# # print("Make a list")
# # my_list = list_input()
#
# my_list = [1, 1, 2, 5, 6, 6, 9, 10, 10, 11]
# find_duplicate(my_list)

# //Task 15


# def split(text):
#     new_text = text.split()
#     return new_text
#
#
# def reverse(text):
#     lenght = len(text)
#     finish_word = []
#     for i in text[lenght + 1::-1]:
#         finish_word.append(i)
#     return finish_word
#
#
# word = "This is my story"
# alada_word = split(word)
# last_answer = []
# last_answer = reverse(alada_word)
# print(last_answer)

# Task 16






