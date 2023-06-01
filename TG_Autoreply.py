from telethon import TelegramClient, events, types, sync

# Авторизация (переменные)
api_id = 27396949
api_hash = '75beb73ea56149860a6205de1f2664e0'
phone_number = '79101500436'
client = TelegramClient('session_name', api_id, api_hash)
client.start(phone_number)
client.send_message('me', 'Автоответчик включен') #Статус работы
print('Автоответчик включен')

exceptions = [1412257310] #Переменная для исключений по user_id
@client.on(events.NewMessage(incoming=True)) #Ответ будет идти на любое личное сообщение
async def handle_message(event):
    if isinstance(event.chat, types.User) and event.chat_id not in exceptions:
        await event.reply('Привет!\nЯ сейчас нахожусь в отпуске и не могу тебе сейчас ответить.\nПожалуйста, сделай заявку на support@ekf.su и мои коллеги обязательно тебе помогут!')


client.run_until_disconnected()

