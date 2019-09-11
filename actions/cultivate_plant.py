from plants import Blue_Jade
from plants import Mtn_Apple_Tree
from plants import Rainbow_Tree
from plants import Silversword

def cultivate_plant(arboretum):

    print("1. Mountain Apple Tree")
    print("2. Silversword")
    print("3. Rainbow Eucalyptus Tree")
    print("4. Blue Jade Vine")
    print("5. Cancel")

    choice = input("\nChoose a plant to cultivate > \n")

    if choice == "1":
        if len(arboretum.mountains) > 0:
            mountain_apple_tree = Mtn_Apple_Tree()

            def sub_menu_1(plant):
                for index, mountain in enumerate(arboretum.mountains):
                    try:
                        print(f'{index + 1}. Mountain ({len(mountain.plants)} plants)')
                    except:
                        pass
                print(f'x. cancel')
                
                choice = input("\nWhere would you like to plant the Mountain Apple Tree > \n")

                if choice == "x":
                    pass
                elif int(choice) > len(arboretum.mountains):
                    print(f'Invalid Entry. Please choose from menu.')
                    sub_menu_1(plant)
                else:
                    arboretum.mountains[int(choice) - 1].add_plant(plant, sub_menu_1)
            
            sub_menu_1(mountain_apple_tree)
        
        else:
            print(f'\nThere are no biomes available for this plant! Please annex one.\n')

    elif choice == "2":
        if len(arboretum.grasslands) > 0:
            silversword = Silversword()

            def sub_menu_2(plant):
                for index, grassland in enumerate(arboretum.grasslands):
                    try:
                        print(f'{index + 1}. Grassland ({len(grassland.plants)} plants)')
                    except:
                        pass
                print(f'x. cancel')
                
                choice = input("\nWhere would you like to plant the Silversword > \n")

                if choice == "x":
                    pass
                elif int(choice) > len(arboretum.grasslands):
                    print(f'Invalid Entry. Please choose from menu.')
                    sub_menu_2(plant)
                else:
                    arboretum.grasslands[int(choice) - 1].add_plant(plant, sub_menu_2)

            sub_menu_2(silversword)
        
        else:
            print(f'\nThere are no biomes available for this plant! Please annex one.\n')

    elif choice == "3":
        if len(arboretum.forests) > 0:
            rainbow_tree = Rainbow_Tree()

            def sub_menu_3(plant):
                for index, forest in enumerate(arboretum.forests):
                    try:
                        print(f'{index + 1}. Forest ({len(forest.plants)} plants)')
                    except:
                        pass
                print(f'x. cancel')
                
                choice = input("\nWhere would you like to plant the Rainbow Eucalyptus Tree > \n")

                if choice == "x":
                    pass
                elif int(choice) > len(arboretum.forests):
                    print(f'Invalid Entry. Please choose from menu.')
                    sub_menu_3(plant)
                else:
                    arboretum.forests[int(choice) - 1].add_plant(plant, sub_menu_3)

            sub_menu_3(rainbow_tree)
        
        else:
            print(f'\nThere are no biomes available for this plant! Please annex one.\n')

    elif choice == "4":
        if len(arboretum.swamps) or len(arboretum.grasslands) > 0:
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
                print(f'x. cancel')
                        
                choice = input("\nWhere would you like to plant the Blue Jade Vine > \n")

                swamp_length = len(arboretum.swamps)
                both = swamp_length + len(arboretum.grasslands)

                if choice == "x":
                    pass
                elif int(choice) > both:
                    print(f'Invalid Entry. Please choose from menu.')
                    sub_menu_4(plant)
                elif int(choice) <= swamp_length:
                    arboretum.swamps[int(choice) - 1].add_plant(plant, sub_menu_4)
                else:
                    arboretum.grasslands[int(choice) - swamp_length - 1].add_plant(plant, sub_menu_4)
            
            sub_menu_4(blue_jade)
        
        else:
            print(f'\nThere are no biomes available for this plant! Please annex one.\n')
        
    elif choice == "5":
        pass

    else:
        print(f'\nThis is not a valid input\n')


    