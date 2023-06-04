import telebot


file_settings = open('E:\GB\Python\hwpy_1_7\settings.ini', mode='r', encoding='utf-8')
my_token = file_settings.read()
file_settings.close()
bot = telebot.TeleBot(my_token)

data_file = open('E:\\GB\Python\\hwpy_1_8\\usrmsg.txt', mode='r+', encoding='utf-8')
data_text = data_file.read()
print(str(data_text))

# usr_text = f'{message.from_user.id}:{message.text}\n'
# usrmsg_file.writelines(usr_text)
data_file.close()

# bot.send_message('694846592', 'Проверка отправки сообщений от Оператора')