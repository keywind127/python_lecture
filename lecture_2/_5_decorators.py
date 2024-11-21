## example 1

def add_consecutive(array):
    result = []
    for i in range(1, len(array)):
        result.append(array[i-1] + array[i])
    return result

def multiply_consecutive(array):
    result = []
    for i in range(1, len(array)):
        result.append(array[i-1] * array[i])
    return result

print(add_consecutive([1, 2, 3, 4]))

print(multiply_consecutive([1, 2, 3, 4]))

## example 2

def for_consecutive(function):
    def funct(array):
        result = []
        for i in range(1, len(array)):
            result.append(function(array[i-1], array[i]))
        return result
    return funct

@for_consecutive
def add_consecutive(val_1, val_2):
    return val_1 + val_2

@for_consecutive
def multiply_consecutive(val_1, val_2):
    return val_1 * val_2

print(add_consecutive([1, 2, 3, 4]))

print(multiply_consecutive([1, 2, 3, 4]))

## example 3

class Utils:
    def for_consecutive(function):
        def funct(self, array):
            result = []
            for i in range(1, len(array)):
                result.append(function(self, array[i-1], array[i]))
            return result
        return funct

    @for_consecutive
    def add_consecutive(self, val_1, val_2):
        return val_1 + val_2

    @for_consecutive
    def multiply_consecutive(self, val_1, val_2):
        return val_1 * val_2

print(Utils().add_consecutive([1, 2, 3, 4]))

print(Utils().multiply_consecutive([1, 2, 3, 4]))

## example 4

# implement your code
# change add_consecutive to classmethod
# and change multiply_consecutive to classmethod 
# ensure the decorators still function correctly

class Utils:
    def for_consecutive(function):
        def funct(self, array): # <- change here
            result = []
            for i in range(1, len(array)):
                result.append(function(self, array[i-1], array[i])) # <- change here
            return result
        return funct

    # <- change here
    @classmethod
    @for_consecutive
    def add_consecutive(cls, val_1, val_2): # <- change here
        return val_1 + val_2

    # <- change here
    @classmethod
    @for_consecutive
    def multiply_consecutive(cls, val_1, val_2): # <- change here
        return val_1 * val_2

print(Utils.add_consecutive([1, 2, 3, 4]))

print(Utils.multiply_consecutive([1, 2, 3, 4]))
