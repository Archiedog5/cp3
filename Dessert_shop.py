from dessert import(
    Order,
    Candy,
    Cookie,
    IceCream,
    Sundae,
    DesserItems

) 


    

def main():
    list = []
    order1 = Order()
    order1.add_item(Candy("Candy Corn", 1.5, .25))
    order1.add_item(Candy("Gummy Bears", .25, .35))
    order1.add_item(Cookie("Chocolate Chip", 6, 3.99))
    order1.add_item(IceCream("Pistachio", 2, .79))
    order1.add_item(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order1.add_item(Cookie("Oatmeal Raisin", 2, 3.45))
    order1.reper()
    x=order1.reper()
    for i in range(x):
        
main()