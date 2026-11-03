from datetime import datetime
 
accounts = {
    "admin": "admin123",
    "cashier": "cashier123"
}
 
food_menu = {
    1: ("Rice", 15),
    2: ("Chicken", 50),
    3: ("Pork", 60),
    4: ("Fish", 45)
}
 
drink_menu = {
    1: ("Coke", 15),
    2: ("Royal", 15),
    3: ("Pepsi", 15)
}
 
transactions = []
 
 
while True:
 
    # LOGIN
    print("\n===== LOGIN =====")
    username = input("Username: ")
    password = input("Password: ")
 
    if username not in accounts or accounts[username] != password:
        print("Invalid login.")
        continue
 
    print("Login successful!")
 
    # CASHIER
    if username == "cashier":
 
        while True:
            print("\n===== CASHIER MENU =====")
            print("1. New Sale")
            print("2. Logout")
 
            choice = input("Choose: ")
 
            if choice == "2":
                break
 
            if choice != "1":
                print("Invalid choice.")
                continue
 
            total = 0
            items = []
 
            # ORDER
            while True:
                print("\n===== ORDER MENU =====")
                print("1. Food")
                print("2. Drinks")
                print("3. Preview Order")
                print("4. Remove Order")
                print("5. Finish Order")
 
                category = input("Choose: ")
 
                # FINISH ORDER
                if category == "5":
                    break
 
                # PREVIEW ORDER
                elif category == "3":
 
                    print("\n===== ORDER PREVIEW =====")
 
                    if len(items) == 0:
                        print("No items in the order.")
 
                    else:
                        print("--------------------------------")
                        print("No.  Item       Qty    Subtotal")
                        print("--------------------------------")
 
                        for number, item in enumerate(items, 1):
                            print(
                                number,
                                item[0],
                                "   x", item[1],
                                "   ₱", item[2]
                            )
 
                        print("--------------------------------")
                        print("Current Total: ₱", total)
 
                # REMOVE ORDER
                elif category == "4":
 
                    print("\n===== REMOVE ORDER =====")
 
                    if len(items) == 0:
                        print("No items to remove.")
 
                    else:
 
                        print("--------------------------------")
                        print("No.  Item       Qty    Subtotal")
                        print("--------------------------------")
 
                        for number, item in enumerate(items, 1):
                            print(
                                number,
                                item[0],
                                "   x", item[1],
                                "   ₱", item[2]
                            )
 
                        print("--------------------------------")
 
                        while True:
                            remove_input = input(
                                "Enter item number to remove (Press 0 to cancel): "
                            )
 
                            if remove_input == "0":
                                break
 
                            if remove_input.isdigit():
                                remove_number = int(remove_input)
 
                                if 1 <= remove_number <= len(items):
 
                                    removed_item = items.pop(
                                        remove_number - 1
                                    )
 
                                    total -= removed_item[2]
 
                                    print(
                                        removed_item[0],
                                        "removed from order."
                                    )
 
                                    break
 
                                else:
                                    print("Invalid item number.")
 
                            else:
                                print("Invalid input.")
 
                # FOOD MENU
                elif category == "1":
 
                    print("\n===== FOOD MENU =====")
 
                    for number, item in food_menu.items():
                        print(
                            number,
                            item[0],
                            "- ₱",
                            item[1]
                        )
 
                    item_choice = input(
                        "Item number (Press 0 to go back in order menu): "
                    )
 
                    if item_choice == "0":
                        continue
 
                    if item_choice.isdigit() and int(item_choice) in food_menu:
 
                        item_choice = int(item_choice)
 
                        while True:
                            quantity = input("Quantity: ")
 
                            if quantity.isdigit() and int(quantity) > 0:
                                quantity = int(quantity)
                                break
                            else:
                                print("Invalid quantity.")
 
                        name, price = food_menu[item_choice]
                        subtotal = price * quantity
 
                        total += subtotal
                        items.append(
                            (name, quantity, subtotal)
                        )
 
                        print("Item added.")
 
                    else:
                        print("Invalid item.")
 
                # DRINK MENU
                elif category == "2":
 
                    print("\n===== DRINK MENU =====")
 
                    for number, item in drink_menu.items():
                        print(
                            number,
                            item[0],
                            "- ₱",
                            item[1]
                        )
 
                    item_choice = input(
                        "Item number (Press 0 to go back in order menu): "
                    )
 
                    if item_choice == "0":
                        continue
 
                    if item_choice.isdigit() and int(item_choice) in drink_menu:
 
                        item_choice = int(item_choice)
 
                        while True:
                            quantity = input("Quantity: ")
 
                            if quantity.isdigit() and int(quantity) > 0:
                                quantity = int(quantity)
                                break
                            else:
                                print("Invalid quantity.")
 
                        name, price = drink_menu[item_choice]
                        subtotal = price * quantity
 
                        total += subtotal
                        items.append(
                            (name, quantity, subtotal)
                        )
 
                        print("Item added.")
 
                    else:
                        print("Invalid item.")
 
                else:
                    print("Invalid choice.")
 
            # CHECK IF ORDER IS EMPTY
            if total == 0:
                print("No order.")
                continue
 
            # PAYMENT
            print("\n===== PAYMENT =====")
            print("Total: ₱", total)
 
            while True:
                payment_input = input("Payment: ₱")
 
                try:
                    payment = float(payment_input)
 
                    if payment >= total:
                        break
                    else:
                        print("Insufficient payment.")
 
                except ValueError:
                    print("Invalid payment.")
 
            change = payment - total
 
            # DATE AND TIME
            date_time = datetime.now().strftime(
                "%Y-%m-%d %I:%M %p"
            )
 
            # RECEIPT
            print("\n")
            print("=" * 40)
            print("           TOYANS CARINDERIA")
            print("              RECEIPT")
            print("=" * 40)
 
            print("Date & Time:", date_time)
 
            print("-" * 40)
            print(
                f"{'Item':<15}"
                f"{'Qty':<6}"
                f"{'Subtotal':>12}"
            )
            print("-" * 40)
 
            for item in items:
                print(
                    f"{item[0]:<15}"
                    f"{item[1]:<6}"
                    f"₱{item[2]:>11.2f}"
                )
 
            print("-" * 40)
            print(f"{'TOTAL:':<21}₱{total:>11.2f}")
            print(f"{'PAYMENT:':<21}₱{payment:>11.2f}")
            print(f"{'CHANGE:':<21}₱{change:>11.2f}")
 
            print("=" * 40)
            print("        Thank you for your order!")
            print("=" * 40)
 
            # SAVE TRANSACTION
            transactions.append({
                "items": items,
                "total": total,
                "payment": payment,
                "change": change,
                "date_time": date_time
            })
 
            print("\nTransaction saved!")
 
 
    # ADMIN
    elif username == "admin":
 
        while True:
            print("\n===== ADMIN MENU =====")
            print("1. View Transactions")
            print("2. View Daily Sales")
            print("3. Logout")
 
            choice = input("Choose: ")
 
            if choice == "3":
                break
 
            # VIEW TRANSACTIONS
            if choice == "1":
 
                print("\n===== COMPLETED TRANSACTIONS =====")
 
                if len(transactions) == 0:
                    print("No completed transactions.")
 
                else:
 
                    print("-" * 92)
 
                    print(
                        f"{'No.':<5}"
                        f"{'Date & Time':<23}"
                        f"{'Items':<25}"
                        f"{'Total':<13}"
                        f"{'Payment':<13}"
                        f"{'Change':<13}"
                    )
 
                    print("-" * 92)
 
                    for number, transaction in enumerate(
                        transactions, 1
                    ):
 
                        item_summary = ""
 
                        for item in transaction["items"]:
                            item_summary += (
                                item[0]
                                + " x"
                                + str(item[1])
                                + ", "
                            )
 
                        item_summary = item_summary.rstrip(", ")
 
                        if len(item_summary) > 24:
                            item_summary = item_summary[:21] + "..."
 
                        print(
                            f"{number:<5}"
                            f"{transaction['date_time']:<23}"
                            f"{item_summary:<25}"
                            f"₱{transaction['total']:<12.2f}"
                            f"₱{transaction['payment']:<12.2f}"
                            f"₱{transaction['change']:<12.2f}"
                        )
 
                    print("-" * 92)
 
 
            # DAILY SALES
            elif choice == "2":
 
                print("\n===== DAILY SALES =====")
 
                print(
                    "Total Transactions:",
                    len(transactions)
                )
 
                print(
                    "Total Sales: ₱",
                    sum(
                        transaction["total"]
                        for transaction in transactions
                    )
                )
 
            else:
                print("Invalid choice.")
 
    print("\nLogged out.")
