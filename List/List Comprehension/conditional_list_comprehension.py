"""
    *** Syntax ***

    newlist = [expression for item in iterable if condition == True]

    or 

    new_list = [new_item for item in list if test]

"""


names = ["sumon", "manu", "deb", "nath", "sanju", "console", "debuger"]

short_list = [name.upper() for name in names if len(name) < 5]

print(short_list)