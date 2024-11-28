number_str = "1a2a3a4a5"
def get_sum_numbers(a):
    s = 0
    for i in a:
        if i.isdigit():
            s += int(i)
    print(s)
print(get_sum_numbers(number_str))
