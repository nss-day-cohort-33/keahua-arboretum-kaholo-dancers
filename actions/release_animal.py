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
            num = 1
            for river in (arboretum.rivers):
                try:
                    print(f'{num}. {river.name} ({len(river.animals)} animals)')
                    num += 1
                except:
                    pass
            for coastline in (arboretum.coastlines):
                try:
                    print(f'{num}. {coastline.name} ({len(coastline.animals)} animals)')
                    num += 1
                except:
                    pass

            print("Release the animal into which biome?")
            choice = input("> ")

            river_length = len(arboretum.rivers)

            if int(choice) <= river_length:
                arboretum.rivers[int(choice) - 1].add_animal(animal, animal_to_biome_1)
            else:
                arboretum.coastlines[int(choice) - river_length - 1].add_animal(animal, animal_to_biome_1)

        animal_to_biome_1(animal)

    if choice == "2":
        animal = Hawaiian_Happy_Face_Spider()

        def animal_to_biome_2(animal):
            for index, swamp in enumerate(arboretum.swamps):
                print(f'{index + 1}. {swamp.name} ({len(swamp.animals)} animals)')

            print("Release the animal into which biome?")
            choice = input("> ")

            arboretum.swamps[int(choice) - 1].add_animal(animal, animal_to_biome_2)

        animal_to_biome_2(animal)


    if choice == "3":
        animal = Pueo()

        def animal_to_biome_3(animal):
            num = 1
            for grassland in (arboretum.grasslands):
                try:
                    print(f'{num}. {grassland.name} ({len(grassland.animals)} animals)')
                    num += 1
                except:
                    pass
            for forest in (arboretum.forests):
                try:
                    print(f'{num}. {forest.name} ({len(forest.animals)} animals)')
                    num += 1
                except:
                    pass

            print("Release the animal into which biome?")
            choice = input("> ")

            grassland_length = len(arboretum.grasslands)

            if int(choice) <= grassland_length:
                arboretum.grasslands[int(choice) - 1].add_animal(animal, animal_to_biome_3)
            else:
                arboretum.forests[int(choice) - grassland_length - 1].add_animal(animal, animal_to_biome_3)

        animal_to_biome_3(animal)

    if choice == "4":
        animal = Ulae()

        def animal_to_biome_4(animal):
            for index, coastline in enumerate(arboretum.coastlines):
                print(f'{index + 1}. {coastline.name} ({len(coastline.animals)} animals)')

            print("Release the animal into which biome?")
            choice = input("> ")

            arboretum.coastlines[int(choice) - 1].add_animal(animal, animal_to_biome_4)
        animal_to_biome_4(animal)

    if choice == "5":
        animal = Gold_Dust_Day_Gecko()

        def animal_to_biome_5(animal):
            for index, forest in enumerate(arboretum.forests):
                print(f'{index + 1}. {forest.name} ({len(forest.animals)} animals)')

            print("Release the animal into which biome?")
            choice = input("> ")

            arboretum.forests[int(choice) - 1].add_animal(animal, animal_to_biome_5)

        animal_to_biome_5(animal)

    if choice == "6":
        animal = Nene_Goose()

        def animal_to_biome_6(animal):
            for index, grassland in enumerate(arboretum.grasslands):
                    print(f'{index + 1}. {grassland.name} ({len(grassland.animals)} animals)')

            print("Release the animal into which biome?")
            choice = input("> ")

            arboretum.grasslands[int(choice) - 1].add_animal(animal, animal_to_biome_6)

        animal_to_biome_6(animal)

    if choice == "7":
        animal = Kikakapu()

        def animal_to_biome_7(animal):
            num = 1
            for river in (arboretum.rivers):
                try:
                    print(f'{num}. {river.name} ({len(river.animals)} animals)')
                    num += 1
                except:
                    pass
            for swamp in (arboretum.swamps):
                try:
                    print(f'{num}. {swamp.name} ({len(swamp.animals)} animals)')
                    num += 1
                except:
                    pass

            print("Release the animal into which biome?")
            choice = input("> ")

            river_length = len(arboretum.rivers)

            if int(choice) <= river_length:
                arboretum.rivers[int(choice) - 1].add_animal(animal, animal_to_biome_7)
            else:
                arboretum.swamps[int(choice) - river_length - 1].add_animal(animal, animal_to_biome_7)

        animal_to_biome_7(animal)


    if choice == "8":
        animal = Opeapea()

        def animal_to_biome_8(animal):
            num = 1
            for mountain in (arboretum.mountains):
                try:
                    print(f'{num}. {mountain.name} ({len(mountain.animals)} animals)')
                    num += 1
                except:
                    pass
            for forest in (arboretum.forests):
                try:
                    print(f'{num}. {forest.name} ({len(forest.animals)} animals)')
                    num += 1
                except:
                    pass

            print("Release the animal into which biome?")
            choice = input("> ")

            mountain_length = len(arboretum.mountains)

            if int(choice) <= mountain_length:
                arboretum.mountains[int(choice) - 1].add_animal(animal, animal_to_biome_8)
            else:
                arboretum.forests[int(choice) - mountain_length - 1].add_animal(animal, animal_to_biome_8)

        animal_to_biome_8(animal)

    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {"%.8s" % river.id}')

    # print("Release the animal into which biome?")
    # choice = input("> ")

    # arboretum.rivers[int(choice) - 1].animals.add_animal(animal)


