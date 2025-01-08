import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        text = file.readline()
        all_data.append(file)

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

line_start = datetime.now()

for i in files:
    read_info(i)

line_end = datetime.now()
time_for_line = line_end - line_start
print(f'Линейно: {time_for_line}')

if __name__ == '__main__':
    time_mult_start = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)

    time_mult_end = datetime.now()
    time_of_multiprocessing = time_mult_end - time_mult_start
    print(f'Мультипроцесс : {time_of_multiprocessing}')