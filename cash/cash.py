from cs50 import get_float

def main():
    change = get_change("How much is owed? ")
    make_change(change)

def get_change(prompt):
    while True:
        n = get_float(prompt)
        if n > 0:
            break
    return n

def make_change(change):
    coins = 0
    amount = round(change)
    while amount > 0:
        if amount >= 25:
            coins = coins + 1
            amount -= 25
        elif amount >= 10:
            coins = coins + 1
            amount -= 10
        elif amount >= 5:
            coins = coins + 1
            amount -= 5
        else:
            coins = coins + 1
            amount -= 1

    print(coins)




if __name__ == "__main__":
    main()