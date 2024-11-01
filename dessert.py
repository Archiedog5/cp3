from Dessert_shop import(
    Candy,
    Cookie,
    IceCream,
    Sundae

) 

class Order:
    def __init__(self):
        self.Order_list=[]

    def add_item(self, order):
        self.Order_list.append(order)
    def reper(self):
        item_amount=0
        for item in self.Order_list:
            print(item)
            item_amount+=1
        print("There is",(item_amount), "items in your order list.")
def main():
    order1 = Order()
    order1.add_item(Candy("Candy Corn", 1.5, .25))
    order1.add_item(Candy("Gummy Bears", .25, .35))
    order1.add_item(Cookie("Chocolate Chip", 6, 3.99))
    order1.add_item(IceCream("Pistachio", 2, .79))
    order1.add_item(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order1.add_item(Cookie("Oatmeal Raisin", 2, 3.45))
    order1.reper()
main()