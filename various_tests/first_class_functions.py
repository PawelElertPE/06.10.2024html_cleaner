# def is_strong_password(password):
#     """Returns True if the password is strong.Otherwise False.
    
#     Args:
#     password: A string representing the password to be checke.
    
#     Returns:
#     A boolean value indicating whether the password is strong.
#     """
    
#     if len(password) < 8:
#         return False
    
#     if not any(c.isupper() for c in password):
#         return False
    
#     if not any(c.islower() for c in password):
#         return False
    
#     if not any(c.isdigit() for c in password):
#         return False
    
#     if not any(c in "!@#$%^&*()" for c in password):
#         return False
    
#     return True

# print(is_strong_password)

# print(is_strong_password("P@ssword1234#"))

# validate_password = is_strong_password

# print(validate_password("Password1234*^"))

# print(validate_password)


def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1 / num_2

# def do_math(a, b, math_fn):
#     return math_fn(a, b)

# print(do_math(2, 3, add))


# print(do_math(12, 23.3, subtract))

def get_arithmetic_function(operator):
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    if operator in operations:
        return operations[operator]
    else:
        raise ValueError("Invalid operator")
    
fn = get_arithmetic_function("+")

print(fn)

print(fn(1.3, 217.00001))


fn = get_arithmetic_function("*")
print(fn)

print(fn(4.1, 3))