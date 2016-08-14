class Customer(object):
    def __init__(self, name, fund, bike):
        self.name = name
        self.fund = fund
        self.bike = None
        
    def purchase(self, bike):
        price = bike.price
        self.fund -= price
        self.bike = bike

class BikeShop(object):
    def __init__(self, name, margin, bikes):
        self.name = name
        self.margin = margin
        self.profit = 0
        self.inventory = {}
        
        for bike in bikes:
            bike.markup = int((bike.cost / 100.0) * self.margin)
            bike.price = bike.cost + bike.markup
            self.inventory[bike.model] = bike
    
    def sale(self, bike):
        ##del self.inventory[bike.model]
        self.inventory[bike.model] = None
        
    def __str__(self):
        for model in self.inventory:
            if model:
                print model
        
class Bicycle(object):
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
        self.markup = 0
        self.price = 0
        

    def __str__(self):
        template = "{0} -- Cost: ${1}; Weight: {2}lbs"
        return template.format(self.model, self.price, self.weight)
    
        

redBike = Bicycle("red", 50, 100)
yellowBike = Bicycle("yellow", 60, 120)
blueBike = Bicycle("blue", 75, 150)
greenBike = Bicycle("green", 90, 200)
pinkBike = Bicycle("pink", 50, 180)
blackBike = Bicycle("black", 45, 300)

bikeShop = BikeShop("Bikes101", 0.2, [redBike, yellowBike, blueBike, greenBike, pinkBike, blackBike])

customer1 = Customer("Harry", 200, None)
customer2 = Customer("Larry", 500, None)
customer3 = Customer("Mary", 1000, None)

print bikeShop

customer3.purchase(blueBike)
bikeShop.sale(blueBike)

print bikeShop