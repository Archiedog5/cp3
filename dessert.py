from Dessert_shop import(
    order,
    Candy,
    Cookie,
    IceCream,
    Sundae,
) 

def main():
    item=order(1)
    item.add_item(Candy("Candy Corn", 1.5, .25))
    item.add_item(Candy("Gummy Bears", .25, .35))
    item.add_item(Cookie("Chocolate Chip", 6, 3.99))
    item.add_item(IceCream("Pistachio", 2, .79))
    item.add_item(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    item.add_item(Cookie("Oatmeal Raisin", 2, 3.45))
    for i in range(len(order_list)):