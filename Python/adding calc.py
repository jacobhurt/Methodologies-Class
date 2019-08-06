subtotal = 0
total = 0
zeroes = 0
while zeroes != 2:
    number = eval(input())
    if number != 0:
        subtotal = subtotal + number
        total = total + number
        zeroes = 0
    else:
        zeroes = zeroes + 1
        print("subtotal",+ subtotal)
        subtotal = 0
print("total",+ total)
