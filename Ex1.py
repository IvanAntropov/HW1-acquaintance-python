# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def Input_values(write_what_you_want):
    for_checking = False
    while not for_checking:
        try:
            number = int(input(f'{write_what_you_want}'))
            if number > 7 or number < 1:
                for_checking = False
                print("Try again. You must enter the number of the day.")
            else:
                for_checking = True
        except ValueError:
            print("Try again. You must enter the number of the day.")
    return number


number_for_check = Input_values('Enter the number = ')
if number_for_check == 6 or number_for_check == 7:
    print(f'{number_for_check} -> weekend')
else:
    print(f'{number_for_check} -> weekdays')
