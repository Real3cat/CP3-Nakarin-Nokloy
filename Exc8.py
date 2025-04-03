UsernameInput = input("Username :")
PasswordInput = input("Password :")
if (UsernameInput == "admin" and PasswordInput == "1111") or (UsernameInput == "nakarin" and PasswordInput == "1111"):
    print("Done !!!")
    print("-" * 20, "You can Select", "-" * 20)
    print("1. Vat Calculator")
    print("2. Price Calculator")
    print("3. Daily Interest")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Price (THB):"))
        vat = 7
        result = price + (price * vat / 100)
        print(f"Price after VAT: {result} THB")
    elif userSelected == 2:
        price1 = int(input("First Product Price :"))
        price2 = int(input("Second Product Price :"))
        print(f"Total Price: {price1 + price2} THB")
    elif userSelected == 3:
        Loan = int(input("Loan (THB): "))
        Rate = float(input("Rate (percentage per year): "))
        daily_interest = (Loan * (Rate / 100)) / 365
        print(f"Daily Interest: {daily_interest:.2f} THB")
    else:
        print("Invalid selection. Please select 1 or 2.")
else:
    print("Invalid username or password.")