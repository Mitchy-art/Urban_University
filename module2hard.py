#import random

#def n():
#    list_ = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#    number1 = random.choice(list_)
#    return number1


#print(n)

print('---------------------------------------')


def gen_password():
    password = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password


for n in range(3, 21):
    print(n, '-', gen_password())
