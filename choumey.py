import random
from currency_converter import CurrencyConverter
import telebot
from telebot import types
from telebot.types import WebAppInfo 
import webbrowser 
from datetime import datetime
from datetime import date
import pytz



bot = telebot.TeleBot("6321476517:AAFxDFhb-itchAUzBbN4lnX40kKPExsbRPE")
API = "f00af4e16194b66ebe88b943973ed633"

currency = CurrencyConverter()


name = None
string1 = "эм чо спезданул"
string2 = "ну ти папутал чоли бош"
string3 = "эм варишку прикрой"
string4 = "чоза высеры пошли😒"
string = [string1, string2]
ant1 = "ну пайдет"
ant2 = "крута оч крута ыы😁"
ant3 = "хирова😒"
ant = [ant1, ant2, ant3]
stri1 = None 
stri2 = "мя надеюсь😘"
stri = [stri1, stri2]
amount = 0

@bot.message_handler(commands = ["website"])
def website(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("open a web", web_app=WebAppInfo(url="https://choumey.github.io")))
    markup.add(types.InlineKeyboardButton("back"))
    bot.send_message(message.chat.id, "here we go", reply_markup=markup)
    
@bot.message_handler(commands = ["help"])
def main(message):
    bot.send_message(message.chat.id, "<em>находится в разработке</em><b><u> великого чоумея</u></b>", parse_mode = "html")


@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, f"Приветствую, {message.from_user.first_name}")

@bot.message_handler(commands = ["convert"])
def start(message):
    bot.send_message(message.chat.id, f"{message.from_user.first_name}, укажите сумму")
    bot.register_next_step_handler(message, summa)
def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, "Неверный формат\nвведите сумму:")
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width = 2)
        btn1 = types.InlineKeyboardButton("USD/EUR", callback_data = "usd/eur") 
        btn2 = types.InlineKeyboardButton("EUR/USD", callback_data = "eur/usd") 
        btn3 = types.InlineKeyboardButton("EUR/GBP", callback_data = "eur/gbp") 
        btn4 = types.InlineKeyboardButton("другой курс", callback_data = "else")   
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, "Выберите пару валют:", reply_markup = markup)
    else: 
        bot.send_message(message.chat.id, "не коректный запрос\nвведите сумму больше нуля:")
        bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func = lambda call: True)
def callback_convert(call):
    if call.data != "else":
        values = call.data.upper().split("/")
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f"Получается: {round(res, 2)}")
    else:
        bot.send_message(call.message.chat.id, "Введите пару значений через слеш")
        bot.register_next_step_handler(call.message, my_currency)
def my_currency(message):
    try:
        values = message.text.upper().split("/")
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f"Получается: {round(res, 2)}")
    except Exception:
        bot.send_message(message.chat.id, "что-то не так..\nвпишите значение заново:")
        bot.register_next_step_handler(message, my_currency)
@bot.message_handler(commands=['reply'])
def selfmyself(message):
    service = telebot.types.ReplyKeyboardMarkup(True, True)
    service.row('чоми сайт')
    service.row('чоми анекдот')
    service.row('чоми дата')
    service.row('чоми время')
    bot.send_message(message.chat.id, 'Что будем делать?', reply_markup=service)

# @bot.message_handler(content_types=["photo"])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()   
#     markup.add(types.InlineKeyboardButton("удалить наху", callback_data = "delete"))
#     markup.add(types.InlineKeyboardButton("го редачить", callback_data = "edit"))
#     bot.reply_to(message, "уф я заценил", reply_markup = markup)
    
    

# @bot.callback_query_handler(func = lambda callback: True)
# def callback_message(callback):
#     if callback.data == "delete":
#         pass
#         if callback.from_user.id == 1177268972:
#             bot.delete_message(callback.message.chat.id, callback.message.message_id)
#         else:
#             bot.send_message(callback.message.chat.id, "ни тепе удалять дазволено")
#     elif callback.data == "edit":
#         pass
#         if callback.from_user.id == 1177268972:
#             bot.edit_message_text("словесни панос", callback.message.chat.id, callback.message.message_id)
#         else:
#             bot.send_message(callback.message.chat.id, "ни тепе редачить дазволено")
    

# @bot.message_handler(content_types=["audio"])
# def get_audio(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("удалить ", callback_data = "delete"))
#     markup.add(types.InlineKeyboardButton("го редачить", callback_data = "edit"))
#     bot.reply_to(message, "музик кайфи брад", reply_markup = markup)

