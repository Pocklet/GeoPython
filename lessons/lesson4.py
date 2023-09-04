def celsius_to_fahr(temp):
    return 9 / 5 * temp + 32

freezing_point = celsius_to_fahr(0)
print(f"The freezing point of water in Fahrenheit is {freezing_point}")

print(f"The boiling point of water in Fahrenheit is {celsius_to_fahr(100)}")


def kelvins_to_celsius(temp_kelvins):
    return temp_kelvins - 273.15

absolute_zero = kelvins_to_celsius(temp_kelvins=0)
print(f"Absolute zero in Celsius is {absolute_zero}")

# from temp_converter import celsius_to_fahr

# print(f"The freezing point of water in Fahrenheit is {celsius_to_fahr(0)}")

# import temp_converter as tc

# print(f"The freezing point of water in Fahrenheit is {tc.celsius_to_fahr(0)}")

# print(f"Absolute zero in Celsius is {tc.kelvins_to_celsius(temp_kelvins=0)}")

# print(f"Absolute zero in Fahrenheit is {tc.kelvins_to_fahr(temp_kelvins=0)}")



def temp_calculator(temp_k, convert_to):
    """
    Function for converting temperature in Kelvins to Celsius or Fahrenheit.

    Parameters
    ----------
    temp_k: <numerical>
        Temperature in Kelvins
    convert_to: <str>
        Target temperature that can be either Celsius ('C') or Fahrenheit ('F'). Supported values: 'C' | 'F'

    Returns
    -------
    <float>
        Converted temperature.
    """
    # Check if user wants the temperature in Celsius
    if convert_to == "C":
        converted_temp = kelvins_to_celsius(temp_kelvins=temp_k)
    elif convert_to == "F":
        converted_temp = kelvins_to_fahr(temp_kelvins=temp_k)
    # Return the result
    return converted_temp

# help(temp_calculator)

temp_kelvin = 30
temperature_c = temp_calculator(temp_k=temp_kelvin, convert_to="C")
print(f"Temperature {temp_kelvin} in Kelvins is {temperature_c} in Celsius")


import math
print(math.sqrt(81))

#can rename modules
import math as m
print(m.sqrt(49))
print(type(m))


import pandas as pd 

import matplotlib.pyplot as plt
# Plot a simple x y line graph with default settings
plt.plot([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])


print(dir(math))
help(math.sin)