import random

# Adjusted with extra spaces to balance visual squareness
dice_faces = {
    1: [
        "┌─────┐",
        "│     │",
        "│  ●  │",
        "│     │",
        "└─────┘"
    ],
    2: [
        "┌─────┐",
        "│ ●   │",
        "│     │",
        "│   ● │",
        "└─────┘"
    ],
    3: [
        "┌─────┐",
        "│ ●   │",
        "│  ●  │",
        "│   ● │",
        "└─────┘"
    ],
    4: [
        "┌─────┐",
        "│ ● ● │",
        "│     │",
        "│ ● ● │",
        "└─────┘"
    ],
    5: [
        "┌─────┐",
        "│ ● ● │",
        "│  ●  │",
        "│ ● ● │",
        "└─────┘"
    ],
    6: [
        "┌─────┐",
        "│ ● ● │",
        "│ ● ● │",
        "│ ● ● │",
        "└─────┘"
    ]
}

dice=[]
total_no = 0
no_of_times= int(input("Enter the no of die you want to roll:   "))
for die in range(no_of_times):
    dice.append(random.randint(1,6))
# for die in range(no_of_times):
#     for i in dice_faces.get(dice[die]):
#         print(i)
for line in range(5):
    for die in dice:
        print(dice_faces.get(die)[line],end=" ")
    print()

for die in dice:
    total_no+=die
print(f"₹total{total_no}")
