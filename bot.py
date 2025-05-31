import telebot 

bot = telebot.TeleBot('7607530682:AAEweD-DkwE2QQ0wpjGbRa1931R8sbo31rg')
@bot.message_handler(commands= ['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!!!!')
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'привет,{message.from_user.first_name}')
    elif message.text.lower() == 'как дела':
        bot.send_message(message.chat.id, f'все хорошо,как твои дела?{message.from_user.first_name}')    
    elif message.text.lower() == 'что ты умеешь':
        bot.send_message(message.chat.id, f'все.а как твои дела?')    
    elif message.text.lower() == 'все нормально' or 'все хорошо':
        

bot.polling(none_stop = True)   