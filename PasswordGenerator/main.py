# Password Generator Project
import random

# lists of all possible letters, numbers, and special characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# list to hold the characters selected
password_list = []

# grabs a number of random characters from each list based on user input then adds them to the password_list
for letter in range(nr_letters):
  password_list += random.choice(letters)

for symbol in range(nr_symbols):
  password_list += random.choice(symbols)

for number in range(nr_numbers):
  password_list += random.choice(numbers)

#randomizes the password_list
random.shuffle(password_list)

# create password variable as empty string
password = ""
# add each character from password_list to the password variable
for char in password_list:
  password += char

print(password)
