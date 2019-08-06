def chorus():
    print ("Old Macdonald had a farm, E I E I O!")

def oldMac(animal, sound):
    print
    chorus()
    print ("And on that farm he had a", animal, "E I E I O!")
    print ("With a %s, %s there" %(sound,sound))
    print ("and a %s, %s there" % (sound,sound))
    print ("Here a %s, there a %s," % (sound, sound))
    print ("everywhere a %s, %s." % (sound, sound))
    print
    chorus()

oldMac('cow', 'moo')
oldMac('cat', 'meow')
oldMac('dog', 'woof')
oldMac('pig', 'oink')
oldMac('sheep', 'baa')
oldMac('horse', 'neigh')
