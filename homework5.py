# Домашнее задание на тему "Неизменяемые и изменяемые объекты. Кортежи"

immutable_var = (1, 2, 'help', 'little', 5, 6)
print(immutable_var)
# immutable_var[1] = 20 - код ошибки - "TypeError: 'tuple' object does not support item assignment"
# "Элементы кортежа не подвергаются изменению,
# исключения если в кортеже находится список ( эти элементы изменить можно )



mutable_list = [1, 2, 'first', 'day']
mutable_list.append(25)
mutable_list.remove(1)
mutable_list.extend(['blood', 'egg'])
print(mutable_list)