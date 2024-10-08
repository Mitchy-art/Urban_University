from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        fight = 0
        day = 0
        enemes = 100
        while enemes > 0:
            fight = enemes - self.power
            enemes = fight
            sleep(1)
            day += 1
            print(f'{self.name} сражается {day} день(дня)..., осталось {fight} воинов.')
        if fight <= 0:
            print(f"{self.name} одержал победу спустя {day} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
