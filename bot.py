from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    print(update)
    update.message.reply_text("Hello, User!")

def talk_to_me(update, context):
    update.message.reply_text(update.message.text)


def main():
    mybot=Updater(settings.API_KEY, use_context=True) #создание переменной
    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start",greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Bot has started")
    mybot.start_polling() #обращения за обновлениями
    mybot.idle() #работает постоянно

if __name__=="__main__":    
    main()