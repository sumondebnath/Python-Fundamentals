import pandas


students_dict = {
    "students" : ["sumon", "manu", "deb", "nath", "sanju"],
    "scores" : [13, 15, 17, 19, 11]
}

students_data = pandas.DataFrame(students_dict)
# print(students_data)

for (index, row) in students_data.iterrows():
    print(row)
    print(row.students)
    print(row.scores)