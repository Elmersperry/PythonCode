# Условное выражение
age = 23
if age < 20:
    print("Error")
    if age < 15:
        print("Fatal")
    else:
        print("Not fatal")
elif age < 25:
    print("<25")
else:
    print("Ok")

print("Next")

# Цикл FOR

numbers = [1,2,3,4,5,6,7,8,9]
cars = ["bmv", "audi", "lada"]
N = 10

# for _ in numbers:
#     print("hi")
#
# for i in range(N+1):
#     print(i)
#
# for car in cars:
#     print(car)
#
# for i in range(len(cars)):
#     print(i)
#
# for ind in range(len(cars)):
#     print(ind, cars[ind])

a = 10
b = 0

while a < 20:
     print(a)
     b += 1
     if b == 15:
         break
