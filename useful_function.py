frends = ['max','kate','mars','leo']

result = []
for frend in frends:
    if frend.startswith("k"):
        result.append(frend)

print(result)
def f(x):
    if x.startswith('m'):
        return True
    else:
        return False

result = filter(f,frends) # фильтруем функцией f  множество frends

