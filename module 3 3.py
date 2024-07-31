def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(8)
print_params(5, 6)
print_params(9,5,2)
# print_params()  - unexpected indent
print('-------------------')

print_params(b=25)
print_params(c=[1, 2, 3])
print('-------------------')

values_list = [3, True, 'cat']
values_dict = {'a': 54, 'b': False, 'c': 'dog'}
print_params(*values_list)
print_params(**values_dict)
print('-------------------')

values_list_2 = [1.5, (32, 5)]
print_params(*values_list_2, 42)