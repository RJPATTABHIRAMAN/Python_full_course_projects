import random
import math
low = 10
high=100

ans = random.randint(low,high)
count=0

is_correct = True
print(f"Enter number which range between {low} and {high}")
while is_correct:
    guss = input("Enter Your Guss ")
    count+=1
    if guss.isdigit():
       
        guss=int(guss)
        if guss < low or guss > high:
            print("Invalid Guss")
            print("NUmber out of range")
            print(f"Enter number which range between {low} and {high}")

        elif guss<ans:
            print("Too low......")
            print(f"Enter number which range between {low} and {high}")

        elif guss>ans:
            print("Too High.......")
        else:
            print(f"Your guss is correct {ans}")
            print(f"No of time required to find count {count}")
            break


    else:
        print("Invalid guss")
        print(f"Enter number which range between {low} and {high}")
