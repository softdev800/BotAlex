
# -*- coding: utf-8 -*-


import telebot
import currency
import setting
import weather
import funny
import core


start_dialog_flow = False
bot = telebot.TeleBot(core.config['bot_token'], parse_mode=None)

my_messages = {
    'Привет': 'Здравствуйте!',
    'Назад': 'Чтобы продолжить выберите раздел внизу!'
}


@bot.message_handler(commands=['start', 'menu'])
def send_welcome(message):

    global start_dialog_flow
    menu_name = message.text

    if menu_name == '/start':
        msg = my_messages['Привет']
    else:
        msg = my_messages['Назад']

    setting.start(bot, message, msg)


@bot.message_handler(func=lambda m: True)
def general_manager(message):

    global start_dialog_flow
    text = message.text

    if text == 'Назад':
        start_dialog_flow = False
        setting.start(bot, message, my_messages['Назад'])
    elif text == 'Начат разговаривать':
        start_dialog_flow = True
        setting.button_started_talking(bot, message)
    elif start_dialog_flow:
        setting.start_dialog_flow(bot, message)
    elif text == 'Умный бот':
        setting.button_smart_bot(bot, message)
    elif text == 'Меню':
        setting.button_menu(bot, message)
    elif text == 'Курс валюты':
        setting.button_currency(bot, message)
    elif text == 'EUR':
        currency.eur(bot, message)
    elif text == 'USD':
        currency.usd(bot, message)
    elif text == 'Погода':
        setting.button_weather(bot, message)
    elif text == 'Берлин':
        weather.berlin(bot, message)
    elif text == 'Вашингтон':
        weather.washington(bot, message)
    elif text == 'Москва':
        weather.moscow(bot, message)
    elif text == 'Ташкент':
        weather.tashkent(bot, message)
    elif text == 'Анекдот':
        funny.init(bot, message)


bot.polling()
