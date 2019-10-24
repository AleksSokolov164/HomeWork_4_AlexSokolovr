def print_who(name):
    print(name)

print_who('Max')

p = print_who('Max')
print_who(p)

p=print_who
print_who(p)
p('Leon')

def kvadro_function(variable, func):
    func(variable)

kvadro_function('Mama',p)