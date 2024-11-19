# Создание списка
# Использование функции list()
users = list()
# Использование литерала []
users_1 = ["A", "B", "C"]
# A = [0, 0]
# B = [1, -2]
# C = [2, -1]
# Доступ к элементам списка
users_2 = ["Dima", "Vova", "Elena"]
print(users_2[0])
print(users_2[-1])
print(users_2[1])

# добавление элемента в список
users_2.append("Olga")

# расширение списка элементами другого списка
users_2 += ["Sasha", "Masha"]
users_2.extend(["Natasha", "Sveta"])

# добавление элемента в произвольное место
users_2.insert(0, "Zero")
users_2.insert(-1, "Last")
users_2.insert(len(users_2), "Last!!!")
print(users_2)

# Получение количества элементов списка
print(len(users_2))

# pop - удалить элемент и получить его
element = users_2.pop(0)
print(element)
print(users_2)

# count - подсчёт количество раз, которые элемент появляется в списке
print(users_2.count("Sasha"))

# Получение индекса элемента по его значению (первого, которого нашёл)
# users_2.remove("Sasha")
print(users_2)
print(users_2.index("Sasha"))

# clear - очищение списка
# users_2.clear()
# print(users_2)

users_3 = [1,2,3,4]
print(users_2 + users_3)

# in - оператор для проверки вхождения элемента в список
name = "Sasha"
if name in users_2:
    print("Ok")
else:
    print("not found")