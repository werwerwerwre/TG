import telebot

# Токен вашого бота
API_TOKEN = '8197638246:AAHRc3q3WlYAQKKEvZDqC60zuSmJ6YWvnjE'

# Ініціалізація бота
bot = telebot.TeleBot(API_TOKEN)

# Функція для обробки текстових повідомлень
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Отримуємо текст повідомлення
    received_text = message.text

    # Записуємо отриманий текст у файл
    with open("Text.txt", "a", encoding="utf-8") as file:
        file.write(received_text + "\n")
    
    # Відповідаємо користувачу
    bot.reply_to(message, "Ваше повідомлення було записано!")

# Запуск бота
if __name__ == '__main__':
    bot.polling(none_stop=True)
