# Реализовать магазин, который продает 3 вида товара.
# Программа должна показывать, сколько осталось в магазине каждого товара
# и какова прибыль на текущий момент продавца по каждому товару и всего
# (Прибыль = доход - себестоимость товара).
import pprint


class Store:
    def __init__(self, items):
        self.items = dict(items)

    def print_info_ext(self):
        pass

    def print_info(self):
        print('Items in the shop: ', self.items)

    def add_item(self, item, qnt):
        self.items.setdefault(self, item, qnt=0)
        print("The corresponding item was added to the store: %s - %d " % (item, qnt))

    def remove_item(self, item, qnt):
        self.items.pop('item')
        print("The corresponding item was removed from the store: %s - %d " % (item, qnt))

    def get_quantity(self):
        return self.items.get('item')
