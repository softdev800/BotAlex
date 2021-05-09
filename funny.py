
# -*- coding: utf-8 -*-


from random import choice


funny_list = []


def init(bot, message):
    with open('data_source/anecdotes.txt', encoding='utf-8') as f:
        content = f.read()
        funny_list = content.split("==========")

    msg = choice(funny_list)
    bot.send_message(message.chat.id, msg, "\n🤣🤣🤣")
