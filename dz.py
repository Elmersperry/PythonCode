def function_1(a: int, b: int, c: int):
    print(f"Сумма: {a + b + c}")
    print(f"Произведение: {a*b*c}")
    print(f"Наибольшее число: {max(a,b,c)}")
    print(f"Наибольшее число: {min(a,b,c)}")
function_1(1,2,3)

def function_2(a: str):
    b = a.split(" ")
    print(f"Количество слов в строке: {len(b)}")
    p=[]
    for i in b:
        if len(i) > 2:
            p.append(i)
    print(f"Количество слов, в которых больше 2-ух символов: {len(p)}")
    print(f"нижний регистр: {a.lower()}")
    print(f"ВЕРХНИЙ РЕГИСТР: {a.upper()}")
function_2("В этой строке 5 слов.")

list_numbers = [1,30,30,25,24,30,1,27,25,40]