from animals.gold_gecko import Gold_Dust_Day_Gecko
from animals.pueo import Pueo
from animals.happy_face import Hawaiian_Happy_Face_Spider
from animals.kikakapu import Kikakapu
from animals.nene_goose import Nene_Goose
from animals.river_dolphin import RiverDolphin
from animals.opeapea import Opeapea
from animals.ulae import Ulae
from animals.animal import Animal

# insects = ["Termites", "Moths", "Beetles"]

# rodents = ["Mouse", "Mongoose", "Rat"]

# fish = ["Trout", "Mackarel", "Sardine"]

# vegetation = ["Grass", "Weeds", "Berries"]


def feeding(animal):
    print(f"1. {animal.prey[0]}")
    print(f"2. {animal.prey[1]}")
    print(f"3. {animal.prey[2]}")

    choice = input("Choose a prey to murder > ")
    
    return animal

    # animal_gets_fed(animal)


def feeding_other(animal):
    print(f"1. {animal.prey[0]}")
    print(f"2. {animal.prey[1]}")
    print(f"3. {animal.prey[2]}")
    print(f"4. {animal.prey[3]}")
    print(f"5. {animal.prey[4]}")
    print(f"6. {animal.prey[5]}")

    choice = input("Choose a prey to murder > ")
    
    return animal

    # other_animal_gets_fed(animal)


def animal_gets_fed(animal):

    feeding(animal)
    choice = input(">> ")

    if choice == "1":
        print(f"{animal.species} ate {animal.prey[0]}")
    if choice == "2":
        print(f"{animal.species} ate {animal.prey[1]}")
    if choice == "3":
        print(f"{animal.species} ate {animal.prey[2]}")


def other_animal_gets_fed(animal):

    feeding_other(animal)
    choice = input(">> ")

    if choice == "1":
        print(f"{animal.species} ate {animal.prey[0]}")
    if choice == "2":
        print(f"{animal.species} ate {animal.prey[1]}")
    if choice == "3":
        print(f"{animal.species} ate {animal.prey[2]}")
    if choice == "4":
        print(f"{animal.species} ate {animal.prey[3]}")
    if choice == "5":
        print(f"{animal.species} ate {animal.prey[4]}")
    if choice == "6":
        print(f"{animal.species} ate {animal.prey[5]}")


# def feed_animal_menu():
#     """Show Keahua Action Options

#     Arguments: None
#     """
#     build_menu()
#     choice = input(">> ")

#     if choice == "1":
#         annex_habitat(keahua)

#     if choice == "2":
#         release_animal(keahua)

#     if choice == "3":
#         feed_animal(keahua)

#     if choice == "4":
#         cultivate_plant(keahua)

#     if choice == "5":
#         build_facility_report(keahua)
#         pass

#     if choice == "6":
#         build_facility_report(keahua)
#         pass

#     if choice == "7":
#         build_facility_report(keahua)
#         pass

#     if choice == "8":
#         build_facility_report(keahua)
#         pass

#     if choice != "9":
#         build_facility_report(keahua)
#         pass


# main_menu()
