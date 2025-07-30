foods=[]
prices=[]
total=0

while True:
    food = input("Enter food name you want :")
    if(food.lower()=='q'):
        break
    else:
        price = float(input("Enter price of the food ₹"))
        foods.append(food)
        prices.append(price)
for i in foods:
    print(i, end=" ")
print()
for price in prices:
    total+=price
print(total)