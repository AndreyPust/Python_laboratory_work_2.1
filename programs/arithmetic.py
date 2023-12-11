#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    print("Hello, please solve the example: 4 * 100 - 54")
    user_answer = int(input("Your answer: "))
    real_answer = 4 * 100 - 54
    if real_answer == user_answer:
        print("This answer is correct!", "Your answer:",
              user_answer, "Right answer:", real_answer)
    else:
        print("This answer is not correct!", "Your answer:",
              user_answer, "Right answer:", real_answer)
