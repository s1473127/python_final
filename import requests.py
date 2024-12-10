import requests

def currency_info():
    currency_search = input("What currency are you interested in? ")
    response = requests.get(f'https://restcountries.com/v3.1/currency/{currency_search}')
    response_dict = response.json()
    
    if len(response_dict) > 0:
        print(f"Found {len(response_dict)} countries using this currency:")
        print('These countries use this currency:')
        for country in response_dict:
            print(country['name']['official'])
        convert_currency(currency_search)
    else:
        print(f"No countries found using the currency {currency_search}")

def convert_currency(currency):
    amount = float(input(f"Enter the amount in {currency}: "))
    response = requests.get(f'https://api.frankfurter.app/latest?amount={amount}&from={currency}&to=USD')
    if response.status_code == 200:
        data = response.json()
        usd_amount = data['rates']['USD']
        print(f"{amount} {currency} = {usd_amount} USD")
    else:
        print(f"Failed to fetch the exchange rate for {currency} to USD.")

while True:
    currency_info()
    respond = input('Can I help with something else? ')
    if respond.lower() == 'no':
        print('Thank you, have a nice day!')
        break
    else:
        print(f"Would you like to know the current USD exchange rate?")
