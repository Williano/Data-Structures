"""
   Script: array_example.py
   Description: An example implementation of custom array data structure
   Programmer: William Kpabitey Kwabla
   Date: 10/10/2020
"""

# Standard library imports
import random

# Local imports
from python_array.arrays import Array


def main():

    random_array = Array(100)

    for i in range(len(random_array)):
        random_array[i] = random.randint(0, 100)


    for value in random_array:
        print(value)

if __name__ == "__main__":
    main()