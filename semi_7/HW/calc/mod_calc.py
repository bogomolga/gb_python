from logg import logging

def sum(a, b):
    logging.info(f"sum (+): {a} + {b} = {a + b}")
    print(f"sum (+): {a} + {b}")
    return a + b

def mul(a, b):
    logging.info(f"mul (*): {a} * {b} = {a * b}")
    print(f"mul (*): {a} * {b}")
    return a * b

def div(a, b):
    logging.info(f"div (/): {a} / {b} = {a / b}")
    print(f"div (/): {a} / {b}")
    return a / b

def sub(a, b):
    logging.info(f"sub (-): {a} - {b} = {a - b}")
    print(f"sub (-): {a} - {b}")
    return a - b

def div_op(a, b):
    logging.info(f"div_op (//): {a} // {b} = {a // b}")
    print(f"div_op (//): {a} // {b}")
    return a // b

def div_os(a, b):
    logging.info(f"div_os (%): {a} % {b} = {a % b}")
    print(f"div_os (%): {a} % {b}")
    return a % b