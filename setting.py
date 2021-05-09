
# -*- coding: utf-8 -*-


from telebot import types

import core


def start(bot, message, msg):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Умный бот', ' Меню')
    bot.send_message(message.chat.id, msg, reply_markup=keyboard)


def button_smart_bot(bot, message):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Начат разговаривать', 'Назад')
    bot.send_message(message.chat.id, "Начните диалог с умным ботом", reply_markup=keyboard)


def button_started_talking(bot, message):
    bot.send_message(message.chat.id, "Привет скажите мне что нибудь, и я отвечу вам!")


def button_menu(bot, message):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Курс валюты', 'Погода')
    keyboard.row('Анекдот', 'Назад')
    bot.send_message(message.chat.id, "Выберите раздел который вас интересует", reply_markup=keyboard)


def button_currency(bot, message):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('EUR', 'USD')
    keyboard.row('Назад')
    bot.send_message(message.chat.id, "Выберите валюту", reply_markup=keyboard)


def button_weather(bot, message):
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Берлин', 'Вашингтон')
    keyboard.row('Москва', 'Ташкент')
    keyboard.row('Назад')
    bot.send_message(message.chat.id, "Выберите город", reply_markup=keyboard)


def start_dialog_flow(bot, message):
    language_code = 'ru'
    text = message.text
    response = core.get_response(text, language_code)

    try:
        msg = response.query_result.fulfillment_text
    except ValueError:
        msg = "Я Вас не совсем понял!"
    bot.send_message(message.chat.id, text=msg)
