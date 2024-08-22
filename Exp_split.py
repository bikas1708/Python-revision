def calc_split(
    total_amount: float, number_of_people: int, currency: str, split: list = None
) -> None:
    if number_of_people < 1:
        raise ValueError("Number of people must be greater than one")
    #print(f"{'Yearly net income:':<30}{currency:>10} {yearly_net_income:>15,.2f}")

    print(f"{'Total Expense:':<25}{currency:>10}{total_amount:>10,.2f}")
    print(f"{'Number of people:':<25}{"":>10}{number_of_people:>10}")

    if split:
        values: list = (i for i in range(1, number_of_people + 1))
        dic: dict = {
            key: total_amount * (value / 100) for (key, value) in zip(values, split)
        }
        print(f"{'Each Person Should Pay:':<25}{"\n"}{"\n".join([f'{k:<15}{currency:>20}{v:>10,.2f}' for k,v in dic.items()])}")
    else:
        share_per_person: float = total_amount / number_of_people
        print(f"{'Each person should pay:':<25}{currency:>10}{share_per_person:>10,.2f}")


def main() -> None:

    while True:
        try:
            total_amount: float = float(input("Enter the total Amount: \n"))
            number_of_people: int = int(input("Enter the Number of People: \n"))
            currency: str = str(input("Enter currency code. Eg-INR: \n"))
            if_split: str = input("Uneven split? Y/N :").lower()

        except ValueError as e:
            print(f"Error: {e}, Please try again")

        else:
            break
    uneven_split: list = list()
    if if_split == "y":
        Split: int = number_of_people
        while Split:

            input_value = input(
                "Enter the percentage of split. To finish, press enter key without any input:\n"
            )

            if input_value == "":
                flag = False
                continue
            # Used To catch error, only takes float/int values.
            try:
                ENTRY: float = float(input_value)
                uneven_split.append(ENTRY)
                Split = Split - 1
            except ValueError:
                print("Please Enter valid value")

        if sum(float(i) for i in uneven_split) != 100:
            print(f"Split is not 100% please check: \n{"%\n".join(str(i) for i in uneven_split)}%")
        if sum(float(i) for i in uneven_split) == 100:
            calc_split(total_amount, number_of_people, currency, uneven_split)
    else:
        calc_split(total_amount, number_of_people, currency)


if __name__ == "__main__":
    main()


"""
Homework:
1. Edit the script to give the user the option to enter uneven splits, such as 20%, 40%, 40%.
2. Make it so that if the user encounters an error, the program nicely asks them to try again with
a proper value.

"""
