from plants import Blue_Jade
from plants import Mtn_Apple_Tree
from plants import Rainbow_Tree
from plants import Silversword

def cultivate_plant(arboretum):

    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")

    choice = input("Choose a plant to cultivate > ")

    if choice == "1":
        mountain_apple_tree = Mtn_Apple_Tree()

        print("")

    if choice == "2":
        silversword = Silversword()
    if choice == "3":
        rainbow_tree = Rainbow_Tree()
    if choice == "4":
        blue_jade = Blue_Jade()

    