import random

list_of_names = input("Give me the names: ")
names = list_of_names.split(", ")

whoPays = random.randint(0, len(names) -1)

print (f"Person who pays is: {names[whoPays]}")