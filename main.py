MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_machine_spin():
    

def deposit():
    while True:
        amount = input("ENTER YOUR AMT: $")
        if amount.isdigit:
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must not be 0.")
        else:
            print("please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("ENTER LINE (1-" + str(MAX_LINES)+")")
        if lines.isdigit:
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("amount must not be 0.")
        else:
            print("please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input("ENTER YOUR AMT FOR EACH LINE: $")
        if amount.isdigit:
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be in between {MIN_BET} and {MAX_BET}")
        else:
            print("please enter a number.")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"insufficient funds, your balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} for {lines} lines. Total amount is {total_bet}")

main()