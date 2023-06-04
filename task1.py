# Задача 1. Напишите бота для техподдержки. 
# Бот должен записывать обращения пользователей в файл.
import datetime
import telebot


file_settings = open('E:\GB\Python\hwpy_1_7\settings.ini', mode='r', encoding='utf-8')
my_token = file_settings.read()
file_settings.close()
bot = telebot.TeleBot(my_token)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Добро пожаловать в чат тех.поддержки!")

@bot.message_handler(content_types='text')
def message_reply(message):
    usrmsg_file = open('E:\\GB\Python\\hwpy_1_8\\usrmsg.txt', mode='a', encoding='utf-8')
    usr_text = f'{message.from_user.id}:{message.text}\n'
    usrmsg_file.writelines(usr_text)
    usrmsg_file.close()
    bot.send_message(message.from_user.id,'Ваше сообщение передано в тех. поддержку.')

bot.polling()