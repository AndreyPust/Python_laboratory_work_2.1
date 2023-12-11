#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    length_rectangle = int(input("Enter the length of rectangle:"))
    width_rectangle = int(input("Enter the width of rectangle:"))
    perimetr = (length_rectangle + width_rectangle) * 2
    diagonal_rectangle = math.sqrt(length_rectangle**2 + width_rectangle**2)
    print("Perimetr of rectangle =", perimetr)
    print("Diagonal of rectangle =", diagonal_rectangle)
