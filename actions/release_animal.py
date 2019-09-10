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

        for index, river in enumerate(arboretum.rivers):
            print(f'{index + 1}. River {"%.8s" % river.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.rivers[int(choice) - 1].add_animal(animal)

    if choice == "2":
        animal = Hawaiian_Happy_Face_Spider()

        for index, swamp in enumerate(arboretum.swamps):
            print(f'{index + 1}. Swamp {"%.8s" % swamp.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.swamps[int(choice) - 1].add_animal(animal)

    if choice == "3":
        animal = Pueo()

    if choice == "4":
        animal = Ulae()

        for index, coastline in enumerate(arboretum.coastlines):
            print(f'{index + 1}. Coastline {"%.8s" % coastline.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.coastlines[int(choice) - 1].add_animal(animal)

    if choice == "5":
        animal = Gold_Dust_Day_Gecko()

        for index, forest in enumerate(arboretum.forests):
            print(f'{index + 1}. Forest {"%.8s" % forest.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.forests[int(choice) - 1].add_animal(animal)

    if choice == "6":
        animal = Nene_Goose()

        for index, grassland in enumerate(arboretum.grasslands):
                print(f'{index + 1}. Grassland {"%.8s" % grassland.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.grasslands[int(choice) - 1].add_animal(animal)

    if choice == "7":
        animal = Kikakapu()

        for index, swamp in enumerate(arboretum.swamps):
            print(f'{index + 1}. swamp {"%.8s" % swamp.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.swamps[int(choice) - 1].add_animal(animal)


    if choice == "8":
        animal = Opeapea()

        for index, mountain in enumerate(arboretum.mountains):
            print(f'{index + 1}. Mountain {"%.8s" % mountain.id}')

        print("Release the animal into which biome?")
        choice = input("> ")

        arboretum.mountains[int(choice) - 1].add_animal(animal)
        print("it added")

    # for index, river in enumerate(arboretum.rivers):
    #     print(f'{index + 1}. River {"%.8s" % river.id}')

    # print("Release the animal into which biome?")
    # choice = input("> ")

    # arboretum.rivers[int(choice) - 1].animals.add_animal(animal)


