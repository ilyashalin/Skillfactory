# import redis
#
# red = redis.Redis(
#     host='redis-16598.c322.us-east-1-2.ec2.cloud.redislabs.com',  # ваш хост, если вы поставили Редис к себе на локальную машину, то у вас это будет localhost. Если же вы находитесь на Windows, то воспользуйтесь полем host из вашей облачной БД, которую мы создавали в скринкасте.
#     port=16598,  # порт подключения. На локальной машине это должно быть 6379. Для пользователей облачного сервиса порт всегда разный, поэтому его надо копировать оттуда же, что и host.
#     password='acmlSp3oDTLkUZgTpexwmbx49S5uLhfm'  # для локальной машины пароль не требуется (если вы устанавливали Редис к себе на компьютер и не пользовались облачным сервисом из скринкаста выше). Для пользователей облачного сервиса пароль находится в вашей облачной базе данных в поле password
# )
#
# red.set('var1', 'value1')  # записываем в кэш строку "value1"
# print(red.get('var1'))  # считываем из кэша данные
import redis
import \
    json  # так-так-так, кто это тут у нас? Наш старый друг Джейсон заглянул на огонёк! Ну привет, чем ты сегодня нас порадуешь?

red = redis.Redis(
     host='redis-16598.c322.us-east-1-2.ec2.cloud.redislabs.com',  # ваш хост, если вы поставили Редис к себе на локальную машину, то у вас это будет localhost. Если же вы находитесь на Windows, то воспользуйтесь полем host из вашей облачной БД, которую мы создавали в скринкасте.
     port=16598,  # порт подключения. На локальной машине это должно быть 6379. Для пользователей облачного сервиса порт всегда разный, поэтому его надо копировать оттуда же, что и host.
     password='acmlSp3oDTLkUZgTpexwmbx49S5uLhfm'  # для локальной машины пароль не требуется (если вы устанавливали Редис к себе на компьютер и не пользовались облачным сервисом из скринкаста выше). Для пользователей облачного сервиса пароль находится в вашей облачной базе данных в поле password
  )

# dict1 = {'key1': 'value1', 'key2': 'value2'}  # создаём словарь для записи
# red.set('dict1', json.dumps(dict1))  # с помощью функции dumps() из модуля json превратим наш словарь в строчку
# converted_dict = json.loads(
#     red.get('dict1'))  # с помощью знакомой нам функции превращаем данные, полученные из кэша обратно в словарь
# print(type(converted_dict))  # убеждаемся, что мы получили действительно словарь
# print(converted_dict)  # ну и выводим его содержание
#
# red.delete('dict1')  # удаляются ключи с помощью метода .delete()
# print(red.get('dict1'))

cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break