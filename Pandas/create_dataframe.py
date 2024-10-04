import pandas

data_dict = {
    "students" : ["Sumon", "Manu", "Sanju"],
    "scores" : [13, 33, 23]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("./Pandas/new_data.csv")