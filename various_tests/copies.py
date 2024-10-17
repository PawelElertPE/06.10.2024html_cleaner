# name = "James"

# name_copy = name

# name_copy = "Janice"

# print(f"Name is: {name}")
# print(f"Name copy is: {name_copy}")

# countries_list = ["India", "Pakistan", "China", "Nepal", "Bhutan"]
# print(countries_list)

# countries_list_copy = countries_list
# countries_list_copy[1] = "PAKISTAN"

# print(f"countries_list is: {countries_list}")
# print(f"countries_list_copy copy is: {countries_list_copy}")

import copy
# countries_list = ["USA", "UK", "Franca", "Germany", "Japan"]

# # Create a deep copy of the list
# countries_list_copy = copy.deepcopy(countries_list)

# # Change an element in the copy
# countries_list_copy[1] = "CHINA"

# # Print the original and the copy
# print(countries_list)
# print(countries_list_copy)

# countries_list = ["India", "Pakistan", "China", "Nepal", "Bhutan"]
# countries_list_copy = countries_list.copy()

# countries_list_copy[1] = "PAKISTAN"

# print(f"countries_list is: {countries_list}")
# print(f"countries_list_copy is: {countries_list_copy}")


# countries_list = ["India", ["China", "Nepal"], "Bhutan", "Pakistan"]
# countries_list_copy = countries_list.copy()

# countries_list_copy[1][0] = "CHINA"

# print(f"countries_list is: {countries_list}")
# print(f"countries_list_copy is: {countries_list_copy}")

countries_list = ["India", ["China", "Nepal"], "Bhutan", "Pakistan"]
countries_list_copy = copy.deepcopy(countries_list)

countries_list_copy[1][0] = "CHINA"

print(f"countries_list is: {countries_list}")
print(f"countries_list_copy is: {countries_list_copy}")

student_scores = {
    'Alice': {'math': 90, 'english': 85, 'science': 92},
    'Bob': {'math': 80, 'english': 75, 'science': 88},
    'Charlie': {'math': 95, 'english': 92, 'science': 90}    
}

print(student_scores)

student_scores_copy = copy.deepcopy(student_scores)
student_scores_copy['Alice']['math'] = 100

print(f"Alice's math score in original: {student_scores['Alice']['math']}")
print(f"Alice's math score in copy: {student_scores_copy['Alice']['math']}")

