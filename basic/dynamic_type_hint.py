# name : str
# age : int
# height : float
# is_human : bool

def check_Adult(age : int)->None:
    if age >= 18:
        return True
    else :
        return False
    


if check_Adult(18):
    print("You are Adult!")
else:
    print("You are Child!")