# Словарь определяется функцией dict или литералом []
# словарь хранит данные в формате ключ: значение
from sys import orig_argv

mydict = dict()

person = {}
person_2 = {"name": "Elena", "age": 26}

# получение элемента словаря Имя_словаря[ключ]
print(person_2["name"])

# добавление элемента в словарь ИМЯ_СЛОВАРЯ[КЛЮЧ]=ЗНАЧЕНИЕ
person_2["phone"] = "217361761378"
print(person_2)

person_2["age"] = 45
print(person_2)

print(len(person_2))
person_2["language"] = {"main": "Русский", "other": "English"}
person_2["age"] = ["376376231", "768947893457", "7894798345"]

print(person_2)

person_2[100] = ["376376", "76894789", "789479834"]
print(person_2)

print(person_2.keys())
print(list(person_2.keys())[0])
print(list(person_2.values()))

for key in person_2:
    print(key, person_2[key])

for item in person_2.items():
    print(item)

for key, value in person_2.items():
    print(f"key - {key}, value - {value}")

print(len(person_2))
print(person_2.get("hghhhj", "404"))
age = person_2.pop("age")
print(age)
print(person_2)

del person_2[100]
print(person_2)
person_1 = person_2.copy()

print(id(person_1))
print(id(person_2))
person_2["NEW"] = "NEW"
print(person_2)
print(person_1)

print(person_2.popitem())
print(person_2.popitem())

a = {}.fromkeys([1,2,3], ["a", "b", "c"])
print(a)

# x=5
# y=6
# x,y = y,x
# print(x)
# print(y)
#
# name, age = ("Sasha", 25)
# print(name)
# print(age)

month_dict = {}
month = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in month:
    month_dict[i] = f"month - {i}"

print(month_dict)

info = {}
users_info = []
N = 3

for i in range(N):
    print(f"Enter {i+1} user's info)

    name = input("Enter the name: ")
    age = input("Enter the age: ")
    phone = input("Enter the phone number: ")
    info = {
        "name": name,
        "age": age,
        "phone": phone
           }
    users_info.append(info)

print(users_info)