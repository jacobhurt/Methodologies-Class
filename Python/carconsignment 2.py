class vehicle:
    def __init__(self, manu, esize, owner, price ):
        self.manu = manu
        self.esize = esize
        self.owner = owner
        self.price = price
    def regCost():
        return price
    def printsticker(self):
        print ("manufacturer: ", self.manu)
        print ("engine size: ", self.esize)
        print ("Owner: ", self.owner)
        print ("Price: ", self.price)
        

class truck(vehicle):
    def __init__(self,manu, esize, owner, price, load, tow):
        vehicle.__init__(self, manu, esize, owner, price)
        self.load = load
        self.tow = tow
    def regCost(self):
        return float(self.price) * 1.25
    def printsticker(self):
        print ("Load: ",self.load)
        print ("Tow: ",self.tow)
        print ("regcost:", self.regCost())

class car(vehicle):
    def __init__(self, manu, esize, owner, price, door):
        vehicle.__init__(self, manu, esize, owner, price)
        self.door = door
    def regCost(self):
        return float(self.price) * 1.33
    def printsticker(self):
        print ("doors: ",self.door)
        print ("regcost:", self.regCost()) 
    
class person:
    def __init__(self, name):
        self.setname = name


def addCar():
    m = input("What is the manufacturer of your vehicle?")
    es = input("What is your engine size?")
    price = float(input("What is your desired price?"))
    p = input("Please enter the name of the owner:")
    door = input("How many doors does your vehicle have?")
    inven.append(car(m, es, p, price, door))

def addTruck():
    m = input("What is the manufacturer of your vehicle?")
    es = input("What is your engine size?")
    price = float(input("What is your desired price?"))
    p = input("Please enter the name of the owner:")
    load = input("How much can your vehicle hold?")
    tow = input("How many cars can it tow?")
    inven.append(truck(m, es, p, price, load, tow)) 

def allCars(inven):
    for i in inven:
        if isinstance(i,car):
            i.printsticker()

def allTrucks(inven):
    for i in inven:
        if isinstance(i,truck):
            i.printsticker()


def priceCars():
    cost = float (input("Enter a price: "))
    for i in inven:
        if isinstance(i,car) and i.regCost() < cost:
            i.printsticker()


def priceTrucks():
    cost = float (input("Enter a price: "))
    for i in inven:
        if isinstance (i, truck) and i.regCost() < cost:
            i.printsticker()

def priceVeh():
    cost = float (input("Enter a price: "))
    for i in inven:
        if i.regCost() < cost:
            i.printsticker()
            if isinstance (i, car):
                print ("Type: Car")
            elif isinstance (i, truck):
                print ("Type: Truck") 
            

def allManu():
    model = input("Enter a manufacturer: ")
    for i in inven:
        if i.manu == model:
            i.printsticker()
            if isinstance (i, car):
                print ("Type: Car")
            if isinstance (i, truck):
                print ("Type: Truck") 

def main(inven):
    while (True):
        print("\n")
        print("Please enter an option:")
        print("1) Enter a new car:")
        print("2) Enter a new truck:")
        print("3) Print out all cars currently stored:")
        print("4) Print out all trucks currently stored:")
        print("5) Check all available cars under certain price:")
        print("6) Check all available trucks under certain prices:")
        print("7) Check all available vehicles under certain price:")
        print("8) Print out all vehicles made by that car manufacturer:")
        choice = input()
        if choice == '1':
            addCar()
        elif choice == '2':
            addTruck()
        elif choice == '3':
            allCars(inven)
        elif choice == '4':
            allTrucks(inven)
        elif choice == '5':
            priceCars()
        elif choice == '6':
            priceTrucks()
        elif choice == '7':
            priceVeh()
        else: #choice == '8':
            allManu()

inven = [] 

main(inven) 
