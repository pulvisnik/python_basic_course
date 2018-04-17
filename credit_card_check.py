import re

def holder_check(holder):
    holder_name_has_error = re.match(r'^[a-zA-Z]+\ [a-zA-Z]+$', holder)
    if holder_name_has_error:
        return True

def card_check(card_num):
    card_has_error = re.match(r'(^[0-9]{4}\ [0-9]{4}\ [0-9]{4}\ [0-9]{4}$)', card_num)
    if card_has_error:
        return True

def bank_check(card_num):
    if card_num.startswith('5167'):
        print("You use PrivatBank card\n")
    elif card_num.startswith('5375'):
        print("You use Monobank credit card\n")
    else:
        print("You use credit card from unknown bank\n")

def exp_date_check(exp_date, current_year):
    exp_date_has_error = re.match(r'(^[0-9]{2}\/[0-9]{2}$)', exp_date)
    exp_date_list = exp_date.split('/')
    if exp_date_has_error and int(exp_date_list[1]) >= current_year and int(exp_date_list[0]) >= 1 and int(exp_date_list[0]) <= 12:
        return True

def check_cvv_code(cvv_code):
    cvv_code_has_error = re.match(r'^[0-9]{3}$', cvv_code)
    if cvv_code_has_error:
        return True