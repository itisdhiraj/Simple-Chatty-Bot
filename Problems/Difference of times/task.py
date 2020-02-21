hour1 = int(input())
minute1 = int(input())
seconds1 = int(input())

hour2 = int(input())
minute2 = int(input())
seconds2 = int(input())

total_seconds1 = (hour1 * 3600) + (minute1 * 60) + seconds1
total_seconds2 = (hour2 * 3600) + (minute2 * 60) + seconds2

print(total_seconds2 - total_seconds1)