
import telebot
from search_id import search_by_id
bot = telebot.TeleBot("TOKEN", parse_mode=None)



@bot.message_handler(commands=['start'])
def start_message(message):
    start_text = f'Привет, {message.from_user.first_name}! Введи ID'
    bot.send_message(message.chat.id, start_text)


@bot.message_handler(content_types=['text'])
def search(message):
    id = message.text  
    bot.send_message(message.chat.id,search_by_id(id))
        



if __name__ == '__main__':
    bot.polling()