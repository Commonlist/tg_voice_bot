from pyrogram import Client, filters
import asyncio
import requests

# Замените на ваш API ID
api_id = "api_id"
# Замените на ваш API Hash
api_hash = "api_hash"
# ID группового чата
group_chat_id = -100group_chat_id
# Ваш username в Telegram
your_username = "your_username"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

voice_message_ids = {}

# Обработчик голосовых сообщений в приватных чатах
@app.on_message(filters.private & filters.voice)
async def forward_voice_to_bot(client, message):
    sent_message = await message.forward(group_chat_id)
    # Используем forward_from.username если доступно, иначе from_user.username
    username = message.forward_from.username if message.forward_from else message.from_user.username
    voice_message_ids[sent_message.id] = (message.chat.id, username)

# Обработчик ответов от бота в групповом чате
@app.on_edited_message(filters.chat(group_chat_id) & filters.text & filters.user('username_of_bot_who_recognize_voice'))
async def handle_bot_response_edited(client, message):
    if message.reply_to_message_id and message.reply_to_message_id in voice_message_ids:
        original_chat_id, username = voice_message_ids[message.reply_to_message_id]
        original_message = await app.get_messages(group_chat_id, message.reply_to_message_id)

        # Определяем префикс на основе имени пользователя
        prefix = "Ваш Голос: " if username == your_username else f"Собеседник: "

        transcription = message.text
        await client.send_message(original_chat_id, f"{prefix}{transcription}")
        del voice_message_ids[message.reply_to_message_id]

# Запуск клиента
app.run()