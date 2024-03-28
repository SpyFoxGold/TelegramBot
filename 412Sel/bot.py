import telebot
import config
import random
from telebot import types
import sqlite3


#Описание бота, таблицы
bot=telebot.TeleBot(config.TOKEN)

connection = sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connection.cursor()



#Приветственное сообщение
@bot.message_handler(commands=['start'])

def welcome(message):
    sti=open('Cats/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    UserNameBase= message.from_user.username
    cursor.execute('INSERT INTO Users (username, request) VALUES (?, ?)', (str(UserNameBase), '/start'))
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
    UserNameBase= message.from_user.username
    cursor.execute('INSERT INTO Users (username, request) VALUES (?, ?)', (str(UserNameBase), '/help'))
    connection.commit()

#котики
    
@bot.message_handler(commands=['cats'])
def cat(message):
    number = random.randrange(1, 10)
    if number==1:
        pho=open('Cats/1.jpg', 'rb')
    elif number==2:
        pho=open('Cats/2.jpeg', 'rb')
    elif number==3:
        pho=open('Cats/3.jpeg', 'rb')
    elif number==4:
        pho=open('Cats/4.jpg', 'rb')
    elif number==5:
        pho=open('Cats/5.jpg', 'rb')
    elif number==6:
        pho=open('Cats/6.jpg', 'rb')
    elif number==7:
        pho=open('Cats/7.jpg', 'rb')
    elif number==8:
        pho=open('Cats/8.jpg', 'rb')
    elif number==9:
        pho=open('Cats/9.jpg', 'rb')
    elif number==10:
        pho=open('Cats/10.jpeg', 'rb')
    bot.send_photo(message.chat.id, pho)
    UserNameBase= message.from_user.username
    cursor.execute('INSERT INTO Users (username, request) VALUES (?, ?)', (str(UserNameBase), '/cats'))
    connection.commit()

#песики

@bot.message_handler(commands=['dogs'])

def dog(message):
    number1 = random.randrange(1, 10)
    if number1==1:
        phot=open('Dogs/1.jpg', 'rb')
    elif number1==2:
        phot=open('Dogs/2.jpg', 'rb')
    elif number1==3:
        phot=open('Dogs/3.jpg', 'rb')
    elif number1==4:
        phot=open('Dogs/4.jpg', 'rb')
    elif number1==5:
        phot=open('Dogs/5.jpg', 'rb')
    elif number1==6:
        phot=open('Dogs/6.jpg', 'rb')
    elif number1==7:
        phot=open('Dogs/7.jpg', 'rb')
    elif number1==8:
        phot=open('Dogs/8.jpg', 'rb')
    elif number1==9:
        phot=open('Dogs/9.jpg', 'rb')
    elif number1==10:
        phot=open('Dogs/10.jpg', 'rb')
    bot.send_photo(message.chat.id, phot)
    UserNameBase = message.from_user.username
    print(UserNameBase)
    cursor.execute('INSERT INTO Users (username, request) VALUES (?, ?)', (str(UserNameBase), '/dogs'))
    connection.commit()


#повторение сообщения если не котики и не песики

@bot.message_handler(content_types=["text"])
def lalala(message):
    bot.send_message(message.chat.id, message.text)
    UserNameBase= message.from_user.username

    MessageTextUser=message.text
    cursor.execute('INSERT INTO Users (username, request) VALUES (?, ?)', (str(UserNameBase), MessageTextUser))
    connection.commit()



#RUNS
bot.polling(none_stop=True)

#connection.close()