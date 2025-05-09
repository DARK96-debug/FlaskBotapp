from flask import Flask, request
import telegram

TOKEN = '7938346036:AAHtkDx0mZQz3uRrjGKZ1f07Dy_gTRRTims'
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot ishga tushdi!'

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text

    if text == "/start":
        bot.send_message(chat_id=chat_id, text="Assalomu alaykum! UC botga xush kelibsiz.")
    elif text == "UC chiqarish":
        bot.send_message(chat_id=chat_id, text="UC miqdorini va PUBG ID'ingizni yuboring.")
    elif text == "Missiya qo‘shish":
        bot.send_message(chat_id=chat_id, text="Missiya qo‘shish uchun admin bilan bog‘laning.")
    elif text == "Referal":
        bot.send_message(chat_id=chat_id, text="Sizning referal linkingiz: https://t.me/yourbot?start=12345")
    else:
        bot.send_message(chat_id=chat_id, text="Xabar qabul qilindi.")

    return 'ok'

if __name__ == '__main__':
    app.run()
