import io
from pprint import pprint
def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    line_number = 1
    strings_positions = {}   #{(<номер строки>, print(file.tell)):line}
    for line in strings:
        position = file.tell()
        file.write(line+'\n')
        strings_positions[(line_number, position)] = line
        line_number += 1
    file.close()
    return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
