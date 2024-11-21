# example 1: logging to console

# import logging

# def add_numbers(num_1, num_2):
#     res = num_1 + num_2
#     logging.info(f"The sum is {res}")
#     return res

# print("Example 1: {}\n".format(add_numbers(1, 2)))

## example 2: logging to file

# import logging

# logging.basicConfig(
#     filename="logs.log", 
#     level=logging.INFO
# )

# def add_numbers(num_1, num_2):
#     res = num_1 + num_2
#     logging.info(f"The sum is {res}")
#     return res

# print("Example 2: {}\n".format(add_numbers(2, 3)))

## example 3: logging to file using different levels: DEBUG, WARN, ERROR

import logging

logging.basicConfig(
    filename="logs.log", 
    level=logging.WARN # change flag to your respective level
)

def add_numbers(num_1, num_2):
    res = num_1 + num_2
    # implement your code here
    logging.warn("This is not a warning!")
    return res

print("Example 3: {}\n".format(add_numbers(2, 3)))
