from logg import logging
from mod_calc import * #sum, mul, div, sub, div_op, div_os
from excep import *

def menu():
    while True:
        item = input ("Choice\n" \
                          "1 - Rational numbers\n" \
                          "2 - Complex numbers\n"  \
                          "3 - Exit\n")
        match item:
            case "1":
                logging.info('Start program')
                menu_calc1(item)
            case "2":
                menu_calc2(item)
            case "3":
                logging.info('Stop program')
                break #не срабатывает почему-то после возвращения из вложенного меню
            case _:
                logging.error('Incorrect menu selection')
                print('Incorrect menu selection')


def menu_calc1(item):
    while True:
        if item == "1":
            logging.info("Rational numbers are selected")
            print("Calculator menu for rational numbers:")
            item2 = input("Select operation\n" \
                          "1 - sum (+)\n" \
                          "2 - sub (-)\n" \
                          "3 - mul (*)\n" \
                          "4 - div (/)\n" \
                          "5 - integar div (//)\n" \
                          "6 - remainder div (%)\n" \
                          "7 - main menu\n")  
            match item2:
                case "1":
                    logging.info("sum (+) selected")
                    a, b = rational_data()
                    print(f"result = {sum(a, b)}")
                    #pause()
                case "2":
                    logging.info("sub (-) selected")
                    a, b = rational_data()
                    print(f"result = {sub(a, b)}")
                case "3":
                    logging.info("mul (*) selected")
                    a, b = rational_data()
                    print(f"result = {mul(a, b)}")
                case "4":
                    logging.info("div (/) selected")
                    a, b = rational_data()
                    check_zero_div(a, b, 1)
                    #print(f"result = {div(a, b)}")
                case "5":
                    logging.info("integar div (//) selected")
                    a, b = rational_data()
                    check_zero_div(a, b, 2)
                    #print(f"result = {div_op(a, b)}")
                case "6":
                    logging.info("remainder div (%) selected")
                    a, b = rational_data()
                    check_zero_div(a, b, 3)
                    #print(f"result = {div_os(a, b)}")
                case "7":
                    menu()
                case _:
                    logging.info("Incorrect menu selection")
                    print("Incorrect menu selection")

def menu_calc2(item):
    while True:
        if item == "2":
            logging.info("Complex numbers are selected")
            print("Calculator menu for complex numbers:")
            item2 = input("Select operation\n" \
                          "1 - sum (+)\n" \
                          "2 - sub (-)\n" \
                          "3 - mul (*)\n" \
                          "4 - div (/)\n" \
                          "5 - main menu\n")  
            match item2:
                case "1":
                    logging.info("sum (+) selected")
                    a, b = complex_data()
                    print(f"result = {sum(a, b)}")
                case "2":
                    logging.info("sub (-) selected")
                    a, b = complex_data()
                    print(f"result = {sub(a, b)}")
                case "3":
                    logging.info("mul (*) selected")
                    a, b = complex_data()
                    print(f"result = {mul(a, b)}")
                case "4":
                    logging.info("div (/) selected")
                    a, b = complex_data()
                    check_zero_div(a, b, 1)
                    #print(f"result = {div(a, b)}")
                case "5":
                    menu()
                case _:
                    logging.info("Incorrect menu selection")
                    print("Incorrect menu selection")

#---------
def rational_data():
    while True:
        try:
            a, b = (float(input("Enter a: ")), float(input("Enter b: ")))
        except ValueError:
            print("Incorrect input. Enter a digit!")
            logging.error("Incorrect user input!")
            continue
        else:
            return a, b

def complex_data():
    while True:
        try: 
            act_a, imag_a = (float(input("Enter actual part for a: ")), float(input("Enter imaginary part for a: ")))
            num1 = complex(act_a, imag_a)
            print(num1)
            act_b, imag_b = (float(input("Enter actual part for b: ")), float(input("Enter imaginary part for b: ")))
            num2 = complex(act_b, imag_b)
            print(num2)
        except ValueError:
            print("Incorrect input. Enter a digit!")
            logging.error("Incorrect user input!")
            continue
        else:
            return num1, num2




