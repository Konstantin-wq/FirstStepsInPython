
import telebot
from create_polinom import first_polynom_input, second_polynom_input
from sum import sum_polinoms
import re

bot = telebot.TeleBot('Token', parse_mode=None)

polinom1 = open('TenthSeminarTask\\polinom1.txt')
polinom2 = open('TenthSeminarTask\\polinom2.txt')
result = open('TenthSeminarTask\\result_sum.txt')


@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id

    start_text = f'Привет, {message.from_user.first_name}! Бот для сложения полиномов'

    bot.send_message(message.chat.id, start_text)
    text = bot.send_message(chat_id, "Введите коэффициенты первого полинома")
    bot.register_next_step_handler(text, first_amount_of_elems)


def first_amount_of_elems(message):
    chat_id = message.chat.id
    next_text = bot.send_message(message.chat.id, "Полученный полином №1")

    elements = re.split(' ', message.text)
    elems = []

    for i in elements:
        if i.isdigit:
            elems.append(i)
    first_polynom_input(elems)
    bot.send_message(message.chat.id, polinom1)
    bot.send_message(chat_id, "Введите коэффициенты второго полинома:")
    bot.register_next_step_handler(next_text, second_amount_of_elems)


def second_amount_of_elems(message):
    elements = re.split(' ', message.text)
    elems = []
    chat_id = message.chat.id
    #next_text = bot.send_message(chat_id,"Результат" )
    for i in elements:
        if i.isdigit:
            elems.append(i)
    second_polynom_input(elems)
    answ_text = bot.send_message(chat_id, "Полученный полином №2:")
    bot.send_message(message.chat.id, polinom2)
    sum_polinoms()
    next_text = bot.send_message(chat_id, "Результат сложения полиномов:")
    bot.send_message(message.chat.id, result)


if __name__ == '__main__':
    bot.polling()
