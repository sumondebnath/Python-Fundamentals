import pandas

data = pandas.read_csv("/home/sumon/Documents/Python/Pandas/weather_data.csv")
print(data)
print(data["temperatures"])


data_dict = data.to_dict()
print(data_dict)

temp_list = data["temperatures"].to_list()
print(temp_list)

# avarage value
print(data["temperatures"].mean())

# max value
print(data["temperatures"].max())

# Get data in column.
print(data["day"])

print(data.day)

# Get data in row
print(data[data.day == "Monday"])

# Get max temperature row in the data cvs
print(data[data.temperatures == data.temperatures.max()])