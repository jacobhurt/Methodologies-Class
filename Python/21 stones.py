stones = 21
while (stones != 0):
    while (stones != 0):
        stoneREMOVE1 = eval(input("Player One Remove 1-3 Stones: "))
        while (1 > stoneREMOVE1 or stoneREMOVE1 > 3):
            stoneREMOVE1 = eval(input("Please Enter 1, 2, or 3: "))
        stones -= stoneREMOVE1
        print ("There are",+stones, "stones left")
        if (stones == 0):
            print ("Player One Wins!")
            break     
        stoneREMOVE2 = eval(input("Player Two Remove 1-3 Stones: "))
        while (1 > stoneREMOVE2 or stoneREMOVE2 > 3):
            stoneREMOVE2 = eval(input("Please Enter 1, 2, or 3: "))
        stones -= stoneREMOVE2
        print ("There are",+stones, "stones left")
        if (stones == 0):
            print ("Player Two Wins!")
            break 
     
print ("Game Over")
