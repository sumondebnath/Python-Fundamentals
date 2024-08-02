

def docStrings(first_name, last_name):
    a = """
    This is the fuction and using the docstring and explore the thinks how to work and how to
    print that and how to declear this thinks.
    this concept in the theory.txt explain as well.
    """

    name_one = first_name.title()
    name_two = last_name.title()

    print(f"{name_one} {name_two}")
    return a


print(docStrings("SumoN", "debNaTH"))