def calc():
    # x = 9
    # y = 5
    def add(x,y):
        z = x + y
        return z

    def sub(x,y):
        z = x - y
        return z
    return add, sub

add,sub = calc()
print(add(4,5),sub(7,4))
