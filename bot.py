import telebot 
import keyboards
import fsm
BOT_TOKEN = '7607530682:AAEweD-DkwE2QQ0wpjGbRa1931R8sbo31rg'
stater = fsm.FSM()
bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(func = lambda message: True)
# def echo_all(message):
    # button1 = telebot.types.KeyboardButton(text = "Меню")
    # button2 = telebot.types.KeyboardButton(text = "Текст")
    # button3 = telebot.types.KeyboardButton(text = "Картинки")
    # keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) 
    # keyboard.add(button1)
    # keyboard.add(button2, button3)
    # bot.send_message(message.chat.id, 'Вот ваша клавиатура', reply_markup= keyboard, )   
def on_message(message):
    msg_text = message.text
    state = stater.set_state(message.chat.id)
    if state == fsm.DEFAULT_STATE:
        if msg_text == "Фото📸":
            stater.set_state(message.chat.id, fsm.IMAGE_STATE)
            bot.send_message(message.chat.id, text = "Напиши описание фото", reply_markup=keyboards.back)
        elif msg_text == "Текст✏️":
            stater.set_state(message.chat.id, fsm.TEXT_STATE)
            bot.send_message(message.chat.id, text = "Напиши о чем хочешь узнать", reply_markup=keyboards.back)
        else:
            bot.send_message(message.chat.id, text = "Не понимаю о чем ты...", reply_markup=keyboards.start)
    elif state == fsm.IMAGE_STATE:
        if msg_text == "В меню📌":
            stater.set_state(message.chat.id, fsm.DEFAULT_STATE)
            bot.send_message(message.chat.id, text = "Главное меню", reply_markup=keyboards.start)
        else:
            bot.send_message(message.chat.id, text = "Скоро буду генерировать")
    elif state == fsm.TEXT_STATE:
        if msg_text == "В меню📌":
            stater.set_state(message.chat.id, fsm.DEFAULT_STATE)
            bot.send_message(message.chat.id, text = "Главное меню", reply_markup=keyboards.start)
        else:
            bot.send_message(message.chat.id, text = "Скоро буду генерировать")
    else:
        stater.set_state(message.chat.id, fsm.DEFAULT_STATE)
        bot.send_message(message.chat.id, text = "Не понимаю о чем ты...")
bot.polling()

