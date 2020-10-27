from .bot import WhatABotChatBot


update_id = None
bot = WhatABotChatBot.build('1210283700:AAFmdd6DANUtFTnK9cuiTvF25RZ5VYzpHUA')

def make_reply(message):
    return message

while True:
    print('...')
    
    updates = bot.get_updates(offset=update_id)
    print(updates)
    if updates['result']:
        for item in updates['result']:
            update_id = item['update_id']

            try:
                message = item['message']['text']
            except:
                message = None

            from_ = item['message']['from']['id']
            reply = make_reply(message)
            bot.send_message(reply, from_)