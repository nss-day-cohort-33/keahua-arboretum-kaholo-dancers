from animals import *

def release_animal(arboretum):
    # animal = None

    print("1. River Dolphin")
    print("2. Happy-Face Spider")
    print("3. Pueo")
    print("4. Ulae")
    print("2. Gold Dust Day Gecko")
    print("6. Nene Goose")
    print("7. Kikakapu")
    print("8. Ope'ape'a")

    choice = input("Choose animal to release > ")

    if choice == "1":
        animal = RiverDolphin()

        def animal_to_biome_1(animal):
            for index, river in enumerate(arboretum.rivers):
                try:
                    print(f'{index + 1}. {river.name} ({len(river.animals)} animals)')
                except:
                    pass
            for index, coastline in enumerate(arboretum.coastlines):
                try:
                    print(f'{index + 1}. {coastline.name} ({len(coastline.animals)} animals)')
                except:
                    pass

            print("Release the animal into which biome?")
            choice = input("> ")

            river_length = len(arboretum.rivers)

            if int(choice) <= river_length:
                arboretum.rivers[int(choice) - 1].add_animal(animal, animal_to_biome_1)
            else:
                arboretum.coastlines[int(choice) - 1].add_animal(animal, animal_to_biome_1)

        animal_to_biome_1(animal)

    if choice == "2":
        animal = Hawaiian_Happy_Face_Spider()

        def animal_to_biome_2(animal):
            for index, swamp in enumerate(arboretum.swamps):
                print(f'{index + 1}. Swamp {"%.8s" % swamp.id}')

            print("Release the animal into which biome?")
            choice = input("> ")

            arboretum.swamps[int(choice) - 1].add_animal(animal)

        animal_to_biome_2(animal)


    if choice == "3":
        animal = Pueo()

        def animal_to_biome_3(animal):
            for index, grassland in enumerate(arboretum.grasslands):
                try:
                    print(f'{index + 1}. {grassland.name} ({len(grassland.animals)} animals)')
                except:
                    pass
            for index, forest in enumerate(arboretum.forests):
                try:
                    print(f'{index + 1}. {forest.name} ({len(forest.animals)} animals)')
                except:
                    pass

            print("Release the animal into which biome?")
            choice = input("> ")

            grassland_length = len(arboretum.grasslands)

            if int(choice) <= grassland_length:
                arboretum.grasslands[int(choice) - 1].add_animal(animal, animal_to_biome_3)
            else:
                arboretum.forests[int(choice) - 1].add_animal(animal, animal_to_biome_3)

        animal_to_biome_3(animal)

    if choice == "4":
        animal = Ulae()

        def animal_to_biome_4(animal):
            for index, coastline in enumerate(arboretum.coastlines):
                print(f'{index + 1}. Coastline {"%.8s" % coastline.id}')

            print("Release the animal into which biome?")
            choice = input("> ")

            arboretum.coastlines[int(choice) - 1].add_animal(animal)
        animal_to_biome_4(animal)

    if choice == "5":
        animal = Gold_Dust_Day_Gecko()

        def animal_to_biome_5(animal):
            for index, forest in enumerate(arboretum.forests):
                print(f'{index + 1}. Forest {"%.8s" % forest.id}')

            print("Release the animal into which biome?")
            choice = input("> ")

            arboretum.forests[int(choice) - 1].add_animal(animal)
            
        animal_to_biome_5(animal)

    if choice == "6":
        animal = Nene_Goose()

        def animal_to_biome_6(animal):
            for index, grassland in enumerate(arboretum.grasslands):
                    print(f'{index + 1}. Grassland {"%.8s" % grassland.id}')

            print("Release the animal into which biome?")
            choice = input("> ")

            arboretum.grasslands[int(choice) - 1].add_animal(animal)

        animal_to_biome_6(animal)

    if choice == "7":
        animal = Kikakapu()

        def animal_to_biome_7(animal):
            for index, river in enumerate(arboretum.rivers):
                try:
                    print(f'{index + 1}. {river.name} ({len(river.animals)} animals)')
                except:
                    pass
            for index, swamp in enumerate(arboretum.swamps):
                try:
                    print(f'{index + 1}. {swamp.name} ({len(swamp.animals)} animals)')
                except:
                    pass

            print("Release the animal into which biome?")
            choice = input("> ")

            river_length = len(arboretum.rivers)

            if int(choice) <= river_length:
                arboretum.rivers[int(choice) - 1].add_animal(animal, animal_to_biome_7)
            else:
                arboretum.swamps[int(choice) - 1].add_animal(animal, animal_to_biome_7)

        animal_to_biome_7(animal)


    if choice == "8":
        animal = Opeapea()

        def animal_to_biome_8(animal):
            for index, mountain in enumerate(arboretum.mountains):
                try:
                    print(f'{index + 1}. {mountain.name} ({len(mountain.animals)} animals)')
                except:
                    pass
            for index, forest in enumerate(arboretum.forests):
                try:
                    print(f'{index + 1}. {forest.name} ({len(forest.animals)} animals)')
                except:
                    pass

            print("Release the animal into which biome?")
            choice = input("> ")

            mountain_length = len(arboretum.mountains)

            if int(choice) <= mountain_length:
                arboretum.mountains[int(choice) - 1].add_animal(animal, animal_to_biome_8)
            else:
                arboretum.forests[int(choice) - 1].add_animal(animal, animal_to_biome_8)

        animal_to_biome_8(animal)

    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {"%.8s" % river.id}')

    # print("Release the animal into which biome?")
    # choice = input("> ")

    # arboretum.rivers[int(choice) - 1].animals.add_animal(animal)


