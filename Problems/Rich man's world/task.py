deposit = int(input())
year = 0

while deposit < 700000:
    deposit = deposit * 1.071
    year += 1
print(year)

i = 1
while i <= 20:
    print(i ** 2)
    i += 1

