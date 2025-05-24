import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '*', '+', '(', ')', '&']
print("Welcome to pypassword generator!")
n_letter = int(input("how many letters you want to use in your password?\n"))
n_number = int(input("how many numbers you want to use in your password?\n"))
n_symbol = int(input("how many symbols you want to use in your password?\n"))
password_list = []
for char in range (0,n_letter):
    password_list.append(random.choice(letters))
for char in range(0,n_number):
    password_list.append(random.choice(numbers))
for char in range(0,n_symbol):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char

print(f"your password is : {password}")

