from logg import logging
from mod_calc import sum, mul, div, sub, div_op, div_os

def check_zero_div(a, b, f):
    if f == 1:
        try:
            print(f"result = {div(a,b)}")
        except ZeroDivisionError:
            logging.error("Division by zero")
            print("Incorrect input. Devision by 0!")
    if f == 2:
        try:
            print(f"result = {div_op(a,b)}")
        except ZeroDivisionError:
            logging.error("Division by zero")
            print("Incorrect input. Devision by 0!")
    if f == 3:
        try:
            print(f"result = {div_os(a,b)}")
        except ZeroDivisionError:
            logging.error("Division by zero")
            print("Incorrect input. Devision by 0!")
