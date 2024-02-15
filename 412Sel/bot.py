import telebot
import config
import random


bot=telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start'])

def welcome(message):
    sti=open('Cats/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "Привет, меня когда-нибудь изобретут и я смогу отпралвтяь котов. Попробуй команду /cats".format(message.from_user, bot.get_me()),
                     parse_mode='html')





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


@bot.message_handler(content_types=["text"])
def lalala(message):
    bot.send_message(message.chat.id, message.text)



#RUNS
bot.polling(none_stop=True)