import os

from yeelight import *


def main():
    bulbs = discover_bulbs()

    IP = os.getenv('BULB')
    bulb = Bulb(IP)

    print(bulb)

    bulb.toggle()

    print(bulb.get_properties())


if __name__ == "__main__":
    main()
