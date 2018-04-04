#Не работает функция импорт в самом Pycharm (Самому по помощи оверфлоу фиксить стремно)
global bank_id

def credit_card_check():
    while True:
        card_num = input("Enter your credit card number, #### #### #### ####")
        is_error = 0  # если будет ошибка при вводе номера карты- запишем в эту переменную 1
        # Если ввели меньше или больше 19 символов - ошибка!
        if len(card_num) != 19:
            is_error = 1
            print('Error: 19 symbols please')
        # Разбиваем строку по пробелам
        else:
            try:
                card_num_list = card_num.split(' ')
                if len(card_num_list) != 4:  # если после разбивки получили не 4 элемента - ошибка!
                    is_error = 1
                    print('Error: Like credit card please')
                else:  # проверим длину элементов списка
                    for el in card_num_list:
                        if len(el) != 4:  # если длина элементов списка не равна 4 - ошибка!
                            is_error = 1
                            print('Error: Its okay. Just try harder')
                            break
                        else:  # проверим, являются ли элементы списка числами
                            try:
                                number = int(el)
                            except ValueError:
                                print('Error: Integers please')
                                is_error = 1
            except ValueError:
                is_error = 1
                print('Error: Not like this')

        if is_error == 1:  # если была ошибка - продолжаем цикл
            continue
        else:  # иначе - переходим на следующий этап
            bank_id = card_num_list[0]
            print('Your card number is valid!')
            break




def date_check():
    while True:
        card_date = input('Enter card date, MM/YY')
        is_error = 0

        if len(card_date) != 5:
            is_error = 1
        else:
            try:
                card_date_list = card_date.split('/')
                if len(card_date_list) != 2:
                    is_error = 1
                else:
                    for ind, el in enumerate(card_date_list):
                        if len(el) != 2:  # если длина элементов списка не равна 2 - ошибка!
                            is_error = 1
                            # print('Error 2')
                            break
                        else:  # проверим, являются ли элементы списка числами
                            try:
                                number = int(el)
                                if ind == 0:
                                    if number < 1 or number > 12:
                                        is_error = 1
                                        print('Error: wrong month!')
                                        break
                                else:
                                    if number < 18:
                                        is_error = 1
                                        print('Error: wrong year!')
                                        break
                            except ValueError:
                                # print('Error 3')
                                is_error = 1
            except ValueError:
                is_error = 1

        if is_error == 1:  # если была ошибка - продолжаем цикл
            continue
        else:  # иначе - переходим на следующий этап
            print('Card date is valid!')
            break



def cvv_check():
    while True:
        cvv_code = input("Enter your CVV code")
        is_error = 0

        if len(cvv_code) != 3:
            is_error = 1
            print("Error: Only 3 symbols pls")
        else:
            try:
                number = int(cvv_code)
                if number < 0 or number > 999:
                    print("Error: Wrong numbers")
                    is_error = 1
            except ValueError:
                print('Error: Integers please')
                is_error = 1

        if is_error == 1:  # если была ошибка - продолжаем цикл
            continue
        else:  # иначе - переходим на следующий этап
            print('CVV is valid!')
            break



def bank_check():
    if bank_id == '5167':
        print("You're using Privat Bank credit card")
    elif bank_id == '5375':
        print("You're usiing Monobank credit card")
    else:
        print("You're using unknown bank credit card")
    print("hahaha I've got your credit card!!!")


credit_card_check()
date_check()
cvv_check()
bank_check()