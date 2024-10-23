from time import sleep
from datetime import datetime
from threading import Thread

class Knight(Thread):
    def __init__(self,name, power):
        super().__init__()
        self.name = name
        self.power = power
    def run(self):
        day = 0
        enemy = 100
        print(f"{self.name}, на нас напали!")
        while enemy > 0:
            day += 1
            enemy = enemy - self.power
            print(f"{self.name} сражается {day} дней(дня), осталось {enemy} воинов.")
            sleep(1)
        print(f"{self.name} одержал победу спустя {day} дней(дня)!")

Knight1 = Knight('Sir Lancelot', 10)
Knight2 = Knight("Sir Galahad", 20)
Knight1.start()
Knight2.start()
Knight1.join()
Knight2.join()

print("Все битвы закончились!")
