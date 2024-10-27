# def increment(x):
#     return x + 1

# print(increment)

# print(increment(4))

# print(increment(411.3838))

plus_one = lambda x: x + 1

print(plus_one)

print(plus_one(6))

print(plus_one(101.3))

multiply_by_10 = lambda a: a * 10

print(multiply_by_10)

print(multiply_by_10(23))

print(multiply_by_10(1.567333300000000001))

def do_math(a, b, math_fn):
    return math_fn(a, b)


# Define a lambda function
add_lambda = lambda x, y: x + y

# Use the do_math function with the lambda as math_fn
result = do_math(5, 3, add_lambda)

print(result)

print(do_math(45, 23.2222, lambda a, b: a / b))


print(do_math(4, 55, lambda a, b: a - b))

print(do_math(4, 55, lambda a, b: a ** b))

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = tuple(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
