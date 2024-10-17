empty_dict = {}

empty_dict

empty_dict = dict()
empty_dict

type(empty_dict)

student_math_scores = {
    'James': 89,
    'Nora': 55,
    'Janet': 96,
    'Richard': 43
}

student_math_scores

student_math_scores["Nora"]

print(student_math_scores)

student_math_scores["Nora"] = 65

print("student_math_scores")

student_math_scores["Richard"] *= 1.1
print(student_math_scores)

student_math_scores["Julian"] = 72
print(student_math_scores)

student_math_scores["Waclaw"] = "Jest chujem"
print(student_math_scores)

print(student_math_scores.keys())
print(student_math_scores.values())

del student_math_scores["Richard"]
print(student_math_scores)

del student_math_scores["Waclaw"]
print(student_math_scores)

student_info = {
    'James': 89,
    'Nora': 3.4,
    'Janet': [44, 78, 90],
    'Richard': "21, Erden Street, Boston, MA"
}

print(student_info)