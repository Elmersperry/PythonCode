def hello():
    print("Hello")

def bye():
    print("Bye")

hello()
bye()

# сигнатура функции - имя и параметры
def print_info(name, lastname, age, city):
    info = {
        "name": name,
        "lastname": lastname,
        "age": age,
        "city": city
    }
    return(info)

user_name = "Dmitriy"
user_lastname = "Ivanov"
user_age = 32
user_city = "Moscow"

# позиционные аргументы
print_info(user_name, user_lastname, user_age, user_city)
# именованные аргументы
print_info(city=user_city, age=user_age, name=user_name, lastname=user_lastname)
# при указании в параметрах функции значения по умолчанию, при неуказании аргумента выводится дефолтное значение

result = print_info(city=user_city, age=user_age, name=user_name, lastname=user_lastname)
print(result)

# def print_name(name):
#     print(name)
# name = "Masha"
# print_name("Maxim")
# print(name)
# print(name=name)
# print(name=last_name)