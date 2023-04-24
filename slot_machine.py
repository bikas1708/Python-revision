import random

MAX_LINES = 3  #Global value
MAX_BET=100
MIN_BET=1


ROWS=3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8,

}

symbol_value={
    "A":5,
    "B":3,
    "C":2,
    "D":1,

}


def check_winnings(columns,lines,bet,values):
    #check which row user bet on first
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:  #we can do a for else where if there is no break then the else statement works
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) #using +1 to make it 1,2,3 instead of 0,1,2
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):   #can use _ when u js want a random variable which u wont use afterwards
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):  #generate a value for every column we have
        #Here we are picking a value for every column
        column=[]
        current_symbols=all_symbols[:] #using [:] so that it makes a copy instead of a reference to the main one  (basically a copy)
        for _ in range(rows):
            value=random.choice(current_symbols)  #picking a random value
            current_symbols.remove(value)  #since only limited value is there, we pick one n remove it so we don't pick it again

            column.append(value)  #add the value to our column
        columns.append(column)
    return columns

def print_slot_machine(columns):
    #our columns would be laid out as rows like
    #[A,B,C]    --> [A A]    
    # [A,A,A]       [B A]
    #               [C A]
    # Basically we are transposing it (matrix transpose)
    for row in range(len(columns[0])):  #loop thru every row we have
        for i,column in enumerate(columns):  #for every row we loop thru every column
            #for every column we print the current row
            if i<len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="\n")



def deposit():

    while True:
        amount=input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a Number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to be on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if lines>0 and lines<=MAX_LINES:
                break
            else:
                print("Enter a valid no. of lines.")
        else:
            print("Enter a number")

    return lines

def get_bet():
    while True:
        amount=input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a Number")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines

        if total_bet>balance:
            print(f"You donot have enough balance. your current balance is ${balance}")
        else:
            break
   
    print(f"You are betting ${bet} on {lines} lines. Total bet = ${total_bet}")
    #print(balance,lines)

    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots )
    winnings, winning_lines=check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ",*winning_lines)  #unpacts the winning lines list n prints it

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        ans = input("Press enter to Play (q to quit).")
        if ans =="q":
            break
        balance += spin(balance)
    print(f"You are left with ${balance}.")
main()