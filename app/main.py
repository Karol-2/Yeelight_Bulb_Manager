import os

from yeelight import *

from menu_functions import *


def main():
    global bulb

    if 'BULB' in os.environ:
        print("Env variable found")
        ip = os.getenv('BULB')
        bulb = Bulb(ip)
    else:
        print("No env variable found, searching for bulbs")
        bulbs = discover_bulbs()
        first_bulb = bulbs[0]
        ip = first_bulb['ip']
        bulb = Bulb(ip)

    menu()


def menu():
    os.system('cls')
    is_turned_on = True if bulb.get_properties()['power'] == 'on' else False

    print("==========================================")
    print("1.Toggle bulb")
    if is_turned_on:
        print("2.Set brightness")
        print("3.Set temperature")
        print("4.Set color")
        print("5.Set Scene")
    print("6.Info")
    print("7.Exit")
    print("==========================================")

    choice = input("Choose action: ")

    os.system('cls')

    if choice == "1":
        power_change(bulb)
        menu()
    elif choice == "2" and is_turned_on:
        brightness(bulb)
        menu()
    elif choice == "3" and is_turned_on:
        temperature(bulb)
        menu()
    elif choice == "4" and is_turned_on:
        color(bulb)
        menu()
    elif choice == "5" and is_turned_on:
        scene(bulb)
        menu()
    elif choice == "6":
        info(bulb)
        menu()
    elif choice == "7":
        exit(0)
    else:
        print("Wrong input")
        menu()


if __name__ == "__main__":
    main()
