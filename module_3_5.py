
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if int(str_number[-1]) == 0:
        str_number = str_number[:-1]
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(4020305)
print(result)
