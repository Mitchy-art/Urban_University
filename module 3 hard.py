def calculate_structure_sum(*args):
    count = 0
    for i in args:
        if isinstance(i, int):
            count += i
        elif isinstance(i, str):
            count += len(i)
        elif isinstance(i, dict):
            count += calculate_structure_sum(*i.items())
        elif isinstance(i, (list, set, tuple)):
            count += calculate_structure_sum(*i)
    return count


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
