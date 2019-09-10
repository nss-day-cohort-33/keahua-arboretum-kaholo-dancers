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

    arboretum.rivers[int(choice) - 1].animals.append(animal)

    if choice == "2":
        animal = Hawaiian_Happy_Face_Spider()

    if choice == "3":
        animal = Pueo()

    if choice == "4":
        animal = Ulae()

    if choice == "5":
        animal = Gold_Dust_Day_Gecko()

    if choice == "6":
        animal = Nene_Goose()

    for index, grassland in enumerate(arboretum.grasslands):
            print(f'{index + 1}. Grassland {"%.8s" % grassland.id}')

    print("Release the animal into which biome?")
    choice = input("> ")

    arboretum.grasslands[int(choice) - 1].animals.append(animal)

    if choice == "7":
        animal = Kikakapu()

    for index, swamp in enumerate(arboretum.swamps):
        print(f'{index + 1}. swamp {"%.8s" % swamp.id}')

    print("Release the animal into which biome?")
    choice = input("> ")

    arboretum.swamps[int(choice) - 1].animals.append(animal)


    if choice == "8":
        animal = Opeapea()


    for index, river in enumerate(arboretum.rivers):
        print(f'{index + 1}. River {"%.8s" % river.id}')

    print("Release the animal into which biome?")
    choice = input("> ")

    arboretum.rivers[int(choice) - 1].animals.append(animal)


