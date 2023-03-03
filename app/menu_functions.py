from yeelight.transitions import *
from yeelight import Flow


def power_change(bulb):
    print("Toggling the light!")
    bulb.toggle()


def brightness(bulb):
    print("Changing brightness!")
    brightness_val = input("Enter value of brightness [1-100]: ")

    try:
        int(brightness_val)
    except ValueError:
        print("Wrong input!")
        return "Wrong input!"

    if 1 <= int(brightness_val) <= 100:
        bulb.set_brightness(int(brightness_val))
    else:
        print("Number out of range!")
        return "Number out of range!"


def temperature(bulb):
    print("Changing temperature!")
    minimal = bulb.get_model_specs()["color_temp"]["min"]
    maximal = bulb.get_model_specs()["color_temp"]["max"]
    temperature_val = input(f"Enter value from {minimal} (warm) - {maximal} (cold): ")

    try:
        int(temperature_val)
    except ValueError:
        print("Wrong input!")
        return "Wrong input!"

    if minimal <= int(temperature_val) <= maximal:
        bulb.set_color_temp(int(temperature_val))
    else:
        print("Number out of range!")
        return "Number out of range!"


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

    color_val = input(f"Enter color name: ")
    if color_val.lower() in colors:
        bulb.set_rgb(colors[color_val][0], colors[color_val][1], colors[color_val][2])
    else:
        print("Wrong input!")
        return "Wrong input!"


def scene(bulb):
    presets = ["disco", "temp", "strobe", "pulse", "strobe_color", "alarm", "police", "police2", "lsd", "rgb",
               "christmas", "random_loop", "slowdown"]
    disco()
    for i in presets:
        print(i)

    preset_val = input(f"Enter preset name: ")
    if preset_val.lower() in presets:
        flow = Flow(
            count=10,
            transitions=globals()[preset_val]()
        )
        bulb.start_flow(flow)
    else:
        print("Wrong input!")
        return "Wrong input!"


def info(bulb):
    print("Properties:")
    print(bulb.get_properties())
    print("Capabilities:")
    print(bulb.get_capabilities())
    print("Specifications:")
    print(bulb.get_model_specs())
