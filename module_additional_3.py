
def calculate_structure_sum(list_):
    count = 0
    for i in list_:
        if isinstance(i, int):
            count += i
        elif isinstance(i, str):
            count += len(i)
        elif isinstance(i, list):
            count += calculate_structure_sum(i)
        elif isinstance(i, dict):
            list_keys = i.keys()
            list_values = i.values()
            count += calculate_structure_sum(list_keys)
            count += calculate_structure_sum(list_values)
        elif isinstance(i, tuple):
            count += calculate_structure_sum(i)
        elif isinstance(i, set):
            count += calculate_structure_sum(i)
        else:
            break

    return count


data_structure = [  [1, 2, 3],  {'a': 4, 'b': 5},  (6, {'cube': 7, 'drum': 8}),  "Hello",  ((), [{(2, 'Urban', ('Urban2', 35))}])]
print(calculate_structure_sum(data_structure))