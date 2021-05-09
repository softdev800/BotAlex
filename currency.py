
# -*- coding: utf-8 -*-


from urllib import request

import json


def cur_view(url, currency_code, bot, message):

    with request.urlopen(url) as url:
        data = json.loads(url.read().decode())

        if data['success']:
            msg = ''

            for key, value in data['rates'].items():
                total = '{:20,.2f}'.format(value).strip()
                number = total.replace(',', ' ')
                msg += f"{currency_code} - {key}: {number}\n"

            bot.send_message(message.chat.id, msg)
        else:
            bot.send_message(message.chat.id, "Запрос не успешен попробуйте ещё раз!")


def eur(bot, message):
    url = 'https://api.exchangerate.host/latest?symbols=USD,RUB,UZS'
    cur_view(url, "EUR", bot, message)


def usd(bot, message):
    url = 'https://api.exchangerate.host/latest?base=USD&symbols=RUB,EUR,UZS'
    cur_view(url, "USD", bot, message)
