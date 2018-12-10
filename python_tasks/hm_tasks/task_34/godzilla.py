# 34. Создать класс Годзила.
# У данного класса должен быть атрибут - объем желудка.
# Написать для данного класса метод поедания людей.
# В данную функцию должен передаваться объем съеденного и соответственно уменьшаться место в желудке.
# Когда Годзила заполнит желудок на 90%, метод должен выводить надпись, что Годзила наелся и больше не может поедать людей.

class Godzilla:
    def __init__(self, stomach_size):
        self.stomach_size = float(stomach_size)
        self.stomach_filling = 0.0
        self.stomach_filling_upper_limit = stomach_size * 90 / 100


    def print_info(self):
        print('~'*50)
        print('Godzilla\'s stomach size:', self.stomach_size)
        print('Godzilla\'s stomach upper line:', self.stomach_filling_upper_limit)
        print('Godzilla\'s stomach filling:', self.stomach_filling)
        if self.stomach_filling >= self.stomach_filling_upper_limit:
            print('Godzilla\'s stomach is full. Godzilla is unable to eat more.')
        print('~'*50)


    def daily_lunch(self, human_weight):
        if (self.stomach_filling + human_weight) <= self.stomach_filling_upper_limit:
            self.stomach_filling += human_weight
            print('Godzilla has eaten human with weight ', human_weight)
            if self.stomach_filling == self.stomach_filling_upper_limit:
                print('Godzilla\'s stomach is full. Godzilla is unable to eat more.')
        else:
            print('Godzilla\'s stomach is full. Godzilla is unable to eat more than %.1f' % (self.stomach_filling_upper_limit - self.stomach_filling))

