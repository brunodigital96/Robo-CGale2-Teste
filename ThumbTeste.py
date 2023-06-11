import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Criação do bot
updater = Updater(token='seu_token_do_bot', use_context=True)
dispatcher = updater.dispatcher

# Função para remover a thumb
def remove_thumb(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='COMPRE A SALA VIP AQUI', disable_web_page_preview=True)

# Handler para a mensagem
handler = MessageHandler(Filters.text & (~Filters.command), remove_thumb)
dispatcher.add_handler(handler)

# Iniciar o bot
updater.start_polling()