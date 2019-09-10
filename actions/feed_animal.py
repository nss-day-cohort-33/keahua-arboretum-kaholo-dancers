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
from actions.feeding import animal_gets_fed
from actions.feeding import other_animal_gets_fed

dolphin = RiverDolphin()
gecko = Gold_Dust_Day_Gecko()
pueo = Pueo()
spider = Hawaiian_Happy_Face_Spider()
kikakapu = Kikakapu()
goose = Nene_Goose()
opeapea = Opeapea()
ulae = Ulae()
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
        animal_gets_fed(dolphin)

    if choice == "2":
        animal_gets_fed(spider)

    if choice == "3":
        animal_gets_fed(pueo)

    if choice == "4":
        animal_gets_fed(ulae)

    if choice == "5":
        animal_gets_fed(gecko)
        pass

    if choice == "6":
        animal_gets_fed(goose)
        pass

    if choice == "7":
        animal_gets_fed(kikakapu)
        pass

    if choice == "8":
        other_animal_gets_fed(opeapea)
        pass

    if choice != "9":
        # main_menu()
        pass