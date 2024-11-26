# def get_info(name, age=34):
#     print(name.title())
#     print(age)

# get_info(name="alex")
#
# a = [1,2,3]
# * - оператор распаковки
# b = [*a,4,5,6]
# print(b)
#
# def print_scores(name, first_test, *scores):
#     print(f"name - {name}")
#     for i in scores:
#         print(i)
#
# print_scores("dima", 26, 27, 56, 23, 67)
#
# def func(*args, **kwargs):
#     print(args)
#     pass
#
# func(1,2,3,4,5)
#
# def func_2(a,b):
#     pass

def print_pet_names(owner, **pets):
    print(f"Владелец - {owner}")
    for key, value in pets.items():
        print(f"{key} - {value}")

print_pet_names(owner="Dima", dog="Tima", cat="Barsik")