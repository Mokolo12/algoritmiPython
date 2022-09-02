def calc():


    operation_type = input("Введите операцию (+, -, / или 0 для выхода): ")

    if operation_type == '0':
        return "Выход"
    else:
        if operation_type in "+-/":
            try:
                num_1 = int(input("ВВедите первое число:" ))
                num_2 = int(input("Введите второе число: "))

                if operation_type == '+':
                    res = num_1 + num_2
                    print(f"Ваш результат {res}")
                    return calc()

                elif operation_type == '-':
                    res = num_1 - num_2
                    print(f"Ваш результат {res}")
                    return calc()

                elif operation_type == '*':
                    res = num_1 * num_2
                    print(f"Ваш результат {res}")
                    return calc()

                elif operation_type == '/':
                    try:
                        res = num_1 / num_2
                    except ZeroDivisionError:
                        print("Деление на ноль невозможно")
                    else:
                        print(f"Ваш результат {res}")
                    finally:
                        return calc()
            except ValueError:
                print("Вы вместо трезначного числа ввели строку. Исправьтесь")
                return calc()

        else:
            print("Введен неверный символ, попробуйте ещё раз")
            return calc()

calc()



