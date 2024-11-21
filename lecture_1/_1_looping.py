
my_array = [1, 3, 5, 7, 9]

### example 1: while loop

print("Example 1:")

i = 0
n = len(my_array)

while (i < n):
    print(my_array[i], end=" ")
    i += 1

print("\n")

### example 2: for loop

print("Example 2:")

for i in range(0, len(my_array), 1):
    print(my_array[i], end=" ")

print("\n")

### example 3: for loop

print("Example 3:")

for i in my_array:
    print(i, end=" ")

print("\n")

### example 4: for loop with enumerate

print("Example 4:")

# implement your code here
# print out their indices and values
# like: (0, 1) (1, 3) (2, 5) (3, 7) (4, 9)
for i, x in enumerate(my_array):
    print((i,x), end=" ")

print("\n")
