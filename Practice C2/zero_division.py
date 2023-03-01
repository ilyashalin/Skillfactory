try:  # Добавляем конструкцию try-except для отлова нашей ошибки
    print("Перед исключением")
    # теперь пользователь сам вводит числа для деления
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b  # здесь может возникнуть исключение деления на ноль
    print(c)  # печатаем c = a / b, если всё хорошо
except ZeroDivisionError as e:  # Добавляем тип именно той ошибки, которую хотим отловить.
    print(e)  # Выводим информацию об ошибке
    print("После исключения")

# print("После исключения")
# try:
#     *ваш код*
# except Ошибка:
#     *Код отлова*
# else:
#     *Код, который выполнится, если в блоке try всё хорошо прошло*
# finally:
#     *Код, который выполнится по-любому*
try:
    print("Перед исключением")
    a = int(input("a: "))
    b = int(input("b: "))
    c = a / b
    print(c)  # печатаем c = a / b, если всё хорошо
except ZeroDivisionError as e:
    print("После исключения")
else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
    print("Всё отлично")
finally:  # код в блоке finally выполнится в любом случае, при выходе из try-except
    print("Finally на месте")

print("После исключения")
#--------------------------------------------------------------------------------------------------------------------
# И конечно же, мы можем вызывать ошибки самостоятельно, с помощью конструкции raise.
age = int(input("How old are you?"))

if age > 100 or age <= 0:
    raise ValueError("Тебе не может быть столько лет")

print(f"Тебе {age} лет!")  # Возраст выводится, только если пользователь ввёл правильный возраст.

raise ValueError("You are too old or don’t exist")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: You are too old or don"t exist

try:
    age = int(input("How old are you?"))

    if age > 100 or age <= 0:
        raise ValueError("Тебе не может быть столько лет")
except ValueError:
    print("Неправильный возраст")

print(f"You are {age} years old!")  # Возраст выводится, только если пользователь ввёл правильный возраст.
#---------------------------------------------------------------------------------------------------------------------
#помещаем код, который может генерировать исключения в блок try
try:
    i = int(input('Введите число:\t'))
#в случае возникновения исключения ValueError выведем соответствующий текст
except ValueError as e:
    print('Вы ввели неправильное число')
#если исключения ValueError не будет то выведем текст, что все в порядке
else:
    print(f'Вы ввели {i}')
#в любом случае, независимо от наличия/отсутствия исключений выполним код
finally:
    print('Мы на выходе')