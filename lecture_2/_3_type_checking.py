## example 1

import logging

def log_result(variable):
    if isinstance(variable, str):
        logging.debug("Variable is a string.")
    elif isinstance(variable, int):
        logging.debug("Variable is an integer.")
    elif isinstance(variable, float):
        logging.debug("Variable is a float.")
    return variable

log_result("hello cruel world")

## example 2

import logging

def log_result(variable):
    if variable is None:
        logging.debug("Variable is None.")
    elif isinstance(variable, str):
        logging.debug("Variable is a string.")
    return variable

my_var = None

log_result(my_var)

## example 3

import logging

def log_result(variable):
    if callable(variable):
        logging.debug("Variable is a function.")
    elif variable is None:
        logging.debug("Variable is None.")
    elif isinstance(variable, str):
        logging.debug("Variable is a string.")
    return variable

def greet():
    print("hello world")

log_result(greet)

## example 4

# implement your code
# throw an AssertionError using assert
# if val_1 or val_2 is not an integer

# hint: assert isinstance(sth, type)

def add_integers(val_1, val_2):
    # your code here
    # :)
    # ;)
    assert isinstance(val_1, int)
    assert isinstance(val_2, int)
    return val_1 + val_2

print(add_integers(2, "2"))
