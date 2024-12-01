''' Файл главный'''
import random
import telebot
import time
from yandexgpt import ask_yandex_gpt

from token_tg import TOKEN_TG

bot = telebot.TeleBot(TOKEN_TG)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    ''' hghghg'''
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_info_bot = telebot.types.KeyboardButton('Информация о боте')
    button_info_creator = telebot.types.KeyboardButton(
        'Информация о создателе')
    button_quastin = telebot.types.KeyboardButton('Задать вопрос')

    markup.add(button_info_bot, button_info_creator, button_quastin)
    bot.send_message(message.chat.id, 'Приветик, бро', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Информация о боте')
def send_info_bot(message):
    ''' jhjgh'''
    bot.send_message(message.chat.id,
                     'Это бот, который поможет тебе с любым вопросом.')


@bot.message_handler(
    func=lambda message: message.text == 'Информация о создателе')
def send_info_creator(message):
    ''' hghghh'''
    bot.send_message(message.chat.id, 'Создатель этого бота - @Leka_sv')


@bot.message_handler(content_types=['text'])
def message_text(message):
    ''' jhjjh'''
    user_message = message.text

    # Отправляем сообщение о том, что бот ищет ответ
    searching_message = bot.send_message(message.chat.id, "Ищу ответ... Это займет немного времени.")

    # Здесь вызываем функцию, которая будет обрабатывать ответ (например, ask_yandex_gpt)
    jpt_response = ask_yandex_gpt(user_message)
    # Удаляем сообщение о поиске
    bot.delete_message(message.chat.id, searching_message.message_id)
    # Отправляем ответ пользователю
    bot.send_message(message.chat.id, jpt_response)


stickers = [
    'CAACAgIAAxkBAANBZ0wubB4exvlZVThP6bFsBoDUHsMAAigsAAKVfMhL7sDoos2Pvdo2BA',
    'CAACAgIAAxkBAANDZ0wurxWyU3iBMBWb1kaEHI8aWPQAAikvAAKFTYFIy33uo4Dh75Q2BA',
    'CAACAgIAAxkBAANFZ0wu5FPox2hRnwnf7HXPw9U3V3EAAvYzAAK-H3lIivYnYH-w9qU2BA',
    'CAACAgIAAxkBAANHZ0wvAAFYTVDeWvYu4WpwCM5KEfAoAAK4NgACI5ZxSf4DVp_KfNNuNgQ'
]

photo_use = 'https://cs14.pikabu.ru/post_img/2023/01/30/8/og_og_1675083542232994806.jpg'


@bot.message_handler(content_types=['photo'])
def message_photo(message):
    ''' hg'''
    photo = message.photo[-1].file_id
    print(f'Полученно фото с id: {photo}')
    bot.send_photo(message.chat.id, photo_use)


@bot.message_handler(content_types=['audio'])
def message_audio(message):
    ''' jghj'''
    audio = message.audio.file_id
    print(f'Получено аудио с id: {audio}')
    bot.reply_to(message, 'Неплохая!')


sticker = 'CAACAgIAAxkBAANFZ0wu5FPox2hRnwnf7HXPw9U3V3EAAvYzAAK-H3lIivYnYH-w9qU2BA'


@bot.message_handler(content_types=['document'])
def message_document(message):
    ''' jhjhjhj'''
    document = message.document.file_id
    print(f'Получен документ с id: {document}')
    bot.reply_to(message, 'Докумееентик!')
    bot.send_sticker(message.chat.id, sticker)


@bot.message_handler(content_types=['sticker'])
def message_sticker(message):
    ''' jhjjh'''
    sticker_id = message.sticker.file_id
    print(f"Получен стикер: {sticker_id}")
    stickers.append(sticker_id)

    # Отправляем случайный стикер из списка
    random_sticker = random.choice(stickers)
    bot.send_sticker(message.chat.id, random_sticker)
    # print(stickers)


vivi = 'BAACAgIAAxkBAAPHZ0w2ytdN-EGwYr-dvzyv8jC-TrMAAl9gAAL_uWBK5wt2dONoHpU2BA'


@bot.message_handler(content_types=['video'])
def message_video(message):
    ''' hjghjj'''
    video = message.video.file_id
    print(f'Получено видео с id: {video}')
    bot.send_video(message.chat.id, vivi)
    # bot.send_message(message.chat.id, 'Я не умею обрабатывать видео')


# my = [
#   'AwACAgIAAxkBAAPNZ0w3z18vunnzp7Rub084rN0a0vEAAntgAAL_uWBKZdwlWaJmrC02BA',
#  'AwACAgIAAxkBAAPUZ0w4Qi0HpQiaP9r-TqMD5RJi2QEAApBgAAL_uWBK2WWZVX6013s2BA',
# 'AwACAgIAAxkBAAPWZ0w4Wnqkb61l4bkrUsGuTIL_eRoAApNgAAL_uWBKVKxKEeKddlc2BA',
# 'AwACAgIAAxkBAAPYZ0w4bKPIZuDpl3nvNrA95QxkEIQAApVgAAL_uWBKDpEqDTX7J-82BA'
# ]


@bot.message_handler(content_types=['voice'])
def message_voice(message):
    ''' jhjjhjh'''
    voise = message.voice.file_id
    print(f'Получено голосовое сообщение с id: {voise}')
    bot.send_message(message.chat.id, 'Я пока не умею читать гс')
    # bot.send_voice(message.chat.id, random.choice(my))


hoho = 'https://cs10.pikabu.ru/post_img/2018/10/24/8/og_og_15403858292647152.jpg'


@bot.message_handler(content_types=['video_note'])
def handle_video_note(message):
    ''' jhhfggs'''
    video_note = message.video_note.file_id
    print(f'Получен кружочек с видео: {video_note}')
    bot.send_photo(message.chat.id, hoho)
    bot.reply_to(message, 'Кружочек бомба!')


@bot.message_handler(content_types=['location'])
def message_location(message):
    '''gjhjhjhjh'''
    location = message.location
    loc1 = message.location.longitude
    loc2 = message.location.latitude
    print(f'Получена локация с широтой: {location}')
    bot.send_message(message.chat.id, 'А не далековато?')
    bot.send_location(message.chat.id, loc2, loc1)


@bot.message_handler(content_types=['contact'])
def message_contact(message):
    ''' hggdfd'''
    bot.reply_to(message, 'Записал')


@bot.message_handler(content_types=['venue'])
def message_venue(message):
    ''' bjhjhjhjh'''
    bot.send_message(message.chat.id, 'Советуете посетить? хорошо')


@bot.message_handler(content_types=['poll'])
def message_poll(message):
    ''' jghjk'''
    bot.send_message(message.chat.id,
                     'Я не могу поучаствовать в вашем опросе(')


@bot.message_handler(content_types=['game'])
def message_game(message):
    ''' hgggfff'''
    bot.send_message(message.chat.id, 'Я не умею обрабатывать игры')


bot.polling(none_stop=True)
