import telebot

# substitua 'BOT_TOKEN' pelo token do seu bot, obtido na plataforma do BotFather
bot = telebot.TeleBot('6230037536:AAFzbNZVV_zo0ILKfiok07Q87NlQUjRTnaA')

# substitua 'ID_DO_CHAT' pelo ID do chat ou canal que receberá a mensagem
chat_id = '-1001839680825'

# substitua 'ID_DO_STICKER' pelo ID do sticker que deseja enviar
sticker_id_atentos = 'CAACAgEAAxkBAAG9UCBkT9RtQLBMrha0d8MZZt2TxsM0xgACVgMAAsoSgUaRc5TpJfH7pC8E'
sticker_id_branco = 'CAACAgEAAxkBAAG9UDZkT9SABPRpWD7vvd7I8hb7EY_RxgACogMAAhrPgUaWDjzAIGIa4C8E'
sticker_id_encerrado = 'CAACAgEAAxkBAAG9UHBkT9SPBQABFz0SAucIMohWEVxOxx0AAocCAAKnFYFG0TGo8k7mUe0vBA'
sticker_id_grenn = 'CAACAgEAAxkBAAG9ULdkT9Sfbbko8LQBsOw7UmKGs7A0BQACQQIAAiC7gEZszH68SfuvXi8E'
sticker_id_loss = 'CAACAgEAAxkBAAG9ULdkT9Sfbbko8LQBsOw7UmKGs7A0BQACQQIAAiC7gEZszH68SfuvXi8E'

# envia o sticker para o chat ou canal especificado
bot.send_sticker(chat_id, sticker_id_atentos)
bot.send_sticker(chat_id, sticker_id_branco)
bot.send_sticker(chat_id, sticker_id_encerrado)
bot.send_sticker(chat_id, sticker_id_grenn)
bot.send_sticker(sticker_id_loss)

