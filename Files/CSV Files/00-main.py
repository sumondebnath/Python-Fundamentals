with open("/home/sumon/Documents/Python/CSV Files/weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)


import csv

with open("/home/sumon/Documents/Python/CSV Files/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    print(data)
    temp = []
    for val in data:
        print(val[1])
        if val[1] != " temperatures":
            temp.append(int(val[1]))

    print(temp)