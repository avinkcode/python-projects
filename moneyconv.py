currency = input("please select a type of currency from this list of currencies: USD,LKR,EUR,CNY,or INR| ")
convert = int(input("how much money would you like to convert| "))
if currency == "USD":
    convert1 = convert * 1
    print(f"${convert1} USD")
elif currency == "LKR":
    convert2 = convert * 335.50
    print(f"${convert2} USD")
elif currency == "EUR":
    convert3 = convert * 0.88
    print(f"${convert3} USD")
elif currency == "CNY":
    convert4 = convert * 6.80
    print(f"${convert4} USD")
elif currency == "INR":
    convert5 = convert * 95.55
    print(f"${convert5} USD")