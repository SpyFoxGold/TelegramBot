import telebot               #работа бота
import config   #Хранение токена и пароля
from telebot import types   #работа кнопок бота
from myapp import DirectoryList, sqltablemode
import random
import os

bot=telebot.TeleBot(config.TOKEN)





@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ITEM=[]
    AnimalList = DirectoryList.AnimalList() #Поулчаем список животных
    for i in range(0, len(AnimalList)):
        ITEM.append(i)
        ITEM[i] = types.KeyboardButton(AnimalList[i])
        markup.add(ITEM[i])
    ITEM_random = types.KeyboardButton("Random")
    markup.add(ITEM_random)


    Name = str(message.from_user.username)
    sqltablemode.SQL_createNewTable(Name, 'userdata.db') #создали вкладку в userdata
    sqltablemode.Add_Sketch_in_userdata('userdata.db',Name,  '/start') #Записали инфу в userdata



    bot.send_message(message.chat.id, "Привет, я могу отправить тебе фотографии различных животных, кого бы ты хотел увидеть?".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)




@bot.message_handler(content_types=["text"])
def cat(message):
    Name = str(message.from_user.username)
    messagetext = str(message.text).capitalize()
    sqltablemode.SQL_createNewTable(Name, 'userdata.db') #создали вкладку в userdata
    sqltablemode.Add_Sketch_in_userdata('userdata.db',Name,  messagetext) #Записали инфу в userdata

    Anima =  str(message.text).capitalize()
    AnimalList = DirectoryList.AnimalList()
    if Anima=="Random":
        RaNdOm=random.randrange(0, len(AnimalList))
        Anima = AnimalList[RaNdOm]
    if os.path.exists(DirectoryList.PathFor(Anima))==True:

        Directory_list_file = DirectoryList.ListFor(Anima)
        number = random.randrange(0, len(Directory_list_file))
        link =DirectoryList.PathFor(Anima) + '/' + Directory_list_file[number]
        pho=open(str(link), 'rb')

        bot.send_photo(message.chat.id, pho)
    else:
        bot.send_message(message.chat.id, "Ой ой, кажется ты что-то не то написал".format(message.from_user, bot.get_me()),
                         parse_mode='html')





bot.polling(none_stop=True)
