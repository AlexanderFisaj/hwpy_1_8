# Задача 2. Напишите программу, которая позволяет считывать из файла вопрос, 
# отвечать на него и отправлять ответ обратно пользователю.
# 846775178

import telebot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


file_settings = open('E:\GB\Python\hwpy_1_7\settings.ini', mode='r', encoding='utf-8')
my_token = file_settings.read()
file_settings.close()
bot = telebot.TeleBot(my_token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Добро пожаловать в чат тех.поддержки!")
    
    def start(update, context):
        # Отправляет приветственное сообщение пользователю
        context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот для ответов на вопросы.")

    def help(update, context):
        # Отправляет сообщение со списком доступных команд
        text = "Список доступных команд:\n/start - начать диалог\n/help - показать список команд"
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    def answer_question(update, context):
    # Обрабатывает вопрос пользователя и отправляет ответ
        question = update.message.text
        answer = get_answer(question) # функция для получения ответа на вопрос
        context.bot.send_message(chat_id=update.effective_chat.id, text=answer)

    def main():
        # Создает экземпляр бота и запускает обработчики сообщений
        # updater = Updater(token='YOUR_TOKEN', use_context=True) # заменить YOUR_TOKEN на токен бота
        dispatcher = Updater.dispatcher

        start_handler = CommandHandler('start', start)
        help_handler = CommandHandler('help', help)
        question_handler = MessageHandler(Filters.text & ~Filters.command, answer_question)

        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(help_handler)
        dispatcher.add_handler(question_handler)

        Updater.start_polling()
        Updater.idle()
    
    if __name__ == '__main__':
        main()

bot.polling()