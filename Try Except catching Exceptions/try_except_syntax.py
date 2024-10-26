"""
    try : Somthing that might cause an exception.

    except : Do this if was an exception.

    else : Do this if there were not exception.

    finally : Do this no matter what happens. 

"""

try:
    file = open("a_file.txt")

except:
    print("There is an Error!")



# FileNotFoundError

try:
    file = open("/home/sumon/Documents/Python/Try Except catching Exceptions/a_file.txt")
    dic_a = {"key" : "value"}
    print(dic_a["key"])                   # Given a keyError.

except FileNotFoundError:
    file = open("/home/sumon/Documents/Python/Try Except catching Exceptions/a_file.txt", 'w')
    file.write("somethink \n")

except KeyError as error_message:
    print(f"That key {error_message} does not exist.")

else: 
    content = file.read()
    print(content)

finally: 
    file.close()
    print("File also closed.")