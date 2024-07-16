

dictionary = {
    "dic1" : [10, 20, 30, 40, 50, 60],
    "dic2" : {
        "one" : 1,
        "two" : 2,
        "three": 3, 
        "four" : 4,
        "five" : 5
    },
    "dic3" : "Sumon Debnath!",
}

dictionary["dic4"] = "hello there, i am here using and learning the python"

print(dictionary)

print(dictionary["dic1"])

for dic in dictionary["dic1"]:
    print(dic)

print(dictionary["dic2"])

for key, val in dictionary["dic2"].items():
    print(key, val)

print(dictionary["dic3"])

print(dictionary["dic4"])