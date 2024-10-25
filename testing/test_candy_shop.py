from candy_shop import(
    Candy,
    Cookie,
    IceCream,
    Sundae,
) 
def test_Candy():
    testCandy=Candy("Choclate", 1.00, 2.00)
    assert testCandy.name=="Choclate"
    assert testCandy.candy_weight==1.00
    assert testCandy.price_per_pound==2.00
def test_Cookie():
    testCookie=Cookie("Choclate chip", 60, 5.35)
    assert testCookie.name=="Choclate chip"
    assert testCookie.cookie_quantity==60
    assert testCookie.price_per_dozen==5.35
def test_IceCream():
    testIceCream=IceCream("Choclate chip", 2, 1.00)
    assert testIceCream.name=="Choclate chip"
    assert testIceCream.scoop_count==2
    assert testIceCream.price_per_scoop==1
def test_Sundae():
    testSundae=Sundae("Choclate chip", 2, 1.00, "Wip Cream", 0.25)
    assert testSundae.name=="Choclate chip"
    assert testSundae.scoop_count==2
    assert testSundae.price_per_scoop==1
    assert testSundae.topping_name=="Wip Cream"
    assert testSundae.topping_price==0.25