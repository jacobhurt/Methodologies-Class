class vehicle:
    def__init__(self, manu, esize, price):
        self.setmanu
        self.setesize
        self.owner.name
        self.setprice
        self.getmanu
        self.getsize
        self.getowner

class truck(vehicle):
    def__init__(self, load, tow):
        self.setload
        self.settow
        self.getload
        self.gettow

class car(vehicle):
    def__init__(self, door):
        self.door

class person:
    def__init__(self, name):
        self.setname
        self.getname

def choice():
    print("Please enter an option:")
    print("1) Enter a new car:")
    print("2) Enter a new truck:")
    print("3) Print out all cars currently stored:")
    print("4) Print out all trucks currently stored:")
    print("5) Check all available cars under certain price:")
    print("6) Check all available trucks under certain prices:")
    print("7) Check all available vehicles under certain price:")
    print("8) Print out all vehicles made by that car manufacturer:")

if choice == '1':
    call enter a car
elif choice == '2':
    call enter a truck
elif choice == '3':
    print all cars
elif choice == '4':
    print all trucks
elif choice == '5':
    print all cars certain price
elif choice == '6':
    print all trucks certain price
elif choice == '7':
    print all vehicles certain price
else choice == '8':
    print all car under manufacturer

list=[]

def printallcars(list):
    for i in list:
        if is instance of(i,car):
            i.printsticker()

def printalltrucks(list):
    for i in list:
        if is instance of(i,car):
            i.printsticker() 
