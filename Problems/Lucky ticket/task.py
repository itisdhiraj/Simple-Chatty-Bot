# Save the input in this variable
ticket = int(input())

x = ticket // 100000
x1 = (ticket - x * 100000) // 10000
x2 = (ticket - x*100000 - x1*10000) // 1000
x3 = (ticket - x*100000 - x1*10000 - x2*1000) // 100
x4 = (ticket - x*100000 - x1*10000 - x2*1000 - x3*100) // 10
x5 = (ticket - x*100000 - x1*10000 - x2*1000 - x3*100 - x4*10)
# Add up the digits for each half
half1 = x + x1 + x2
half2 = x3 + x4 + x5

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")