days = int(input())
food_cost = int(input())
flights = int(input())
hotel_cost = int(input())

total_food_costs = days * food_cost
total_flight = flights * 2
total_hotel = hotel_cost * (days - 1)

total_costs = total_flight + total_food_costs + total_hotel
print(total_costs)