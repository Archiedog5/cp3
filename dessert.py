from Dessert_shop import(
    Candy,
    Cookie,
    IceCream,
    Sundae,
    Order,

) 

def main():
    Order.add_item(Candy("Candy Corn", 1.5, .25))
    Order.add_item(Candy("Gummy Bears", .25, .35))
    Order.add_item(Cookie("Chocolate Chip", 6, 3.99))
    Order.add_item(IceCream("Pistachio", 2, .79))
    Order.add_item(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    Order.add_item(Cookie("Oatmeal Raisin", 2, 3.45))
    z = Order.add_item
    print(z)
main()