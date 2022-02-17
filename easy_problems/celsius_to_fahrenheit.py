# -*- coding: utf-8 -*-
print("Type Celsius value and hit enter")
celsius_value = float(input())
fahrenheit_value = (celsius_value*1.8)+32
value = "{:.1f}".format(fahrenheit_value)
print(value + u'\u2109')