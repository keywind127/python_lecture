## example 1

def divide_number(num_1, num_2):
    try:
        return num_1 / num_2
    except Exception:
        return None
    
print(divide_number(1, 2))

## example 2

import logging

def divide_number(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        logging.error("Division by zero!")
        return None
    
print(divide_number(1, 0))
    
## example 3

import logging

def divide_number(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        logging.error("Division by zero!")
    except TypeError:
        logging.error("Type unsupported!")
    return None

print(divide_number(1, "20"))

## example 4

# implement your code
# and catch the NegativeDivisor Exception
# and log the error

class NegativeDivisor(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)

def divide_number(num_1, num_2):
    try:
        if num_2 < 0:
            raise NegativeDivisor("Negative divisor!")
        return num_1 / num_2
    except ZeroDivisionError:
        logging.error("Division by zero!")
    except TypeError:
        logging.error("Type unsupported!")
    # your code here
    # your code here 
    # :)
    return None

print(divide_number(1, -1))
