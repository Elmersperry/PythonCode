from http.client import responses

import requests
# """
# try:
#     блок,
#     где возможна
#     ошибка
# except:
#     действия
#     в случае
#     ошибки
# finally:
#     блок кода,
#     который выполнится в любом случае
# """
# age = input("Enter the age: ")
# try:
#     if age < 18:
#         print("Error")
#     else:
#         print("Ok")
# except:
#     if age.isdigit():
#         if int(age) < 18:
#             print("Error")
#         else:
#             print("не число")

# def send_data():
#     data = {"name": "Alex", "age": 26}
#     data= None
#     return Exception("ERROR")

# def get_data_from_server():
#     try:
#         data = send_data()
#         print(data)
#     except:
#         data = []
#         for i in data:
#             print(i)
# get_data_from_server()

# try:
#     mydict = {"name": "dima"}
#     if not mydict.get("age"):
#         print(mydict.get("age"))
#         raise Exception("Такого ключа нет!!!")
# except Exception as err:
#     print(err)

# def check_age(age):
#     if age > 102:
#         raise Exception("Возраст слишком большой!!!")
#     return age
# try:
#     print(check_age(226))
# except:
#     print("Возникла ошибка")

# HTTP
def get_page(url):
    try:
        response = requests.get(url)
        print(response.status_code)
        print(response.text)
    except:
        print("Error")

url = "https://en.wikipedia.org/wiki/Main_Page"
get_page(url)