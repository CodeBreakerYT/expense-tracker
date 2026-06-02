import json

fn = "expenses.json"

try:
    with open(fn, "r") as f:
        exp = json.load(f)
except:
    exp = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Spending")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        item = input("Enter item: ")
        amt = float(input("Enter amount: "))

        exp.append({
            "item": item,
            "amount": amt
        })

        with open(fn, "w") as f:
            json.dump(exp, f)

        print("Expense Added")

    elif ch == "2":
        if len(exp) == 0:
            print("No Expenses")
        else:
            for i in range(len(exp)):
                print(i + 1, exp[i]["item"], "-", exp[i]["amount"])

    elif ch == "3":
        if len(exp) == 0:
            print("No Expenses")
        else:
            for i in range(len(exp)):
                print(i + 1, exp[i]["item"], "-", exp[i]["amount"])

            n = int(input("Enter expense number: "))

            if 1 <= n <= len(exp):
                exp.pop(n - 1)

                with open(fn, "w") as f:
                    json.dump(exp, f)

                print("Expense Deleted")
            else:
                print("Invalid Number")

    elif ch == "4":
        total = 0

        for e in exp:
            total += e["amount"]

        print("Total Spending =", total)

    elif ch == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")