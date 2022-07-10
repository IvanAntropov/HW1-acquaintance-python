# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def Input_values(write_what_you_want):
    for_checking = False
    while not for_checking:
        try:
            number = float(input(f'{write_what_you_want}'))
            if number == 0:
                for_checking = False
                print(
                    'Try again. Number must be != 0. If you wanna enter float number use ".", exampple: 1.25 ')
            else:
                for_checking = True
        except ValueError:
            print(
                'Try again. Number must be != 0. If you wanna enter float number use ".", exampple: 1.25 ')
    return number


def Checking(x, y):
    if x > 0 and y > 0:
        print("It's I quarter")
    elif x < 0 and y > 0:
        print("It's II quarter")
    elif x < 0 and y < 0:
        print("It's III quarter")
    else:
        print("It's IV quarter")


x = Input_values("Enter X: ")
y = Input_values("Enter Y: ")
Checking(x, y)
