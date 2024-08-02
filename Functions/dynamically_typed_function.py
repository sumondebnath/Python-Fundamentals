

def some_add(a, b):
    return a+b


add_dic = {
    "+" : some_add
} 

add = add_dic['+']

print(add(10, 20))