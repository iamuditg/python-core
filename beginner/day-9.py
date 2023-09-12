# Dictionary
programming_dictionary = {
    "Bug": "Bug is Bug",
    "Function": "Function is func"
}

print(programming_dictionary["Bug"])

# Adding new entry to dictionary.
programming_dictionary["loop"] = "loop is loop"

print(programming_dictionary)

# empty dictionary
empty_dictionary = {}
empty_dictionary = programming_dictionary
programming_dictionary = {}
print(programming_dictionary)
print(empty_dictionary)
empty_dictionary["loop"] = "new loop text"
print(empty_dictionary)

for key in empty_dictionary:
    print(key)
    print(empty_dictionary[key])

student = {
    "anil": 80,
    "prokasj": 90,
    "Draco": 70,
    "Neville": 62,
    "Udit": 87
}

student_grades = {}
for key in student:
    score = student[key]
    if score > 75:
        student_grades[key] = score

print(student_grades)

# Nesting lists and dictionary
capitals = {
    "france": "Paris",
    "Germany": "Berlin"
}
print(capitals)
travel_log = {
    "france": ["Paris","lille"],
    "Germany": ["Berlin","Hamburg"]
}
print(travel_log)
travel_log_dict = {
    "france": {"cities": ["Paris","lille"]},
    "Germany": ["Berlin","Hamburg"]
}
print(travel_log_dict)