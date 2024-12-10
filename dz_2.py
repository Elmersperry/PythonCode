myfile = open(file="myfile.txt", mode="r", encoding="utf-8")
text_from_file = myfile.read()
text_rows = text_from_file.split("\n")
print(text_from_file)
print(len(text_rows))

num = [1,2,3,4,5,6,7,8,9]
a = 0
for i in num:
    if i > 4:
        a += 1
print(a)