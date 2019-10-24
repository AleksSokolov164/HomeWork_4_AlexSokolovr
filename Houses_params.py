def print_roof():
    print('   /\\   ')
    print('  /  \\  ')
    print(' /    \\ ')
    print('-' * 8)
def print_walls(k,wall_symbol='|'):
    for i in range(k):
        print(f'{wall_symbol}     {wall_symbol}')
    print('_' * 8)
def print_hous(k,wall_symbol='/'):
    print_roof()
    print_walls(k,wall_symbol)

print_walls(2)
print_roof()

b = 3
for i in range(2):
    print_hous(b)
