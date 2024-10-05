"""
    *** Syntax ***
        -> For List To Dictionary: 

    new_dict = {new_key : new_value for item in list}

    or,
        -> For Dictionary To Dictionary: 

    new_dict = {new_key : new_value for (key, value) in dict.items()}
    
"""

import random

names = ["sumon", "manu", "deb", "nath", "sanju"]

students_scores = {student : random.randint(1, 100) for student in names}

print(students_scores)