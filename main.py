import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI
from notifiers import get_notifier
import time
from help import help_str
cg = CoinGeckoAPI()
token = 'сюда Ваш токен'
bot = telebot.TeleBot(token)

name = ''
surname = ''
age = ''
valute_from_konv = ''
valute_to_konv = ''
count_of_convert = 0
valute_of_uved =''
valute_of_uved_counter =''
count_time_uved = 0
count_value_bound = 0
close_uved_flag = True
close_uved_flag_usual = True
time_notes = 0
notes_str = ''
notes_flag = True
usual_notice = ''
time_usual_notice = 0
list_konvert = [0]*18

list_tokens = ['bitcoin', 'ethereum', 'dogecoin']
list_valute = ['usd', 'rub', 'eur']

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btnBit = types.KeyboardButton("bitcoin")
btnEth = types.KeyboardButton("ethereum")
btnDoge = types.KeyboardButton("dogecoin")
markup1.add(btnBit, btnEth, btnDoge)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btnUsd = types.KeyboardButton("usd")
btnEur = types.KeyboardButton("rub")
btnRub = types.KeyboardButton("eur")
markup2.add(btnUsd, btnEur, btnRub)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn = types.KeyboardButton("help")
btn1 = types.KeyboardButton("konverter")
btn2 = types.KeyboardButton("start")
btn3 = types.KeyboardButton("nCripto")
btn0 = types.KeyboardButton("notice")
btn4 = types.KeyboardButton("notes")
btnBit = types.KeyboardButton("bitcoin")
btnEth = types.KeyboardButton("ethereum")
btnDoge = types.KeyboardButton("dogecoin")
markup.add(btn2, btn, btn1, btn3, btn0, btn4, btnBit, btnEth, btnDoge)

markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn5 = types.KeyboardButton("stop noticeCripto")
markup3.add(btn5)

markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn6 = types.KeyboardButton("0.1")
btn7 = types.KeyboardButton("1")
btn8 = types.KeyboardButton("5")
markup4.add(btn6, btn7, btn8)

@bot.message_handler(content_types=['text'])
def give_price(message):
    global list_konvert, close_uved_flag, close_uved_flag_usual, notes_flag, notes_str
    print('jjj')
    mes_true = False
    for j in list_tokens:
        if message.text == j:
            mes_true = True
            st = str(cg.get_price(ids=j, vs_currencies='usd'))
            st_ch = ''
            for i in st:
                if i.isdigit() or i == '.':
                    st_ch += i
            opop = 'сегодня ' + j + ' стоит всего-то: ' + st_ch
            bot.send_message(message.from_user.id, opop)

    if message.text == 'start':
        mes_true = True
        bot.send_message(message.from_user.id, "Как тебя зовут?", reply_markup=markup)
        bot.register_next_step_handler(message, get_name)

    if message.text == 'konverter':
        mes_true = True
        bot.send_message(message.from_user.id, "Откуда конвертируем?", reply_markup=markup1)
        bot.register_next_step_handler(message, get_name_from_valute_konvert)

    if message.text == 'nCripto':
        mes_true = True
        if not(close_uved_flag):
            bot.send_message(message.from_user.id, "Сначала выключите предыдущие уведомления, для этого напишите ``stop noticeCripto``", reply_markup=markup3)
        else:
            close_uved_flag = False
            bot.send_message(message.from_user.id, "На какую криптовалюту хотите настроить уведомления?", reply_markup=markup1)
            bot.register_next_step_handler(message, get_valute_of_uved_counter)

    if message.text == 'stop nCripto':
        mes_true = True
        close_uved_flag = True

    if message.text == 'notice':
        mes_true = True
        if not(close_uved_flag_usual):
            bot.send_message(message.from_user.id, "Дождитесь отправки предыдущего уведомления!")
        else:
            close_uved_flag_usual = False
            bot.send_message(message.from_user.id, "Напишите текст уведомления", reply_markup=markup1)
            bot.register_next_step_handler(message, get_usual_notice)

    if message.text == 'help':
        mes_true = True
        bot.send_message(message.from_user.id, help_str)

    if message.text == 'notes':
        mes_true = True
        if not(notes_flag):
            notes_str = ''
            notes_flag = True
        bot.send_message(message.from_user.id, "Напишите текст своего уведомления!")
        bot.register_next_step_handler(message, get_notes)

    if message.text == 'stop notes':
        notes_flag = False

    if message.text == 'get notes':
        bot.send_message(message.from_user.id, notes_str)

    if not(mes_true):
        bot.send_message(message.from_user.id, "Ваше сообщение не распознано. Пожалуйста, ознакомьтесь со списком команд.")

