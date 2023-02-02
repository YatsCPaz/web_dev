#Password Generator Project
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# i_password = ""

# for i in range(1, nr_letters+1):
#     random_order = random.randint(0,nr_letters)
#     i_password += letters[random_order]

# for s in range(1, nr_symbols+1):
#     random_order = random.randint(0,nr_symbols)
#     i_password += symbols[random_order]

# for n in range(1, nr_numbers+1):
#     random_order = random.randint(0, nr_numbers)
#     i_password += numbers[random_order]

# print(f'''
#                    __
#                   // \\
#                   \\\_/ //
# ''-.._.-''-.._.. -(||)(')     New Password: {i_password}
#                      ''')


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
i_password = ""
pass_lenght = nr_letters + nr_numbers + nr_symbols

for i in range(1, pass_lenght+1):

    set_caracter = 0
    while set_caracter < 1:
        random_order = random.randint(1, 3)
        ## Random letters
        if random_order == 1:
            if nr_letters == 0:
                set_caracter = 0
            else:
                random_letter = random.randint(0, len(letters))
                i_password += letters[random_letter]
                nr_letters -= 1
                set_caracter = 1

        if random_order == 2:
            if nr_symbols == 0:
                set_caracter = 0
            else:    
                random_letter = random.randint(0, len(symbols))
                i_password += symbols[random_letter]
                nr_symbols -= 1
                set_caracter = 1

        if random_order == 3:
            if nr_numbers == 0:
                set_caracter = 0
            else:
                random_letter = random.randint(0, len(numbers))
                i_password += numbers[random_letter]
                nr_numbers -= 1
                set_caracter = 1

print(f'''
                   __
                  // \\
                  \\\_/ //
''-.._.-''-.._.. -(||)(')     New Password: {i_password}
                     ''')

#Hard Level - Other opcion Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P                     
#Hard Level
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")