#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letter = random.choice(letters)
random_symbol = random.choice(symbols)
random_number = random.choice(numbers)

if nr_letters > len(letters):
    print("Too many letters!")
if nr_symbols > len(symbols):
    print("Too many numbers!")
if nr_numbers > len(numbers):
    print("Too many numbers!")
for i in range(nr_letters):
    random_letter = random.sample(letters, nr_letters)
    for i in range(nr_symbols):
        random_symbol =random.sample(symbols, nr_symbols)
    for i in range(nr_numbers):
        random_number =random.sample(numbers, nr_numbers)
list = [random_letter, random_symbol, random_number]
#random.shuffle(list) - use to shuffle between list(l,n,s)

final_string = ""
for elem in list:
    final_string = final_string + ""
    for el in elem:
        final_string = final_string + str(el)
print(final_string)
