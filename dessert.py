from abc import ABC, abstractmethod 

class DesserItems(ABC):
    def __init__(self,name):
        self.name = name
        self.tax_precent=0.75

    def __str__(self):
        return f"{self.name}"
    
    @abstractmethod
    def calculate_cost(self):
        pass

    
    def calculate_tax(self):
        tax=self.calculate_cost()*self.tax_precent
        return tax

class Candy(DesserItems):

    def __init__(self, name, candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight=candy_weight
        self.price_per_pound=price_per_pound

    def calculate_cost(self, candy_weight, price_per_pound):
        cost = candy_weight*price_per_pound
        return cost
    
class Cookie(DesserItems):

    def __init__(self, name, cookie_quantity, price_per_dozen):
        super().__init__(name)
        self.cookie_quantity=cookie_quantity
        self.price_per_dozen=price_per_dozen
    
    def calculate_cost(self, cookie_quantity, price_per_dozen):
        cookie_dozen = cookie_quantity/12
        cost = cookie_dozen*price_per_dozen
        return cost

class IceCream(DesserItems):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count=scoop_count
        self.price_per_scoop=price_per_scoop

    def calculate_cost(self, scoop_count, price_per_scoop):
        cost = scoop_count*price_per_scoop
        return cost

class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name=topping_name
        self.topping_price=topping_price

    def calculate_cost(self, scoop_count, price_per_scoop, topping_name):
        cost = scoop_count*price_per_scoop
        add_on= cost+topping_name
        return add_on
    
class Order:
    def __init__(self):
        self.Order_list=[]
        self.total=0

    def add_item(self, order):
        self.Order_list.append(order)

    def reper(self):
        item_amount=0
        for item in self.Order_list:
            print(item)
            item_amount+=1
        print("There is",(item_amount), "items in your order list.")
        return item_amount
    
    def order_cost(self):
        for item in self.Order_list:
            self.total+=item.calculate_cost()
        return self.total
    
    def order_tax(self):
        tax=self.total.calculate_tax()
        return tax