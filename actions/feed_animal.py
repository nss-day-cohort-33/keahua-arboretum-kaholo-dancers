from actions.feeding import feeding
# from index import main_menu
from animals.gold_gecko import Gold_Dust_Day_Gecko
from animals.pueo import Pueo
from animals.happy_face import Hawaiian_Happy_Face_Spider
from animals.kikakapu import Kikakapu
from animals.nene_goose import Nene_Goose
from animals.river_dolphin import RiverDolphin
from animals.opeapea import Opeapea
from animals.ulae import Ulae
from animals.animal import Animal
from actions.feeding import feeding_other


def feed_animal():

    print("1. River Dolphin")
    print("2. Happy-Face Spider")
    print("3. Pueo")
    print("4. Ulae")
    print("5. Gold Dust Day Gecko")
    print("6. Nene Goose")
    print("7. Kikakapu")
    print("8. Ope'ape'a")

    choice = input("Choose an animal to feed > ")


def feed_animal_menu():

    feed_animal()
    choice = input(">> ")

    if choice == "1":
        feeding(RiverDolphin)

    if choice == "2":
        feeding(Hawaiian_Happy_Face_Spider)

    if choice == "3":
        feeding(Pueo)

    if choice == "4":
        feeding(Ulae)

    if choice == "5":
        feeding(Gold_Dust_Day_Gecko)
        pass

    if choice == "6":
        feeding(Nene_Goose)
        pass

    if choice == "7":
        feeding(Kikakapu)
        pass

    if choice == "8":
        feeding_other(Opeapea)
        pass

    if choice != "9":
        # main_menu()
        pass