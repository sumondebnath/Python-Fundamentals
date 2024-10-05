
students_dict = {
    "students" : ["sumon", "manu", "deb", "nath", "sanju"],
    "scores" : [13, 15, 17, 19, 11]
}

for (keys, values) in students_dict.items():
    print(keys," : ", values)

    for val in values:
        print(val)