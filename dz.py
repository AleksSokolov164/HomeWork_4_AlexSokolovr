d = {
    '1': 1,
    '2': 1,
    '3': 2
    }
keys = []
for k, v in d.items():
    if v==1:
        keys.append(k)
print (keys)