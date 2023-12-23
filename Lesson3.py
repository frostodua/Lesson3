# У всіх завданнях використовувати обробку винятків
#
# 1. Користувач вводить із клавіатури номер дня тижня (1-7).
# Необхідно вивести на екран назви дня тижня.
# Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.
#
# 2. Користувач вводить два числа.
# Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання
#
# 3. Користувач вводить два числа та матем дію: + - * або /
# Залежно від введеної матем дії вивести результат

#1
try:
    numday = int(input("Введіть номер дня тижня від 1 до 7\n"))
    if numday == 1:
        print("Понеділок")
    elif numday == 2:
        print("Вівторок")
    elif numday == 3:
        print("Середа")
    elif numday == 4:
        print("Четвер")
    elif numday == 5:
        print("П'ятниця")
    elif numday == 6:
        print("Субота")
    elif numday == 7:
        print("Неділя")
    else:
        print("Помилка, введіть цифри від 1 до 7")
except ValueError as error:
    print("Введіть цифри, будь ласка!")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print("Гарного дня!")

#2
try:
    num1 = int(input("Введіть перше число\n"))
    num2 = int(input("Введіть друге число\n"))
    if num1 == num2:
        print()
    else:
        if num1 < num2:
            print(num1,num2)
        else:
            print(num2,num1)
except ValueError as error:
    print("Введіть цифри, будь ласка!")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print("Гарного дня!")

#3
try:
    A = int(input("Введіть перше число "))
    B = int(input("Введіть друге число "))
    C = str(input("Введіть математичну дію +-*/ "))
    if C == "+":
        result = A+B
        print(f"Сума дорівнює {result}")
    elif C == "-":
        result = A-B
        print(f"Маємо у підсумку {result}")
    elif C == "*":
        result = A*B
        print(f"Множення дорівнює {result}")
    elif C == "/":
        result = A/B
        print(f"Поділ дорівнює {result}")
    else:
        print("Введіть математичні дії, будь ласка!")

except ZeroDivisionError as error:
    print(f"Ділення на нуль: {error}")
except ValueError as error:
    print("Вводіть цифри, будь ласка!")
    print(f"ValueError: {error}")
except Exception as error:
    print(f"Exception occurred: {error}")
finally:
    print("Гарного дня!")







