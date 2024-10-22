# List of names
# import time
# names = ["Alice", "Bob", "Charlie", "Diana","Alice", "Bob", 
#          "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack", "Kate", "Leo", 
#          "Mia", "Noah", "Olivia"]

# # Loop through the list and print each name
# for current_name in names:
#     time.sleep(1)
#     print(current_name)
#     print(time.strftime('%H:%M:%S'))


# import time

# names = ["Alice", "Bob", "Charlie", "Diana", "Alice", "Bob",
#           "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack", "Kate", "Leo",
#           "Mia", "Noah", "Olivia"]

# # Loop through the list and print each name
# for current_name in names:
#     time.sleep(1)
#     print(current_name)
#     print(time.strftime('%H:%M:%S'))

#     # Add a brief description or comment about the current name
#     if current_name == "Alice":
#         print("Alice is the first person on the list.")
#     elif current_name == "Bob":
#         print("Bob is the second person on the list.")
#     elif current_name == "Charlie":
#         print("Charlie is the third person on the list.")
#     else:
#         print("This is a generic message for other names.")


# dog_ages = [
#     ("Oba", 12),
#     ("Moje", 8),
#     ("Nemo", 6),
#     ("Tofu", 2)
# ]

# for dog, age in dog_ages:
#     print("Dog %s is %d years old" % (dog, age))

# dog_ages = [
#     ("Oba", 12),
#     ("Moje", 8),
#     ("Nemo", 6),
#     ("Tofu", 2),
#     ("Brutus", 1.5),
#     ("PI", 3.1415)
# ]

# for dog, age in dog_ages:
#     print(f"Dog {dog} is {age} years old")
    

# student_scores = {
#     "Alice": 95,
#     "Bob": 85,
#     "Charlie": 92,
#     "Diana": 12,
#     "Eve": 98,
#     "Frank": 91,
#     "Tadek": 30
# }

# for student, score in student_scores.items():
#     if score > 90:
#         print(f"{student} scored {score} in math.")
#     else:
#         print(f"{student} scored {score} and has to learn more")   
        
# print(student_scores.items())


# Use a for loop to print numbers from 1 through 5
# for num in range(1, 6):
#     print(num)
    
# my_range = range(10)

# print(my_range)

# list(my_range)
# print(list)

# tuple(my_range)
# print(tuple)

# my_range = range(35)

# print(my_range)

# list_from_range = list(my_range)
# print(list_from_range)

# tuple_from_range = tuple(my_range)
# print(tuple_from_range)

# import time
# for i in my_range:
#     print(i)
#     time.sleep(0.3)
    
for num in range(0, 17, 3):
    print(num)