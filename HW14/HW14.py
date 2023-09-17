import requests

bank_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
try:
    response = requests.get(bank_url)
except Exception as Exc:
    print(f'Error is {Exc}')
else:
    if 200 <= response.status_code < 300 and response.headers['Content-Type'] == 'application/json; charset=utf-8':
        currency_list = response.json()

        with open('currency.txt', 'w', encoding='utf-8') as file:
            file.write("[Дата, на яку актуальний курс]\n")

            for index, currency in enumerate(currency_list, start=1):
                currency_name = currency['txt']
                currency_rate = currency['rate']
                file.write(f"{index}. {currency_name} to UAH: {currency_rate}\n")

        print('Saved in currency.txt')
    else:
        print(f'Error {response.status_code}')
