#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    degree = int(input("Enter the number of full degrees:"))
    hours_number = degree * 12 // 360
    minutes_number = (12 * degree / 360 - hours_number) * 60
    minutes_number = int(minutes_number)
    print("Now", hours_number, ",", minutes_number, "minutes")
