pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

my_ingredients = input()

if my_ingredients in pasta:
    print("You can make pasta")
if my_ingredients in apple_pie:
    print("You can make apple pie")
if my_ingredients in ratatouille:
    print("You can make ratatouille")
if my_ingredients in chocolate_cake:
    print("You can make chocolate cake")
if my_ingredients in omelette:
    print("You can make omelette")
