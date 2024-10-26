"""
    This is the own error exception Raise.
    
"""

height = float(input("Enter a value type is meter: "))
weight = int(input("Enter a value type is KG: "))

if height > 4:
    raise ValueError("This height very far long.")

bmi = weight / height ** 2

print(bmi)