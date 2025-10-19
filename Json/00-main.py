import json
from pathlib import Path


name = input("Name: ")
status = input("Gender: ")
age = int(input("Age: "))

new_data = {
    name : {
        "gender" : status,
        "age" : age
    }
}

file_path  = Path(__file__).parent / "data.json"

with open("/home/sumon/Documents/Python-Fundamentals/Json/data.json", "w") as json_file:
    json.dump(new_data, json_file, indent=4)                    # Create or Write a Json File.


with open("/home/sumon/Documents/Python-Fundamentals/Json/data.json", "r") as json_file:
    data = json.load(json_file)                                 # Read a Json File



# with open("file_path", "w") as json_file:
#     json.dump(new_data, json_file, indent=4)                    # Create or Write a Json File.


# with open("file_path", "r") as json_file:
#     data = json.load(json_file)                                 # Read a Json File





    # Update a json file with new data
# json_file.update(new_data)

    # Save a json file with new data to old_data.
# json.dump(new_data, old_data)


print(data)