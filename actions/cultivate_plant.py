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
            #Create Instance of the plant
            mountain_apple_tree = Mtn_Apple_Tree()

            #Function that takes the plant instance as the argument 
            def sub_menu_1(plant):
                #A loop that creates the menu options from the list of mountains inside our arboretum object
                for index, mountain in enumerate(arboretum.mountains):
                    try:
                        print(f'{index + 1}. Mountain ({len(mountain.plants)} plants)')
                    except:
                        pass
                print(f'x. cancel')
                
                choice = input("\nWhere would you like to plant the Mountain Apple Tree > \n")

                if choice == "x":
                    pass
                #if the user input is a number greater than the number of choices provided then print error
                elif int(choice) > len(arboretum.mountains):
                    print(f'Invalid Entry. Please choose from menu.')
                    sub_menu_1(plant)
                #Selects the correct mountain from the list and adds the instance of plant using the add_plant method on the mountain object
                else:
                    arboretum.mountains[int(choice) - 1].add_plant(plant, sub_menu_1)
            
            #Calls the function
            sub_menu_1(mountain_apple_tree)
        
        #Ensures that a user cannot select to add a plant without adding a biome
        else:
            print(f'\nThere are no biomes available for this plant! Please annex one.\n')

    #The same logic is used for every choice besides choice 4 and 5
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

    #Choice 4 is a plant that could go into mutliple biomes
    elif choice == "4":
        if len(arboretum.swamps) or len(arboretum.grasslands) > 0:
            #Creates the instance of the plant
            blue_jade = Blue_Jade()

            #Function that takes the plant instance as an argument
            def sub_menu_4(plant):
                #Loop trickery to get the correct numbering for the list when there are two types of biomes to account for
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

                #Caculation the length of the swamp list by itself and with the grassland list
                swamp_length = len(arboretum.swamps)
                both = swamp_length + len(arboretum.grasslands)

                if choice == "x":
                    pass
                #the length of both list is used for input validation
                elif int(choice) > both:
                    print(f'Invalid Entry. Please choose from menu.')
                    sub_menu_4(plant)
                elif int(choice) <= swamp_length:
                    arboretum.swamps[int(choice) - 1].add_plant(plant, sub_menu_4)
                #the length of the swamp list is used to calculate what index number the chosen swamp is at
                else:
                    arboretum.grasslands[int(choice) - swamp_length - 1].add_plant(plant, sub_menu_4)
            
            #The function is called and the instance is passed in
            sub_menu_4(blue_jade)
        
        else:
            print(f'\nThere are no biomes available for this plant! Please annex one.\n')
        
    elif choice == "5":
        pass

    #Tricky input validation
    else:
        print(f'\nThis is not a valid input\n')


    