"""
Celsius to Fahrenheit
=====================

You are making a Celsius to Fahrenheit converter.
Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.

Sample Input
36

Sample Output
96.8

NOTE: the following equation is used to calculate the Fahrenheit value:
9/5 * celsius + 32
"""

celsius = int(input())

def converter(c):
    return 9/5*c+32


fahrenheit = converter(celsius)
print(fahrenheit)