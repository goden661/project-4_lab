import telebot
import json

def parse_shedule(spisok):
    result = ""
    i = 1
    for subject in spisok:
        result += "{n} - {name}\r\n".format(n=i, name=str(subject))
        i += 1
    return result
token = "5864188381:AAEO_QPsiC33SLo22sFOx-jeoIf6GBO8PZ8"

with open("shedule.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

print(data)
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "понедельник":
        bot.send_message(message.chat.id, parse_shedule(data["расписание"]["понедельник"]))
    if message.text.lower() == "вторник":
        bot.send_message(message.chat.id, parse_shedule(data["расписание"]["вторник"]))
    if message.text.lower() == "среда":
        bot.send_message(message.chat.id, parse_shedule(data["расписание"]["среда"]))
    if message.text.lower() == "четверг":
        bot.send_message(message.chat.id, parse_shedule(data["расписание"]["четверг"]))
    if message.text.lower() == "пятница":
        bot.send_message(message.chat.id, parse_shedule(data["расписание"]["пятница"]))

    if message.text.lower() == "все расписание":
        bot.send_message(message.chat.id, parse_shedule(data["расписание"]["понедельник"]) +
            parse_shedule(data["расписание"]["вторник"]) +
            parse_shedule(data["расписание"]["среда"]) +
            parse_shedule(data["расписание"]["четверг"]) +
            parse_shedule(data["расписание"]["пятница"]))

    if message.text.lower() == "расписание":
        keyboard = telebot.types.ReplyKeyboardMarkup()
        keyboard.row("понедельник","вторник","среда")
        keyboard.row("четверг","пятница","все расписание")

        bot.send_message(message.chat.id, "выберите день", reply_markup=keyboard)

print("start")
bot.infinity_polling()