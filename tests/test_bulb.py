import os
import unittest
from unittest.mock import patch

from colour import hex2rgb
from yeelight import *
from io import StringIO
from app.menu_functions import *


class TestBulbFunctions(unittest.TestCase):
    ip = os.getenv('BULB')
    bulb = Bulb(ip)
    bulb.turn_on()

    def test_toggle(self):
        self.bulb.turn_off()
        power_change(self.bulb)
        self.assertEqual(self.bulb.get_properties()['power'], 'on', "Bulb doesn't turn on")

    @patch('builtins.input', return_value='50')
    def test_brightness_valid_input(self, mock_input):
        brightness(self.bulb)
        self.assertEqual(self.bulb.get_properties()["bright"], '50', "Brightness hasn't changed")

    @patch('builtins.input', return_value='999999')
    def test_brightness_too_big_value(self, mock_input):
        self.assertEqual(brightness(self.bulb), "Number out of range!")

    @patch('builtins.input', return_value='0')
    def test_brightness_too_small_value(self, mock_input):
        self.assertEqual(brightness(self.bulb), "Number out of range!")

    @patch('builtins.input', return_value='not a number')
    def test_brightness_invalid_input(self, mock_input):
        self.assertEqual(brightness(self.bulb), "Wrong input!")

    @patch('builtins.input', return_value='2000')
    def test_temperature_valid_input(self, mock_input):
        minimal = int(self.bulb.get_model_specs()["color_temp"]["min"])
        maximal = int(self.bulb.get_model_specs()["color_temp"]["max"])
        temp = int(self.bulb.get_properties()['ct'])

        self.assertEqual(temp, 2000)
        self.assertLessEqual(temp, int(maximal))
        self.assertGreaterEqual(temp, int(minimal))

    @patch('builtins.input', return_value='5')
    def test_temperature_too_small_value(self, mock_input):
        self.assertEqual(temperature(self.bulb), "Number out of range!")

    @patch('builtins.input', return_value='10000000')
    def test_temperature_too_big_value(self, mock_input):
        self.assertEqual(temperature(self.bulb), "Number out of range!")

    @patch('builtins.input', return_value='bulb')
    def test_temperature_not_number(self, mock_input):
        self.assertEqual(temperature(self.bulb), "Wrong input!")

    @patch('builtins.input', return_value='lavender')
    def test_color_valid(self, mock_input):
        lavender_rgb = (230, 230, 250)
        color(self.bulb)
        bulb_color_hex = '#' + hex(int(self.bulb.get_properties()['rgb']))[2::]
        bulb_color_val = hex2rgb(bulb_color_hex)
        bulb_color_rgb = tuple(x * 255 for x in bulb_color_val)

        self.assertEqual(int(bulb_color_rgb[0]), lavender_rgb[0], "First rgb value incurrect!")
        self.assertEqual(int(bulb_color_rgb[1]), lavender_rgb[1], "Second rgb value incurrect!")
        self.assertEqual(int(bulb_color_rgb[2]), lavender_rgb[2], "Third rgb value incurrect!")

    @patch('builtins.input', return_value='pinky yellow green grass')
    def test_color_invalid_input(self, mock_input):
        color(self.bulb)
        self.assertEqual(color(self.bulb), "Wrong input!", "Accepted invalid input!")

    def test_info_showcase(self):
        phrases_to_find = ["power", "color_temp", "name"]
        captured_output = StringIO()
        info(self.bulb)
        output = captured_output.getvalue()
        for phrase in phrases_to_find:
            self.assertIn(phrase, output)