def get_notes(message):
    global notes_str
    notes_str += message.text
    notes_str += '\n'
    bot.send_message(message.from_user.id, "Через сколько прислать?", reply_markup=markup4)
    bot.register_next_step_handler(message, get_times_notes)

def get_times_notes(message):
    global time_notes, notes_str
    time_notes = message.text
    if time_notes.isdigit() or time_notes == '0.1':
        t = float(time_notes) * 60
        time.sleep(t)
        mes1 = 'ого-го, вам уведомление!\n'
        mes2 = notes_str
        mes3 = mes1 + mes2
        notes_str = ''
        bot.send_message(message.from_user.id, mes3, reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, "Вы неправильно ввели значение! Неуд1")
        bot.send_message(message.from_user.id, "Через сколько прислать?", reply_markup=markup4)
        bot.register_next_step_handler(message, get_times_notes)

def get_valute_of_uved_counter(message):
    global valute_of_uved, list_tokens
    valute_of_uved = message.text
    if not(valute_of_uved in list_tokens):
        bot.send_message(message.from_user.id, "Вы неправильно ввели название крипты! Вам неуд2")
        bot.send_message(message.from_user.id, "На какую криптовалюту хотите настроить уведомления?", reply_markup=markup1)
        bot.register_next_step_handler(message, get_valute_of_uved_counter)
    else:
        bot.send_message(message.from_user.id, 'В какой валюте установите границу для уведомлений?', reply_markup=markup2)
        bot.register_next_step_handler(message, get_valute_of_uved)

def get_valute_of_uved(message):
    global valute_of_uved_counter, list_valute
    valute_of_uved_counter = message.text
    if not (valute_of_uved_counter in list_valute):
        bot.send_message(message.from_user.id, "Вы неправильно ввели валюту! Такое не достойно уважения")
        bot.send_message(message.from_user.id, 'В какой валюте установите границу для уведомлений?', reply_markup=markup2)
        bot.register_next_step_handler(message, get_valute_of_uved)
    else:
        bot.send_message(message.from_user.id, 'После превышения какого значения присылать уведомления?')
        bot.register_next_step_handler(message, get_count_time_uved)

def get_count_time_uved(message):
    global count_value_bound
    count_value_bound = message.text
    chek_true_of_count = ''
    for i in count_value_bound:
        if i != '.':
            chek_true_of_count += i
    if chek_true_of_count.isdigit() and count_value_bound.count('.') < 2 and len(chek_true_of_count) > 0:
        bot.send_message(message.from_user.id, 'Через какие промежутки времени присылать уведомления?', reply_markup=markup4)
        bot.register_next_step_handler(message, get_uved)
    else:
        bot.send_message(message.from_user.id, "Вы неправильно ввели значение! Неуд1")
        bot.send_message(message.from_user.id, 'После превышения какого значения присылать уведомления?')
        bot.register_next_step_handler(message, get_count_time_uved)

def get_uved(message):
    global valute_of_uved, count_value_bound, count_time_uved, valute_of_uved_counter, close_uved_flag
    count_time_uved = message.text
    if (count_time_uved.isdigit() or count_time_uved == '0.1'):
        print('uvediki')
        while True:
            if close_uved_flag:
                print('close')
                break
            st_bit_res = ''
            st_bit = str(cg.get_price(ids=valute_of_uved, vs_currencies=valute_of_uved_counter))
            for i in st_bit:
                if i.isdigit() or i == '.':
                    st_bit_res += i
            if float(st_bit_res) > float(count_value_bound) and not(close_uved_flag):
                #t = 1
                t = float(count_time_uved) * 60
                time.sleep(t)
                telegram = get_notifier('telegram')
                mes1 = 'ого-го, значение '
                mes2 = 'превысило '
                mes3 = mes1 + valute_of_uved + ' ' + mes2 + count_value_bound + valute_of_uved_counter
                bot.send_message(message.from_user.id, mes3)
                #telegram.notify(token=token, chat_id=chatId, message=mes3)
    else:
        bot.send_message(message.from_user.id, "Вы неправильно ввели значение! Неуд1")
        bot.send_message(message.from_user.id, 'Через какие промежутки времени присылать уведомления?', reply_markup=markup4)
        bot.register_next_step_handler(message, get_uved)

