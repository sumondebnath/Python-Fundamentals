import json


name = input("Name: ")
status = input("Gender: ")
age = int(input("Age: "))

new_data = {
    name : {
        "gender" : status,
        "age" : age
    }
}

with open("/home/sumon/Documents/Python/Json/data.json", "w") as json_file:
    json.dump(new_data, json_file, indent=4)                    # Create or Write a Json File.


with open("/home/sumon/Documents/Python/Json/data.json", "r") as json_file:
    data = json.load(json_file)                                 # Read a Json File

    # Update a json file with new data
# json_file.update(new_data)

    # Save a json file with new data to old_data.
# json.dump(new_data, old_data)


print(data)