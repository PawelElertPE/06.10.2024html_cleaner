# while True:
#     number = float(input("Enter a number (or enter a negative number to quit): "))

#     if number < 0:
#         print("Goodbye!")
#         break

#     square = number ** 2
#     cube = number ** 3

#     print(f"The square of {number} is {square}.")
#     print(f"The cube of {number} is {cube}.")


country_names = ["Australia", "Brazil", "Canada", "Denmark", "Egypt", "France", "Germany", "Hungary", "India", "Japan"]

for country in country_names:
    if country.startswith("A"):
        continue  # Skip countries starting with "A"
    print(country.upper())
