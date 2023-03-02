def power_change(bulb):
    print("Toggling the light!")
    bulb.toggle()
    input("Press Enter to continue...")


def brightness(bulb):
    print("Changing brightness!")
    brightness_val = input("Enter value of brightness [1-100]: ")  # TODO: different input cases
    bulb.set_brightness(int(brightness_val))
    input("Press Enter to continue...")


def temperature(bulb):
    print("Changing temperature!")
    min = bulb.get_model_specs()["color_temp"]["min"]
    max = bulb.get_model_specs()["color_temp"]["max"]
    temperature_val = input(f"Enter value from {min} (warm) - {max} (cold): ")  # TODO: different input cases
    bulb.set_color_temp(int(temperature_val))

    input("Press Enter to continue...")


def color(bulb):
    print("Available colors:")
    colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "cyan": (0, 255, 255),
        "magenta": (255, 0, 255),
        "orange": (255, 165, 0),
        "purple": (128, 0, 128),
        "chartreuse": (173, 255, 47),
        "lime": (0, 255, 0),
        "lavender": (230, 230, 250),
        "pink": (255, 192, 203),
        "turquoise": (64, 224, 208),
        "brown": (165, 42, 42),
        "khaki": (240, 230, 140)
    }

    for i in colors:
        print(i)

    color_val = input(f"Enter color name: ")  # TODO: different input cases
    bulb.set_rgb(colors[color_val][0], colors[color_val][1], colors[color_val][2])


def scene(bulb):  # TODO: add function
    print("bulbb")


def info(bulb):
    print("Properties:")
    print(bulb.get_properties())
    print("Capabilities:")
    print(bulb.get_capabilities())
    print("Specifications:")
    print(bulb.get_model_specs())
    input("Press Enter to continue...")
