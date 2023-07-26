from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount

if __name__ == "__main__":
    try:
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the currency code to convert from (e.g., USD): ").upper()
        to_currency = input("Enter the currency code to convert to (e.g., EUR): ").upper()

        converted_amount = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")
