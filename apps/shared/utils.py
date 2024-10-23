from typing import Optional

import requests


def get_dollar_currency() -> tuple[Optional[float], bool]:
    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for currency in data:
            if currency['Ccy'] == 'USD':
                usd_rate = float(currency['Rate'])
                return usd_rate, True
    return None, False
