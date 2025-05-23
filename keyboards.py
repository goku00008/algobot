import telebot 
start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) 
button4 = telebot.types.KeyboardButton(text = "Текст")
button5 = telebot.types.KeyboardButton(text = "Фото")
start.add(button4, button5)

back = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True) 
button6 = telebot.types.KeyboardButton(text = "В меню")
back.add(button6)
    
