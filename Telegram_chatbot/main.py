#pip install pyTelegramBotAPI


import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from BotFather on Telegram
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

# Handle the /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    user = message.from_user
    bot.send_message(message.chat.id, f"Hi {user.first_name}! I am your echo bot. Send me a message, and I'll echo it back to you.")

# Echo all text messages
@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    print(message.text)
    bot.send_message(message.chat.id, message.text)

# Start the bot
bot.polling()
