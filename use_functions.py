"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета personal account
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное менюп

2. покупка purchase
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок purchase history
 

выводим историю покупок пользователя (название purchase name
 
 и сумму purchase price)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
n_operatin = int(0)  # номер операции со счетом
operatin = 'нет операций'  # описание операции со счетом
debit = float(0)  # приход по счету пользователя
credit = float(0)  # расход по счету пользователя
total = float(0)  # сумма на счету пользователя
purchase_history = [[n_operatin, operatin, debit, credit, total], ]  # история покупок
total_debit = float(0)
total_credit = float(0)
def separator(simbol, count):
    k = simbol * count
    print(k)
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. снятие наличных')
    print('5. выход')
    choice = input('Выберите пункт меню ')
    if choice == '1':
        n_operatin = n_operatin + 1  # номер операции со счетом
        operatin = 'зачисление '  # описание операции со счетом
        debit = float(input('Ввудите сумму пополнения счета: '))  # приход по счету пользователя
        credit = float(0)  # расход по счету пользователя
        total = total + debit  # сумма на счету пользователя
        purchase_history.append([n_operatin, operatin, debit, credit, total])
        total_debit = total_debit+debit
    elif choice == '2':
        debit = float(0)  # приход по счету пользователя
        credit = float(input('Введите цену покупки: '))  # расход по счету пользователя
        if credit > total:
            print('У Вас недостаточно средств на счете') # проверка на платежеспособность
        else:
            operatin = input('Введите название покупки: ')  # описание операции со счетом
            total = total - credit  # сумма на счету пользователя
            n_operatin = n_operatin + 1  # номер операции со счетом
            purchase_history.append([n_operatin, operatin, debit, credit, total])
            total_credit = total_credit+credit
    elif choice == '3':
        width_n_operatin = 5  # ширина столбца - номер операции со счетом
        width_operatin = 20   # ширина столбца -описание операции со счетом
        width_debit = 10  # ширина столбца -приход по счету пользователя
        width_credit = 10  # ширина столбца -расход по счету пользователя
        width_total = 10  # ширина столбца -сумма на счету пользователя
        print('N      операция              приход      расход      итог ')
        separator('*', 60)
        for i in purchase_history:
            tail_width_n_operatin = ' '*(width_n_operatin-len(str(i[0]))) # выравнивание по сроке - номер операции со счетом
            tail_width_operatin = ' '*(width_operatin- len(i[1]))  # выравнивание по сроке -описание операции со счетом
            tail_width_debit = ' '*(width_debit-len(str(i[2])))  # выравнивание по сроке -приход по счету пользователя
            tail_width_credit = ' '*(width_credit-len(str(i[3])))  # выравнивание по сроке -расход по счету пользователя
            tail_width_total = ' '*(width_total-len(str(i[4])))  # выравнивание по сроке -сумма на счету пользователя
            print(f'{i[0]} {tail_width_n_operatin} {i[1]} {tail_width_operatin} {i[2]} {tail_width_debit} '
                   f'{i[3]} {tail_width_credit} {i[4]} {tail_width_total} ')
            separator('-', 60)
        print(f'       ИТОГО                 {total_debit}         {total_credit}         {i[4]} ')
    elif choice == '4':
        debit = float(0)  # приход по счету пользователя
        credit = float(input('Введите сумму для снятия: '))  # расход по счету пользователя
        if credit > total:
            print('У Вас недостаточно средств на счете') # проверка на платежеспособность
        else:
            operatin = 'выдача наличных '  # описание операции со счетом
            total = total - credit  # сумма на счету пользователя
            n_operatin = n_operatin + 1  # номер операции со счетом
            purchase_history.append([n_operatin, operatin, debit, credit, total])
            total_credit = total_credit+credit
    elif choice == '5':
        break
    else:
        print('Неверный пункт меню')
