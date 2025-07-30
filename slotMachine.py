import random

def spint_row():
    symbol = ['🏏','⚽','🎾','🏑','❤️','❤️‍🩹']
    return [random.choice(symbol) for _ in range(3)]

def print_row(row):
    print("******************")
    print(" ".join(row))
    print("******************")

def pay_out(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🏏':
            return bet * 10
        elif row[0] == '⚽':
            return bet * 30
        elif row[0] == '🎾':
            return bet * 6
        elif row[0] == '🏑':
            return bet * 6
        elif row[0] == '❤️':
            return bet * 5
        elif row[0] == '❤️‍🩹':
            return bet * 0.5
    return 0

def main():
    balence = 100
    print("********************")
    print("Welcome to Python Slots")
    print("Symbols: 🏏 ⚽ 🎾 🏑 ❤️ ❤️‍🩹")
    print("********************")
    
    while balence > 0:
        try:
            bet = int(input(f"\nYour balance: ₹{balence}\nEnter amount you want to bet: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if bet > balence:
            print("Insufficient balance")
            continue
        if bet <= 0:
            print("Amount should be greater than 0")
            continue

        balence -= bet
        print("Spinning.........")
        row = spint_row()
        print_row(row)

        payout = pay_out(row, bet)
        if payout > 0:
            print(f"Yes! You won ₹{payout}")
        else:
            print("You lost")
        balence += payout

    print("Game over! Your balance is ₹0")

if __name__ == '__main__':
    main()
