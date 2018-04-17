import datetime
from credit_card_check import card_check
from credit_card_check import exp_date_check
from credit_card_check import check_cvv_code
from credit_card_check import bank_check
from credit_card_check import holder_check
while True:
    holder_name = input("Enter your Name and Surname (Vasya Pupkin) :\n")
    if holder_check(holder_name) == True:
        break
    else:print("Wrong Holder name!")

while True:
    card_num = input("Enter your card number in format 1111 1111 1111 1111:\n")
    if card_check(card_num) == True:
        break
    else:print("Wrong card number!")

bank_check(card_num)

now = datetime.datetime.now()
current_year = now.year - 2000
while True:
    exp_date = input("Enter expiration date:\n")
    if exp_date_check(exp_date, current_year) == True:
        break
    else:print("Wrong exp date!")


while True:
    cvv_code = input("Enter your CVV code:\n")
    if check_cvv_code(cvv_code) == True:
        break
    else:print("Wrong CVV code!!!")

print("Your credit card information:\n")
print(holder_name.upper())
print(card_num)
print(exp_date)
print(cvv_code)