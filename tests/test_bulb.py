import os
import unittest
from unittest.mock import patch

from yeelight import *

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

        self.assertEqual(temp,2000)
        self.assertLessEqual(temp,int(maximal))
        self.assertGreaterEqual(temp,int(minimal))

    @patch('builtins.input', return_value='5')
    def test_temperature_too_small_value(self, mock_input):
        self.assertEqual(temperature(self.bulb), "Number out of range!")

    @patch('builtins.input', return_value='10000000')
    def test_temperature_too_big_value(self, mock_input):
        self.assertEqual(temperature(self.bulb), "Number out of range!")

    @patch('builtins.input', return_value='bulb')
    def test_temperature_not_number(self, mock_input):
        self.assertEqual(temperature(self.bulb), "Wrong input!")
