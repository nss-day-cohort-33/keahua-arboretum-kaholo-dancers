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

        def sub_menu_1(plant):
            for index, mountain in enumerate(arboretum.mountains):
                try:
                    print(f'{index + 1}. Mountain ({len(mountain.plants)} plants)')
                except:
                    pass
            
            choice = input("Where would you like to plant the Mountain Apple Tree > ")

            arboretum.mountains[int(choice) - 1].add_plant(plant, sub_menu_1)
        
        sub_menu_1(mountain_apple_tree)

    if choice == "2":
        silversword = Silversword()

        def sub_menu_2(plant):
            for index, grassland in enumerate(arboretum.grasslands):
                try:
                    print(f'{index + 1}. Grassland ({len(grassland.plants)} plants)')
                except:
                    pass
            
            choice = input("Where would you like to plant the Silversword > ")

            arboretum.grasslands[int(choice) - 1].add_plant(plant, sub_menu_2)

        sub_menu_2(silversword)

    if choice == "3":
        rainbow_tree = Rainbow_Tree()

        def sub_menu_3(plant):
            for index, forest in enumerate(arboretum.forests):
                try:
                    print(f'{index + 1}. Forest ({len(forest.plants)} plants)')
                except:
                    pass
            
            choice = input("Where would you like to plant the Rainbow Eucalyptus Tree > ")

            arboretum.forests[int(choice) - 1].add_plant(plant, sub_menu_3)

        sub_menu_3(rainbow_tree)

    if choice == "4":
        blue_jade = Blue_Jade()

        def sub_menu_4(plant):
            num = 1
            for swamp in arboretum.swamps:
                try:
                    print(f'{num}. {swamp.name} ({len(swamp.plants)} plants)')
                    num += 1
                except:
                    pass
            for grassland in arboretum.grasslands:
                try:
                    print(f'{num}. {grassland.name} ({len(grassland.plants)} plants)')
                    num += 1
                except:
                    pass
                    
            choice = input("Where would you like to plant the Blue Jade Vine > ")

            swamp_length = len(arboretum.swamps)

            if int(choice) <= swamp_length:
                arboretum.swamps[int(choice) - 1].add_plant(plant, sub_menu_4)
            else:
                arboretum.grasslands[int(choice) - swamp_length - 1].add_plant(plant, sub_menu_4)
        
        sub_menu_4(blue_jade)


    