# @bot.callback_query_handler(func = lambda callback: True)
# def callback_message(callback):
#     if callback.data == "delete":
#         pass
#         if callback.from_user.id == 1177268972:
#             bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#         else:
#             bot.send_message(callback.message.chat.id, "ни тепе удалять дазволено")
#     elif callback.data == "edit":
#         pass
#         if callback.from_user.id == 1177268972:
#             bot.edit_message_text("словесни панос", callback.markup.message.chat.id, callback.message.message_id)
#         else:
#             bot.send_message(callback.message.chat.id,  "ни тепе редачить дазволено")
@bot.message_handler()
def info(message):
    if message.text.lower() == "чоми":
        bot.send_message(message.chat.id, "хуеми бебебе")
    elif message.text.lower() == "скучно":
        bot.reply_to(message, "пойди убейся")
    elif message.text.lower() == "чоми как дела":
        bot.send_message(message.chat.id, random.choice(ant))
    elif message.text.lower() == "айди":
        bot.reply_to(message, f"Id: {message.from_user.id}")
    elif message.text.lower() == "сам":
        bot.send_message(message.chat.id, "сам")
    elif message.text.lower() == "чурка":
        bot.reply_to(message, "дина")
    elif message.text.lower() == "чоми к ноге":
        pass
        if message.from_user.id == 1177268972:
            bot.reply_to(message, "да гаспадин")
        else:
            bot.send_message(message.chat.id, "чоза лох ришил камандывать🤨")
    elif message.text.lower() == "споки ночи":
        bot.send_message(message.chat.id, "споке ночи чату :)")
    elif message.text.lower() == "чоми чо делаешь":
        d1 = "ничо, а ти"
        d2 = "жду кодировки ебучего разраба\nзаєбал ничо не делать уше"
        d = [d1, d2]
        bot.send_message(message.chat.id, random.choice(d))
    elif message.text.lower() == "чоми что делаешь":
        d1 = "ничо, а ти"
        d2 = "жду кодировки ебучего разраба\nзаєбал ничо не делать уше"
        d = [d1, d2]
        bot.send_message(message.chat.id, random.choice(d))
    elif message.text.lower() == "рандом 0 100":
        bot.reply_to(message, random.randrange(0,100))
    elif message.text.lower() == "рандом 100 200":
        bot.reply_to(message, random.randrange(100,200))
    elif message.text.lower() == "рандом 200 300":
        bot.reply_to(message, random.randrange(200,300))
    elif message.text.lower() == "рандом":
        bot.reply_to(message, random.randrange(0,100000000))
    #elif message.text.lower() == "номер1":
        #bot.reply_to(message, f"0953848872, {message.from_user.first_name}, вот номер1 насти")
    #elif message.text.lower() == "номер2":
        #bot.reply_to(message, f"0936219707, {message.from_user.first_name}, вот номер2 насти")
    elif message.text.lower() == "тиха":
        bot.reply_to(message, "громка")
    elif message.text.lower() == "динаху":
        bot.reply_to(message, "цыц")
    elif message.text.lower() == "чо":
        bot.reply_to(message, "аничо")

    elif message.text.lower() == "кто я":
            pass
            if message.from_user.id == 1177268972:
                bot.reply_to(message, f"ты вроде {message.from_user.first_name}\nтвое айди и угадывать не нужно эт {message.from_user.id}\nну и крч ты клутои дядя ну а ваще я щучу в ротек тя манал")
            else:
               bot.reply_to(message, f"ты вроде {message.from_user.first_name}\nтвое айди и угадывать не нужно эт {message.from_user.id}\nну и крч ты обычный смертный походу")
    elif message.text.lower() == "чоми хуесос":
         bot.reply_to(message, random.choice(string))
    elif message.text.lower() == "чоми заебал":
        bot.reply_to(message, "а")
    elif message.text.lower() == "хуй на":
        bot.reply_to(message, "ловлю")
    elif message.text.lower() == "я ебал":
        bot.reply_to(message, random.choice(stri))
    elif message.text.lower() == "чоми накинь музики":
        bot.reply_to(message, "сори у мя пока нет мп3 формата🤥")
    elif message.text == "чоми сайт":
        a = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, str("https://tanki.su/"), reply_markup=a)
    elif message.text == "чоми анекдот":
        a = telebot.types.ReplyKeyboardRemove()
        j1 = 'сидел чомик на лавочке...\nи вдруг он замечает башенки похожие друг на друга\nне задумываясь кричит\n-алахакбар'
        j2 = 'бобик сдох'
        j3 = 'колобок повесился'
        j = [j1, j2, j3]
        bot.send_message(message.chat.id, random.choice(j), reply_markup=a)
    elif message.text == "чоми дата":
        a = telebot.types.ReplyKeyboardRemove()
        current_date = date.today()
        bot.send_message(message.chat.id, f"{message.from_user.first_name}, дата: ", reply_markup=a)
        bot.send_message(message.chat.id, current_date, reply_markup=a) 
        
    elif message.text == "чоми время":
        a = telebot.types.ReplyKeyboardRemove()
        tz1 = pytz.timezone("Europe/Vienna")
        tz2 = pytz.timezone("Europe/Kishinev") 
        germ_current_time = datetime.now(tz1).time()
        ua_current_time = datetime.now(tz2).time()
        if message.from_user.id == 1177268972:
            bot.send_message(message.chat.id, f"{message.from_user.first_name}, время: ", reply_markup=a)
            bot.send_message(message.chat.id, germ_current_time ,reply_markup=a)
        elif not message.from_user.id == 1177268972:
            bot.send_message(message.chat.id, f"{message.from_user.first_name}, время: ", reply_markup=a)
            bot.send_message(message.chat.id, ua_current_time ,reply_markup=a)
            
    elif message.text == "back":
        telebot.types.ReplyKeyboardRemove()


    
        
bot.polling(none_stop = True)
