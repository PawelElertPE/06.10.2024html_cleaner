#print(hello_world)

#print(f"Result is: {100/0 +3}")

# var_one = "23"
# var_two = 45
# result = var_one + var_two

# result = var_two + var_one

def add(num1, num2):
    result = float(num1) + float(num2)
    print(f"The sum of {num1} and {num2} is {result}")
    
    return result

print(add(12, 17.1))

inp1 = input("Enter the first number: ")

inp2 = input("Enter the second number: ")

add(inp1, inp2)