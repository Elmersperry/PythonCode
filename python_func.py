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

def text_analyse(text):
    """

    :param text: str
    :return: dict
    """
    stat = {}
    for s in text:
        stat[s] = text.count(s)
    return stat

print(text_analyse(text="hello"))


def text_to_list(text: str):
    return text.split(" ")

print(text_to_list(text="I love python string"))

emails = [
    "admin@mail.ru",
    "alex@yandex.ru",
    "alena@mail.ru",
    "igor@mail.ru"
]

def get_emails(in_emails: list[str], domain: str = ".ru") -> list:
    emails = []
    for email in in_emails:
        if email.endswith(domain):
            emails.append(email)
    return emails

a = print(get_emails(in_emails=emails, domain="@yandex.ru"))
print(a)


def check_age(age: int|str) -> bool:
    if age < 18:
        return False
    else:
        return True

age  = 20
if check_age(age):
    print_info("Ok")
else:
    ("Error!!!")