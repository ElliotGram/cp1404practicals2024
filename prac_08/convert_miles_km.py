"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Elliot Gram, IT@JCU
Started 27/07/2024
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Elliot Gram'


class MilesToKmConversion(App):
    """ MilesToKmConversion is a Kivy App for converting Miles to Kilometers """

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 400)
        self.title = "Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        try:
            result = float(value) / 0.6214
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass

    def increase_input(self, user_input):
        """ Increase the value in the input field by 1 """
        try:
            user_input = float(user_input) + 1
            self.root.ids.input_number.text = str(user_input)
            self.handle_calculate(user_input)
        except ValueError:
            self.root.ids.output_label.text = "Invalid Input"

    def decrease_input(self, user_input):
        """ Decrease the value in the input field by 1 """
        try:
            user_input = float(user_input) - 1
            self.root.ids.input_number.text = str(user_input)
            self.handle_calculate(user_input)
        except ValueError:
            self.root.ids.output_label.text = "Invalid Input"


MilesToKmConversion().run()
