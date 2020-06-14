import logging as log
import telebot
from datetime import datetime

import urls_loader as ul
from  helpers import set_logger 


BOT_TOKEN = '901113125:AAGYLh2t4p8NJOUJl9fQ2-Zo9ryYgyumBuQ'


CONFIG_CAT = {'stop_list':[],
              'query_list':['cats', 
                            'cats fun'],
              'urls_count': 5,
              'default_url': 'https://static.scientificamerican.com/sciam/cache/file/92E141F8-36E4-4331-BB2EE42AC8674DD3_source.jpg'}


CONFIG_DOG = {'stop_list':[],
              'query_list':['dogs humor', 
                            'dogs fun'],
              'urls_count': 5,
              'default_url': 'https://i.ytimg.com/vi/evrcmOxTKxM/maxresdefault.jpg'}


if __name__ == '__main__':

    log = set_logger(log)
    bot = telebot.TeleBot(BOT_TOKEN)
    log.info("STARTED BOT")

    @bot.message_handler(commands=['start'])
    def start_message(message):

        bot.send_message(message.chat.id, "Hi! Write 'cat' or 'dog' to get fun picture with it")
        log.info("User {} {} started session".format(message.from_user.first_name, message.from_user.last_name))


    @bot.message_handler(content_types=['text'])
    def send_text(message):

        #################################################

        if message.text.lower() == 'cat':

            urls = ul.get_urls_to_show(CONFIG_CAT)

            for url in urls:
                print(url)

                try:
                    bot.send_photo(message.chat.id, url)
                    log.info("User {} {} get CAT".format(message.from_user.first_name, message.from_user.last_name))
                    break
                except Exception as e:
                    print(e)
                    continue
            
                bot.send_photo(message.chat.id, CONFIG_CAT['default_url'])
                bot.send_message(message.chat.id, 'Cant send image "cat", default sent')
                log.error("User {} {} failed to load CAT".format(message.from_user.first_name, message.from_user.last_name))

        #################################################

        elif message.text.lower() == 'dog':

            urls = ul.get_urls_to_show(CONFIG_DOG)

            for url in urls:
                print(url)

                try:
                    bot.send_photo(message.chat.id, url)
                    log.info("User {} {} get DOG".format(message.from_user.first_name, message.from_user.last_name))
                    break
                except Exception as e:
                    print(e)
                    continue

                bot.send_photo(message.chat.id, CONFIG_DOG['default_url'])
                bot.send_message(message.chat.id, 'Cant send image "dog", default sent')
                log.error("User {} {} failed to load DOG".format(message.from_user.first_name, message.from_user.last_name))


        else:
            bot.send_message(message.chat.id, 'Can\'t understand you, sorry!')
            log.info("User {} {} sent unknown command: {}".format(message.from_user.first_name, message.from_user.last_name, message.text))

        #################################################
        

    bot.polling()



