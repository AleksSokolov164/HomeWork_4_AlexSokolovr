# def multipication(x,y):
#    result = x*y
#    return result

def multipication(*args):
    result = 1
    for number in args:
        result = result * number
    return result


print(multipication(2, 3,6))
print(multipication(3, 4, 5))
