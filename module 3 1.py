def count_calls():
    global calls
    # print(calls)
    calls += 1
    # print(calls)


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()



def is_contains(string, list_to_search):
    count_calls()
    list_to_search = [a.lower() for a in list_to_search]
    if string.lower() in list_to_search:
        return True
    else:
        return False




# is_contains()
# print(calls)
# string_info()

calls = 0
# list_to_search = ['urban']
# # string = 'dog'



# string = ((input('Введите строку:')))
# string = ((a.lower() for a in string))


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)


