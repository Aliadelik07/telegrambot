import requests
import datetime
from Eliza import Eliza
from Bothandler import bothandler


token = '1314285111:AAEuXFO8K-dHcw_eIAoGX7bvyi3dtdJxW_A'
Ade = BotHandler(token)

therapist = Eliza()

def main():
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates=Ade.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                    first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                if first_chat_text == "/start":
                    Ade.send_message(first_chat_id, 'my name is Ade ' + first_chat_name + '. How are you feeling today?')
                    new_offset = first_update_id + 1
                else:
                    Ade.send_message(first_chat_id, therapist.respond(first_chat_text))
                    new_offset = first_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()