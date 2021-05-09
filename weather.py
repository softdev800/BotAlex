
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup as BS
from datetime import date

import requests


def berlin(bot, message):
    url = requests.get(
        'https://sinoptik.ua/'
        '%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B1%D0%B5%D1%80%D0%BB%D0%B8%D0%BD-102950159'
    )
    html = BS(url.content, 'html.parser')

    if url:
        for el in html.select('#header'):
            name = el.select('.cityName h1')[0].text

        for el in html.select('#content'):
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text
            desc = el.select('.wDescription .description')[0].text
            data = date.today()

            msg = f"{data}\n" \
                  f"\n{name.upper().strip()}\n" \
                  f"\n{t_min}\n" \
                  f"{t_max}\n" \
                  f"\n{desc.strip()}"

        bot.send_message(message.chat.id, msg)
    else:
        bot.send_message(message.chat.id, "Запрос не успешен попробуйте ещё раз!")


def washington(bot, message):
    url = requests.get(
        'https://sinoptik.ua/'
        '%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B2%D0%B0%D1%88%D0%B8%D0%BD%D0%B3%D1%82%D0%BE%D0%BD-104140963'
    )
    html = BS(url.content, 'html.parser')

    if url:
        for el in html.select('#header'):
            name = el.select('.cityName h1')[0].text

        for el in html.select('#content'):
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text
            desc = el.select('.wDescription .description')[0].text
            data = date.today()

            msg = f"{data}\n" \
                  f"\n{name.upper().strip()}\n" \
                  f"\n{t_min}\n" \
                  f"{t_max}\n" \
                  f"\n{desc.strip()}"

        bot.send_message(message.chat.id, msg)
    else:
        bot.send_message(message.chat.id, "Запрос не успешен попробуйте ещё раз!")


def moscow(bot, message):
    url = requests.get(
        'https://sinoptik.ua/'
        '%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0'
    )
    html = BS(url.content, 'html.parser')

    if url:
        for el in html.select('#header'):
            name = el.select('.cityName h1')[0].text

        for el in html.select('#content'):
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text
            desc = el.select('.wDescription .description')[0].text
            data = date.today()

            msg = f"{data}\n" \
                  f"\n{name.upper().strip()}\n" \
                  f"\n{t_min}\n" \
                  f"{t_max}\n" \
                  f"\n{desc.strip()}"

        bot.send_message(message.chat.id, msg)
    else:
        bot.send_message(message.chat.id, "Запрос не успешен попробуйте ещё раз!")


def tashkent(bot, message):
    url = requests.get(
        'https://sinoptik.ua/'
        '%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%82%D0%B0%D1%88%D0%BA%D0%B5%D0%BD%D1%82'
    )
    html = BS(url.content, 'html.parser')

    if url:
        for el in html.select('#header'):
            name = el.select('.cityName h1')[0].text

        for el in html.select('#content'):
            t_min = el.select('.temperature .min')[0].text
            t_max = el.select('.temperature .max')[0].text
            desc = el.select('.wDescription .description')[0].text
            data = date.today()

            msg = f"{data}\n" \
                  f"\n{name.upper().strip()}\n" \
                  f"\n{t_min}\n" \
                  f"{t_max}\n" \
                  f"\n{desc.strip()}"

        bot.send_message(message.chat.id, msg)
    else:
        bot.send_message(message.chat.id, "Запрос не успешен попробуйте ещё раз!")
