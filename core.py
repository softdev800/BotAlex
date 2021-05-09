
# -*- coding: utf-8 -*-


import dialogflow
import os


config = {
    'bot_name': 'AlexBot',
    'bot_url': '@alex_talk_bot',
    'bot_token': '735047848:AAG7djpfQJGPgOXIKGk4ekd7_z72TpXzLZc',
    'project_id': 'my-small-talk-bot-cjvcrr',
    'session_id': 'MYSMALLTALKBOTAISESSION'
}


def get_response(text, language_code):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join('data_source', 'my-small-talk-bot.json')
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(config['project_id'], config['session_id'])
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    return response
