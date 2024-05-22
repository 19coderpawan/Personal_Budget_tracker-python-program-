# It is a budget tracker program through which you can tack and organize you budget.
import json

# to store all the transaction in a structural format we will use list of dictionary.
Transactions = []


# function to add the Transactions-:
def add_transactions(amount, category, description, type):
    transaction = {
        "amount": amount,
        "category": category,
        "description": description,
        "type": type
    }
    Transactions.append(transaction)


# function to add the income in Transactions-:
def add_income():
    amount = int(input("enter the income amount-:"))
    category = input("enter the category-:")
    des = input("enter the description-:")
    add_transactions(amount, category, des, "Income")


# function to add the expenses in Transactions-:
def add_expense():
    amount = int(input("enter the expense amount-:"))
    category = input("enter the category-:")
    des = input("enter the description-:")
    add_transactions(amount, category, des, "Expenses")


# function to view the Transactions-:
def view_transactions():
    print("YOUR TRANSACTIONS ARE-:")
    #     to view each transaction we have to iterate through the list.
    for transaction in Transactions:
        print(
            f"{transaction['type']}-:{transaction['amount']} | {transaction['category']} | {transaction['description']}")


def view_blance():
    # total_income=0
    # total_expense=0
    # for transaction in Transactions:
    #     if transaction['type']=="Income":
    #         total_income=total_income+transaction['amount']
    #     else:
    #         total_expense=total_expense+transaction['amount']

    # using sum() fun of python to add elements of list iterable.
    total_income = sum(transaction['amount'] for transaction in Transactions if transaction['type'] == "Income")
    total_expense = sum(transaction['amount'] for transaction in Transactions if transaction['type'] == "Expenses")
    balance = total_income - total_expense
    print(f"Total Income-:{total_income}")
    print(f"Total Expense-:{total_expense}")
    print(f"Balance Left-: {balance}")


# function to save the Transactions in the File-:
# json.dump() serializes Python objects to JSON formatted strings and writes them to a file.
# json.load() reads JSON formatted strings from a file and deserializes them into Python objects.
# These functions are commonly used for data serialization and deserialization, especially when working with data
# interchange between different systems or storing data in a human-readable format.
def save_file(file):
    with open(file, 'w') as f:
        json.dump(Transactions, f)
        print(f"your data is being save to the file {file}")


# function to load the saved data from the specified file.
def load_file(file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            print(f"Your data is successfully loaded from file {file}")
            print(f"data -: {data}")
    except FileNotFoundError:
        print("unable to find the file")


def main():
    while True:
        print("Choose 1- add_income ")
        print("Choose 2- add_expenses ")
        print("Choose 3- view_transactions ")
        print("Choose 4- view_balance")
        print("Choose 5- save_data ")
        print("Choose 6- load_data ")
        print("Choose 0- exit")
        choice = int(input("enter your choice-:"))
        match choice:
            case 1:
                add_income()
            case 2:
                add_expense()
            case 3:
                view_transactions()
            case 4:
                view_blance()
            case 5:
                file = input("enter the file_name")
                save_file(file)
            case 6:
                file = input("enter the file_name")
                load_file(file)
            case 0:
                break
            case _:
                print("enter a valid choice from 0 to 1")


main()
