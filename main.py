import telebot

bot = telebot.TeleBot('YOUR BOT TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    global rost, rost_int, ves_int, flag
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!\nЭтот бот создан чтобы узнать твой ИМТ (индекс массы тела). Чтобы начать подсчеты, напиши свой рост одним числом')
    ves_int = 1
    rost_int = 1
    rost = False 
    flag = True  
flag = True

def delete(message):
        bot.delete_message(message.chat.id, message.id-1)
        bot.delete_message(message.chat.id, message.id)
@bot.message_handler()
def reply(message):
    global rost, rost_int, ves_int, flag
    
    if flag:
        text = message.text.lower() #сообщение от пользователя
        sort = ''
        rost_int = 0
        for char in text:
            if char.isdigit():
                sort = sort + char
            else:
                if sort != '':
                    rost_int = (int(sort))
                    sort = ''
        if sort != '':
            rost_int = (int(sort))        
        if rost_int != '' or rost_int != '.' or rost_int != ',': #Функция роста
            delete(message)
            bot.send_message(message.chat.id, f'''Теперь отправь свой вес в киллограммах \nТвой рост равен {rost_int}, если ошибся отправь /start''')
        rost = False
        flag = False

    elif rost == False: #Функция веса
        text_v = message.text.lower() #сообщение от пользователя
        sort_v = ''
        for char in text_v:
            if char.isdigit():
                sort_v = sort_v + char
            else:
                if sort_v != '':
                    ves_int = (int(sort_v))
                    sort_v = ''
        if sort_v != '':
            ves_int = (int(sort_v))
        delete(message)
        if rost_int == 0:
            bot.send_message(message.chat.id, f'Жди докс даун, или пиши /start')
        else:
            if ves_int != 0 or rost_int != 0:
                imt = ves_int/(rost_int*rost_int/10000)
            else:
                bot.send_message(message.chat.id, 'Жди докс даун (/start)')
            file = open(r'G:/Del/bot/IMT/photo1.jpg', 'rb')
            bot.send_photo(message.chat.id, file, )
            bot.send_message(message.chat.id, f'Твой ИМТ {(round(imt, 1))}. Если надо пересчитать пиши /start')
            ves_int = 0
            rost_int = 0
            flag = True
            rost = False           
bot.polling(none_stop=True)