
my_list = []
in_num = ''
while in_num != 5:
    in_num = input("Enter your fav. number")
    try:
        int_num = int(in_num)
        my_list.append(int_num)
        if int_num > 100:
            print("your number is more than max")
        elif int_num < 1:
            print("Your number is less than 1")
        else:
            break
    except ValueError:
        my_list.append(in_num)
        print("Not like this")
        print(my_list)
        #not_everything