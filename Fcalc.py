def calc_finances(
    monthly_income: float,
    tax_rate: float,
    user_expense: float,
    currency: str,
) -> None:

    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    monthly_income_deducted: float = monthly_net_income - user_expense
    yearly_tax: float = monthly_tax * 12
    yearly_salary: float = monthly_income * 12
    yearly_net_income: float = yearly_salary - yearly_tax
    yearly_user_expense: float = user_expense * 12
    yearly_income_deducted: float = yearly_net_income - yearly_user_expense

    print(f"{'':-<60}")
    print(f"{'Monthly income:':<30}{currency:>10} {monthly_income:>15,.2f}")
    print(f"{'Tax Rate:':<30} {tax_rate:>25,.2f}%")
    print(f"{'Monthly Tax:':<30}{currency:>10} {monthly_tax:>15,.2f}")
    print(f"{'Monthly net Income:':<30}{currency:>10} {monthly_net_income:>15,.2f}")
    print(f"{'Yearly salary:':<30}{currency:>10} {yearly_salary:>15,.2f}")
    print(f"{'Yearly tax paid:':<30}{currency:>10} {yearly_tax:>15,.2f}")
    print(f"{'Yearly net income:':<30}{currency:>10} {yearly_net_income:>15,.2f}")
    print(
        f"{'Monthly income with Expense:':<30}{currency:>10} {monthly_income_deducted:>15,.2f}"
    )
    print(f"{'Montly Personal Expense:':<30}{currency:>10} {user_expense:>15,.2f}")
    print(
        f"{'Yearly Personal Expense:':<30}{currency:>10} {yearly_user_expense:>15,.2f}"
    )
    print(
        f"{'Yearly Income with Expense:':<30}{currency:>10} {yearly_income_deducted:>15,.2f}"
    )
    print(f"{'':-<60}")


# calc_finances(1000, 20, currency="INR",123214)
# calc_finances(1000, 20, 123214, currency="INR")


def main() -> None:
    # USED while loop to handle user Input Errors.
    while True:
        try:
            monthly_income: float = float(input("Enter Your monthly salary: "))
        except ValueError:
            print("The argument should be a number")
        else:
            break

    while True:
        try:
            tax_rate: float = float(input("Enter Your tax rate (%): "))
        except ValueError:
            print("The argument should be a number")
        else:
            break

    flag = True
    monthly_expense = list()
    while flag:
        input_value = input(
            "Enter the value in the list. To finish, press enter key without any input:\n"
        )

        if input_value == "":
            flag = False
            continue
        # Used To catch error, only takes float/int values.
        try:
            ENTRY: float = float(input_value)
            monthly_expense.append(ENTRY)
        except ValueError:
            print("Enter valid number")
    mon_exp = sum(float(i) for i in monthly_expense)

    calc_finances(monthly_income, tax_rate, mon_exp, currency="INR")


if __name__ == "__main__":
    main()


"""
Homework:
1. Edit the script so that users can also enter their expenses (eg. rent, food, gym memberships) so they
can see how much they have left over each month.
2. Recreate the user input section to safely handle users inserting the wrong type without 
crashing the program.

"""
