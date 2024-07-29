import telebot

bot = telebot.TeleBot('7442845832:AAH_cEI6x2vXSepI5Wc8SBu9gjoA3NpXcAM')

@bot.message_handler(commands=['start'])
def main (message):
    bot.send_message(message.chat.id,'Привет!')



bot.polling(none_stop=True)