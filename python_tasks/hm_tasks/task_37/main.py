import default
from store import Store


default.start(37)


goods = Store('electronics', 'food', 'clothes')
goods.print_info()
# goods.add_item('food', 4)
# goods.add_item('shoes', 8)



default.end()
