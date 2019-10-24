"""
МОДУЛЬ 1
В модуле прописаны заготовки для 8 функций
Под каждой функцией есть описание как она должна работать
ниже есть примеры использования функции
Задание: реализовать код функции, чтобы он работал по описанию и примеры использования давали верный результат
"""


def simple_separator(n=10):
     k = '*'*n
     return k

print(simple_separator()=='**********')

def long_separator(count):
     k = '*'*count
     return k

print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True


def separator(simbol, count):
     k = simbol*count
     return k


print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True


def hello_world():
    print('**********')
    print('          ')
    print('Hello World!')
    print('          ')
    print('##########')
hello_world()


def hello_who(who='World'):
    print('**********')
    print('          ')
    print(f'Hello, {who}!' )
    print('          ')
    print('##########')

hello_who()
hello_who('Max')
hello_who('Kate')


def pow_many(power, *args):
    result = 0
    for number in args:
        result = result+number
    result1 = result**power
    return result1

print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100


def print_key_val(**kwargs):
    for k,v in kwargs.items():
        print(k,'-->',v, sep=' ')
print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)



def my_filter(iterable, function):
    result = []
    for i in iterable:
        if function(i):
            result.append(i)
    return result



print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True
