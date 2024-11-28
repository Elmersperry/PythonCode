import os


# функция open(file, mode, encoding) - открывает файл
# file - путь к файлу (абсолютный или относительно скрипта)
# mode - режим открытия файла
# encoding - кодировка
from python_set import names

# основные режимы: r - чтение, w - запись с пересозданием файла, a - добавление в конец файла

myfile = open(file="myfile.txt", mode="w", encoding="utf-8")
print(type(myfile))

# write - запись в файл
myfile.write("Python!!!\n")
text = "Forever!!!"
myfile.write(text+"\n")
# my_list = ["alena,", "elena!"]
# for item in my_list:
#     myfile.write(item+"\n")
# for item in my_list:
#     myfile.write(item.strip(",!")+"\n")
# names = "\n".join(my_list)
# myfile.write(names)

# после завершения работы с файлом - закрываем его
myfile.close()

# открытие файла в режиме добавления в конец файла
myfile = open(file="myfile.txt", mode="a", encoding="utf-8")
myfile.write("Python!!!\n")
# myfile.writelines(my_list)
myfile.close()

# открытие файла для чтения
myfile = open(file="myfile.txt", mode="r", encoding="utf-8")
text_from_file = myfile.read()
text_rows = text_from_file.split("\n")
print(text_from_file)
print(text_rows)

# text_lines = myfile.readlines()
# print(text_lines[0], text_lines[1])
# print(text_lines)

my_list = ["alex", "ivanov"]
print(*my_list, sep="\n")

filename = "myfilenew.txt"
if os.path.exists(filename):
    with open(file="filename", mode="r", encoding="utf-8") as myfile:
        text_form_f = myfile.read()
else:
    with open(file="filename", mode="w", encoding="utf-8") as myfile:
        pass

if os.path.exists(filename):
    os.rename(filename, f"new_{filename}")

dir_name = "files"
if not os.path.exists(dir_name):
    os.makedirs(dir_name, exist_ok=True)