# squares = []
# for x in range(11):
#     if x % 2 == 0:
#         squares.append(x**2)
#         print(squares)
#         print(x)

# squares = [x**2 for x in range(1,11)]
# print(squares)

# numbers = [1, 2, 3, 4, 5]

# squares = [x**2 for x in numbers]

# print(squares)


# car_makes = ["Toyota", "Honda", "Ford", "Chevrolet", "BMW"]

# print(car_makes)

# car_makes_copy = []

# for car_make in car_makes:
#     car_makes_copy.append(car_make)
#     print(car_makes_copy)
    
    
# car_makes_copy[1] = "Rzyguli"

# print(f"Original: {car_makes}")
# print(f"Copy:     {car_makes_copy}")

# car_makes_copy = [car_make for car_make in car_makes]
# print(car_makes_copy)

# car_makes_copy[1] = "Skodilak"

# print(f"Origina;: {car_makes}")
# print(f"Copy    : {car_makes_copy}")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = [number for number in numbers if number % 2 == 0]

# print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# even_numbers = {number for number in range(11) if number % 2 == 0}

# print(even_numbers)  # Output: {0, 2, 4, 6, 8}

# countries = ["United States", "Canada", "Mexico", "United States", "Australia", "New Zealand"]

# uppercase_countries = {country.upper() for country in countries}

# print(uppercase_countries)  # Output: {'AUSTRALIA', 'CANADA', 'MEXICO', 'NEW ZEALAND', 'UNITED STATES'}


# names = ["James", "Julie", "Greg", "Sara"]
# departments = ["Engineering", "Operations", "Sales", "Marketing"]

# combined =  [(name, department) for name in names for department in departments]

# print(combined)


names = ["James", "Julie", "Greg", "Sara"]
departments = ["Engineering", "Operations", "Sales", "Marketing"]

combined =  [(name, department) for name, department in zip(names, departments)]

print(combined)

original = {
    "Zoey": 75000,
    "Ursula": 83000,
    "Richard": 6500,
    "Timmy": 45000
}

print(original)
flipped = {value: key for key, value in original.items()}

print(flipped)



