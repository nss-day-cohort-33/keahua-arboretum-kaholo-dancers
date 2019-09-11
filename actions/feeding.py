from animals.gold_gecko import Gold_Dust_Day_Gecko
from animals.pueo import Pueo
from animals.happy_face import Hawaiian_Happy_Face_Spider
from animals.kikakapu import Kikakapu
from animals.nene_goose import Nene_Goose
from animals.river_dolphin import RiverDolphin
from animals.opeapea import Opeapea
from animals.ulae import Ulae
from animals.animal import Animal


def feeding(animal):

    return animal


def feeding_other(animal):

    return animal


def animal_gets_fed(animal):
    print(f"1. {animal.prey[0]}")
    print(f"2. {animal.prey[1]}")
    print(f"3. {animal.prey[2]}")

    choice = input("Choose a prey to murder > ")

    if choice == "1":
        print(f"{animal.species} ate {animal.prey[0]}")
    if choice == "2":
        print(f"{animal.species} ate {animal.prey[1]}")
    if choice == "3":
        print(f"{animal.species} ate {animal.prey[2]}")


def other_animal_gets_fed(animal):
    print(f"1. {animal.prey[0]}")
    print(f"2. {animal.prey[1]}")
    print(f"3. {animal.prey[2]}")
    print(f"4. {animal.prey[3]}")
    print(f"5. {animal.prey[4]}")
    print(f"6. {animal.prey[5]}")

    choice = input("Choose a prey to murder > ")

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
