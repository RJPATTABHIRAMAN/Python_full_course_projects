menu = {"potato":99,
        "samosa":49,
        "parota":20,
        "Chiken":199,
        "Burger":599,
        "idly":19}
print("---------Your Menu--------")
for key,value in menu.items():
    print(f"{key}:₹{value:.2f}")
card = []
total = 0
while True:
    food = input("Enter food you want enter (q to quit ):")
    if food.lower()=='q':
        break
    elif menu.get(food):
        card.append(food)
print("----Your Bill------")
for f in card:
    total+=menu.get(f)
    print(f,end=" ")
print()
print(total)
print("Thank You")
