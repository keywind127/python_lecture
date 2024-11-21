
## example 1: simple function

def add(x, y):
    return x + y

print(f"Example 1: {add(1, 3)}")

## example 2: updating global variables

x = 10
def update_x(new_x):
    global x
    x = new_x

update_x(11)

print(f"Example 2: After function call, x = {x}")

## example 3: updating nonlocal variables

def add(a, b):
    c = 10
    def update_c(new_c):
        nonlocal c
        c = new_c
    if a == 0:
        update_c(a)
    return c + a + b

print(f"Example 3: {add(0, 3)}")

## example 4: updating global and nonlocal variables in nested function

global_var = 10

print("Example 4:")

def reset_to_zero():
    # try to make the code work
    # both local variable and global variable should become 0 
    # after calling the nested function
    local_var = 11
    def nested_function():
        nonlocal local_var 
        local_var = 0
        global global_var 
        global_var = 0 
    nested_function()
    print(f"\tLocal variable: {local_var}")

reset_to_zero()

print(f"\tGlobal variable: {global_var}")
