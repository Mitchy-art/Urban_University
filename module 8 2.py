def personal_sum(numbers):
    result = 0
    incorrect_data = 0
        # if isinstance (numbers(int)):
        #     result = sum(numbers)
    for i in numbers:
        try:
            print(f'Некорректный тип данных для подсчета суммы - {i}')
            result += i
        except TypeError as exc:
            #print(exc)
            incorrect_data +=1
    return result, incorrect_data


def calculate_average(numbers):
    try:
        total_sum, incorrect_data = personal_sum(numbers)
        return total_sum / (len(numbers) - incorrect_data)
        # for i in numbers:
        #     personal_sum(i)/len(numbers)
        #cal_ave = personal_sum(numbers)/len(numbers)
    except ZeroDivisionError as exc:
        return 0
    except TypeError as exc:
        print('В numbers записан некорректный тип данных')

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать