import another_module
import prettytable
#import turtle
#tom = turtle.Turtle()

from prettytable import PrettyTable

table = PrettyTable()
print(table._align)
pokemons = ["Pikachu", "Squirtle", "Charmander"]
types = ["Electric", "Water", "Fire"]
table.add_column("Pokemon Name",pokemons)
table.add_column("Type", types)

print(table)

from turtle import Turtle, Screen

tommy = Turtle()
tommy.shape("turtle")
tommy.color("purple")

my_screen = Screen()
my_screen.exitonclick()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(another_module.another_varible)  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
