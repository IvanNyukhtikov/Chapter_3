calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    str_tuple = (len(string), string.upper(), string.lower())
    return str_tuple

def  is_contains (string, list_to_search):
    count_calls()
    for i_list in list_to_search:
        if string.casefold() == i_list.casefold():
            return True
        else:
            return False

str_1 = 'Овца'
str_info = string_info(str_1)
print(str_info)

str_1 = 'Баран'
str_info = string_info(str_1)
print(str_info)

str_2 = 'Вода'
list_1 = ['Вода', 'Земля', 'Воздух', 'Огонь']
result = is_contains(str_2, list_1)
print(result)

str_3 = 'дерево'
list_1 = ['Вода', 'Земля', 'Воздух', 'Огонь']
result = is_contains(str_3, list_1)
print(result)

print(calls)