def get_name_from_valute_konvert(message):
    global valute_from_konv, list_tokens
    valute_from_konv = message.text
    if not(valute_from_konv in list_tokens):
        bot.send_message(message.from_user.id, "Вы неправильно ввели название крипты! Вам неуд2")
        bot.send_message(message.from_user.id, "Откуда конвертируем?", reply_markup=markup1)
        bot.register_next_step_handler(message, get_name_from_valute_konvert)
    else:
        bot.send_message(message.from_user.id, 'Куда конвертируем?', reply_markup=markup2)
        bot.register_next_step_handler(message, get_name_to_valute_konvert)

def get_name_to_valute_konvert(message):
    global valute_to_konv, list_valute
    valute_to_konv = message.text
    if not (valute_to_konv in list_valute):
        bot.send_message(message.from_user.id, "Вы неправильно ввели валюту! Такое не достойно уважения")
        bot.send_message(message.from_user.id, 'Куда конвертируем?', reply_markup=markup2)
        bot.register_next_step_handler(message, get_name_to_valute_konvert)
    else:
        bot.send_message(message.from_user.id, 'Сколько конвертируем?')
        bot.register_next_step_handler(message, get_count_of_convert)

def get_count_of_convert(message):
    global count_of_convert, valute_from_konv, valute_to_konv, list_konvert
    count_of_convert = message.text
    chek_true_of_count = ''
    for i in count_of_convert:
        if i != '.':
            chek_true_of_count += i
    if chek_true_of_count.isdigit() and count_of_convert.count('.') < 2 and len(chek_true_of_count) > 0:
        st_konv = str(cg.get_price(ids=valute_from_konv, vs_currencies=valute_to_konv))

        st_ch_konv = ''
        for i in st_konv:
            if i.isdigit() or i == '.':
                st_ch_konv += i
        if st_ch_konv == '':
            st_ch_konv = '0'
        p = valute_to_konv + ' in ' + str(count_of_convert) + ' ' + valute_from_konv + ': ' + str(
            round(float(st_ch_konv) * float(count_of_convert), 3))
        bot.send_message(message.from_user.id, p, reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, "Вы неправильно ввели значение! Неуд1")
        bot.send_message(message.from_user.id, 'Сколько конвертируем?')
        bot.register_next_step_handler(message, get_count_of_convert)

def get_usual_notice(message):
    global usual_notice
    usual_notice = message.text
    bot.send_message(message.from_user.id, 'Через сколько прислать уведомление?', reply_markup=markup4)
    bot.register_next_step_handler(message, get_time_usual_notice)

def get_time_usual_notice(message):
    global time_usual_notice, close_uved_flag_usual
    time_usual_notice = message.text
    if time_usual_notice.isdigit() or time_usual_notice == '0.1':
        t = float(time_usual_notice) * 60
        time.sleep(t)
        telegram = get_notifier('telegram')
        mes1 = 'Вам посылка:\n'
        mes2 = mes1 + usual_notice
        bot.send_message(message.from_user.id, mes2)
        #telegram.notify(token=token, chat_id=chatId, message=mes2)
        close_uved_flag_usual = True
    else:
        bot.send_message(message.from_user.id, 'Введите целое число минут или 0.1')
        bot.send_message(message.from_user.id, 'Через сколько прислать уведомление?')
        bot.register_next_step_handler(message, get_time_usual_notice)

def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id,'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    age = message.text
    if age.isdigit() and int(age) > 0:
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key_yes) #добавляем кнопку в клавиатуру
        key_no= types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, 'Возраст не нормик')
        bot.send_message(message.from_user.id, 'Сколько тебе лет?')
        bot.register_next_step_handler(message, get_age)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global age
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню : )')
        if int(age) < 18:
            bot.send_message(call.message.chat.id, 'А не маленький для больших бабок?')
        else:
            if int(age) > 33:
                bot.send_message(call.message.chat.id, 'А не староват для телеграмма?')
            else:
                bot.send_message(call.message.chat.id, 'Отличный возраст, чтобы начать делать деньги')
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Очень жаль, что ошиблись, снова напишите старт, больше не ошибайтесь!", reply_markup=markup)
bot.polling(none_stop=True, interval=0)
