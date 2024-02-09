from datetime import datetime, timedelta

def calculate_expenses():
    # Collect user data
    name = input("Enter your name: ")
    card_balance = float(input("Enter your card balance: $"))
    wallet_balance = float(input("Enter your wallet balance: $"))
    meal_expense = float(input("Enter the value you spend for one meal: $"))
    travel_expense = float(input("Enter money required for travel: $"))
    days_to_office = int(input("Enter the number of days to the office: "))
    start_date_str = input("Enter the start date (dd/mm/yyyy): ")

    # Calculate total expense for the given days
    total_expense = travel_expense * days_to_office + meal_expense * days_to_office

    # Check if the user has enough balance
    if card_balance + wallet_balance >= total_expense:
        print("You have enough balance for the given days.")
        # Calculate the end date
        start_date = datetime.strptime(start_date_str, "%d/%m/%Y")
        end_date = start_date + timedelta(days=days_to_office - 1)
        print(f"Your end date will be: {end_date.strftime('%d/%m/%Y')}")
    else:
        print("You don't have enough balance for the given days.")

if __name__ == "__main__":
    calculate_expenses()
