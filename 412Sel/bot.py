#python bot.py

import telebot
import config
import random
from telebot import types
import sqlite3
import DerictoryList
import sqltablemode

#Описание бота, таблицы
bot=telebot.TeleBot(config.TOKEN)

connection = sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connection.cursor()



#Приветственное сообщение
@bot.message_handler(commands=['start'])

def welcome(message):
    sti=open('Cats/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    UserNameBase= message.from_user.username #имя пользователя
    sqltablemode.SQL_createNewTable(UserNameBase,'my_database.db')
    sqltablemode.Add_Sketch_in_table(UserNameBase, 'my_database.db', '/start')

    connection.commit()

#Клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/cats")
    item2 = types.KeyboardButton("/dogs")

    markup.add(item1, item2)

#Вывод приветсвенного сообщения
    bot.send_message(message.chat.id, "Привет, меня когда-нибудь изобретут и я смогу отпралвтяь котов. Попробуй команду /help".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)








#команда помощи

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/cats /dogs".format(message.from_user, bot.get_me()), parse_mode='html' )
    UserNameBase= message.from_user.username #имя пользователя
    sqltablemode.SQL_createNewTable(UserNameBase,'my_database.db')
    sqltablemode.Add_Sketch_in_table(UserNameBase, 'my_database.db', '/help')
    connection.commit()

#котики

@bot.message_handler(commands=['cats'])
def cat(message):
    Directory_list_file = DerictoryList.ListFor('Cats')
    number = random.randrange(0, len(Directory_list_file))
    link ='Cats' + '/' + Directory_list_file[number]
    pho=open(str(link), 'rb')

    bot.send_photo(message.chat.id, pho)
    UserNameBase= message.from_user.username #имя пользователя
    sqltablemode.SQL_createNewTable(UserNameBase,'my_database.db')
    sqltablemode.Add_Sketch_in_table(UserNameBase, 'my_database.db', '/cats')
    connection.commit()






#песики

@bot.message_handler(commands=['dogs'])

def dog(message):
    Directory_list_file = DerictoryList.ListFor('Dogs')
    number = random.randrange(0, len(Directory_list_file))
    link ='Dogs' + '/' + Directory_list_file[number]
    pho=open(str(link), 'rb')
    bot.send_photo(message.chat.id, pho)
    UserNameBase= message.from_user.username #имя пользователя
    sqltablemode.SQL_createNewTable(UserNameBase,'my_database.db')
    sqltablemode.Add_Sketch_in_table(UserNameBase, 'my_database.db', '/dogs')
    connection.commit()


#повторение сообщения если не котики и не песики

@bot.message_handler(content_types=["text"])
def lalala(message):
    bot.send_message(message.chat.id, message.text)
    UserNameBase= message.from_user.username
    MessageTextUser=message.text
    MessageTextUser = str(MessageTextUser)

    sqltablemode.SQL_createNewTable(UserNameBase,'my_database.db')
    sqltablemode.Add_Sketch_in_table(UserNameBase, 'my_database.db', MessageTextUser)
    connection.commit()



#RUNS
bot.polling(none_stop=True)


