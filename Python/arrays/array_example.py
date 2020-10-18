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
from python_array.two_d_array import Array2D

def one_dim_array():

    random_array = Array(100)

    for i in range(len(random_array)):
        random_array[i] = random.randint(0, 100)


    for value in random_array:
        print(value)

def two_dim_array():

    random_two_d_array = Array2D(5, 5)

    random_two_d_array[3, 1] = random.randint(0, 100)


    for row in range(5):
        for col in range(5):
            random_two_d_array[row, col] = random.randint(0, 100)


    for row in range(5):
        for col in range(5):
            print(random_two_d_array[row, col])


def main():

    one_dim_array()

    print("*************************")

    two_dim_array()

if __name__ == "__main__":
    main()