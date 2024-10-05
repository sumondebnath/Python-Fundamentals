"""
    *** Syntax ***

    new_dict = {new_key : new_value for (key, value) in dict.items() if test }

"""

students_scores = {
    'sumon': 12, 
    'manu': 21, 
    'deb': 42, 
    'nath': 61, 
    'sanju': 48
}

passed_students = {pass_student:student for (pass_student, student) in students_scores.items() if student > 40}

print(passed_students)