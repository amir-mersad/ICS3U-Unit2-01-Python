#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program calculates the area and the perimeter of a circle
#     with radius 15mm

import math


def main():
    print("If a circle has a radius of 15mm:")
    print("")
    print("area is {}mm^2".format(math.pi*15**2))
    print("Perimeter is {}mm".format(2*math.pi*15))


if __name__ == "__main__":
    main()
