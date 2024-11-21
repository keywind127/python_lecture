## example 1: simple list comprehension

# result = []
# for i in range(1, 11):
#     result.append(i ** 2)

result = [
    (i ** 2) for i in range(1, 11)
]

print(f"Example 1: {result}\n")

## example 2: nested list comprehension

# result = []
# for i in range(1, 11):
#     for j in range(10):
#         result.append(i ** 2 + j)

result = [
    (i ** 2 + j) for i in range(1, 11)
        for j in range(10)
]

print(f"Example 2: {result}\n")

## example 3: list comprehension with conditioning

# result = []
# for i in range(1, 11):
#     if i % 2:
#         result.append(i)

result = [
    i for i in range(1, 11) if i % 2
]

print(f"Example 3: {result}\n")

## example 4: nested list comprehension with conditioning

# result = []
# for i in range(1, 11):
#     for j in range(10):
#         if j % 2:
#             result.append(i ** 2 + j)

# implement your code here
# :)
# ;)
result = [
    (i ** 2 + j) for i in range(1, 11)
        for j in range(10)
            if j % 2
]

print(result)
