import requests


def get_usd_rate():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = response.json()
    usd_rate = data['Valute']['USD']['Value']
    return usd_rate