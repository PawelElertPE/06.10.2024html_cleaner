# def say_hello():
#     print("Hello")

# say_hello()

# result = say_hello()
# print(result)

# def return_hello():
#     return "Hello"

# message = return_hello()

# print(message)


# def sum_two_numbers(num1, num2):
#   """Sums two numbers."""
#   return num1 + num2

# # Example usage:
# result = sum_two_numbers(3, 5)

# # The result will contain the sum of the two numbers (3 + 5 = 8)
# print(result)  # Output: 8

# result = sum_two_numbers()
# result


# result = sum_two_numbers(5, 8.8)
# result

# def divide(numerator, denominator):
#     return numerator / 0

# divide(3, 4)

# def find_factors(number):
#   """Finds the factors of a given number."""
#   factors = []
#   for i in range(1, number + 1):
#     if number % i == 0:
#       factors.append(i)
#   return factors

# number = 21
# result = find_factors(number)

# print(result)

# find_factors(102)


def find_factors(number):
  """Finds the factors of a given number.

  Args:
    number: The number whose factors are to be found.

  Returns:
    A list of factors of the given number.
  """
  factors = []
  for i in range(1, number + 1):
    if number % i == 0:
      factors.append(i)
  return factors

find_factors(12)

find_factors
print(find_factors.__doc__)
