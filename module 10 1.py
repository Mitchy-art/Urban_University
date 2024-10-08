from time import sleep
from threading import Thread
from datetime import datetime

time_start_func = datetime.now()


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for word_number in range(1, word_count+1):
            file.write(f'Какое-то слово № {word_number}' + '\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end_func = datetime.now()
time_res_func = time_end_func - time_start_func
print('Время функции:', time_res_func)

time_start_thr = datetime.now()
thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(10, 'example6.txt'))
thr_third = Thread(target=write_words, args=(10, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(10, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end_thr = datetime.now()
time_res_thr = time_end_thr - time_start_thr

print('Время потока:', time_res_thr)