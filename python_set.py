# множества set() - только уникальные значения
numbers = {1,2,2,2,2,4,5}
print(type(numbers))
print(numbers)

names = ["Sasha", "Lena", "Igor", "Igor", "Olga", "Sasha"]
names = list(set(names))
print(names)

# добавление элемента во множество
numbers.add(6)
print(numbers)

# удаление элемента из множества
numbers.remove(2)
print(numbers)

# удаление элемента из множества
numbers.discard(10)
print(numbers)

first_numbers = {1,2,3,4,5}
second_numbers = {4,5,6,7,8}

# объединение множеств
third_numbers = first_numbers.union(second_numbers)
print(third_numbers)
print(first_numbers | second_numbers)

# пересечение множеств
third_numbers = first_numbers.intersection(second_numbers)
print(first_numbers & second_numbers)
print(third_numbers)

# разность множеств
third_numbers = second_numbers.difference(first_numbers)
print(third_numbers)
print(first_numbers - second_numbers)
third_numbers = second_numbers.symmetric_difference(first_numbers)
print(third_numbers)
print(first_numbers ^ second_numbers)

frozen_numbers = frozenset(numbers)
print(type(frozen_numbers))