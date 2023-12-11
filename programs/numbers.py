#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print("Hello, please enter 4 numbers")
    number_1 = int(input("First number: "))
    number_2 = int(input("Second number: "))
    number_3 = int(input("Third number: "))
    number_4 = int(input("Fourth number: "))
    sum_1 = number_1 + number_2
    sum_2 = number_3 + number_4
    answer = sum_1 / sum_2
    print("The answer is:", round(answer, 2))
