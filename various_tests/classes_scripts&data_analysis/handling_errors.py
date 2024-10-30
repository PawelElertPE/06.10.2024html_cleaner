#print(hello_world)

#print(f"Result is: {100/0 +3}")

# var_one = "23"
# var_two = 45
# result = var_one + var_two

# result = var_two + var_one

# def add(num1, num2):
#     result = float(num1) + float(num2)
#     print(f"The sum of {num1} and {num2} is {result}")
    
#     return result

# print(add(12, 17.1))

# inp1 = input("Enter the first number: ")

# inp2 = input("Enter the second number: ")

# add(inp1, inp2)
# add(inp1, inp2)


# def add(num1, num2):
#     try:
#         # Attempt to convert inputs to float and add them
#         result = float(num1) + float(num2)
#         print(f"The sum of {num1} and {num2} is {result}")
#         return result
#     except ValueError as e:
#         # Handle the error if inputs cannot be converted to float
#         print("Error: Both inputs must be numbers.")
#         return None
    
# inp1 = input("Enter the first number: ")

# inp2 = input("Enter the second number: ")

# add(inp1, inp2)



def divide(num1, num2):
    try:
        # Prompt user for input
        num1 = float(num1)
        num2 = float(num2)
        
        # Perform the division
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is {result}")
        return result
    except ValueError:
        # Handle cases where inputs are not valid numbers
        print("Error: Both inputs must be valid numbers.")
        return None
    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Cannot divide by zero.")
        return None

# Example usage
inp1 = input("Enter the first number: ")
inp2 = input("Enter the second number: ")

divide(inp1, inp2)

