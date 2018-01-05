#In the name of ALLAH
#-*- coding: utf-8 -*-
import sys
import urllib
import telebot
from telebot import types
import urllib2
import requests as req
import json

reload(sys)
sys.setdefaultencoding('utf-8')

api_token = "380896813:AAHZJ8BpF_WM0ZpVncjHvKow0GLcChSj4bM"

sudo = ""

bot = telebot.TeleBot(api_token)

a = '\n---Bot name : '+str(bot.get_me().first_name)
b = '\n---Bot User : @'+str(bot.get_me().username)
c = '\n---Bot GLID : '+str(bot.get_me().id)
print a+b+c
############################################################################################################################################################

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
     cid = call.message.chat.id
     mes = call.message.message_id
###########################
     if call.message:
        if call.data == "abo":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="""⭐️بسم الله الرحمن الرحیم⭐️

🌹دوستان این ربات برای من خیلی هزینه داره ، بیایین با هم این ربات رو انلاین نگه داریم!
🌐از دکمه "حمایت کنید" استفاده کنید!""")
###########################
     if call.message:
        if call.data == "creator":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="""
⚜️ارتباط با برنامه نویس :

📌آیدی : @Fedora_PD
📌تلفن همراه : +989196515740
📌ایمیل : DayanWorks@hotmail.com""")
###########################منوی اصلی (بازگشت)
     if call.message:
        if call.data == "back":
            i = types.InlineKeyboardMarkup()
            a = types.InlineKeyboardButton("🔺ورود به منو🔺" , callback_data='menu')
            i.add(a)
            bot.edit_message_text('✔️به منوی اصلی بازگشتید!' , cid , mes)
            bot.edit_message_reply_markup(cid , mes , reply_markup=i)
###########################
     if call.message:
        if call.data == "helps":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="""
به زودی . . .""")
###########################منو اصلی
     if call.message:
        if call.data=='menu':
            i = types.InlineKeyboardMarkup()
            a = types.InlineKeyboardButton("📜منوی ترجمه📜" , callback_data='menutrans')
            b = types.InlineKeyboardButton("⚜️سازنده⚜️" , callback_data='creator')
            c = types.InlineKeyboardButton("💻کانال💻" , url='https://t.me/fedorasec')
            e = types.InlineKeyboardButton("📌راهنما📌" , callback_data='helps')
            f = types.InlineKeyboardButton("⭐️حمایت کنید⭐️" , url='https://idpay.ir/enfatranslate')
            d = types.InlineKeyboardButton("🔙بازگشت به منوی اصلی🔙" , callback_data='back')
            h = types.InlineKeyboardButton("💻بخوانید💻" , callback_data='abo')
            i.add(a)
            i.add(e)
            i.add(h)
            i.add(f)
            i.add(b , c)
            i.add(d)
            bot.edit_message_text('⚜️به منوی ربات خوش آمدید!' , cid , mes)
            bot.edit_message_reply_markup(cid , mes , reply_markup=i)

     if call.message:
        if call.data=='menutrans':
            i = types.InlineKeyboardMarkup()
            a = types.InlineKeyboardButton("🇮🇷ترجمه از انگلیسی به فارسی🇮🇷" , switch_inline_query_current_chat='fa ')
            b = types.InlineKeyboardButton("🇬🇧ترجمه از فارسی به انگلیسی🇬🇧" , switch_inline_query_current_chat='en ')
            i.add(a)
            i.add(b)
            d = types.InlineKeyboardButton("🔙بازگشت به منوی اصلی🔙" , callback_data='back')
            i.add(d)
            bot.edit_message_text('🔰به منوی ترجمه خوش آمدید!' , cid , mes)
            bot.edit_message_reply_markup(cid , mes , reply_markup=i)
############################################################################################################################################################

@bot.message_handler(commands = ['start'])
def start(m):
    id = m.chat.id
    i = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton("🔺ورود به منو🔺" , callback_data='menu')
    i.add(a)
    bot.send_message(id , "⚜️سلام به ربات مترجم *EnFa* خوش آمدید!" , reply_markup=i , parse_mode="Markdown")

############################################################################################################################################################

@bot.inline_handler(lambda q: q.query)
def inline(query):
    try:
        i = types.InlineKeyboardMarkup()
        a = types.InlineKeyboardButton("⚙️برنامه نویس⚙️" , "https://t.me/fedora_pd")
        i.add(a)

        if query.query.split()[0]=='en' :
            en = query.query.split()[0]
            text = query.query.replace(en ,"%20")
            r = req.get("https://api.beyond-dev.ir/translate/?from=fa&to=en&text={}".format(text) + "&simple=json")
            json_data = r.json()
            t2 = json_data['translate']
            markdown2 = types.InlineQueryResultArticle('1','🇬🇧English | انگلیسی🇬🇧', types.InputTextMessageContent(t2), reply_markup=i , description="🇬🇧Translate from Persian to English\n🇬🇧ترجمه از فارسی به انگلیسی", thumb_url="http://nordgain.com/wp-content/uploads/2015/08/union-jack-1027898_1280.jpg")
            bot.answer_inline_query(query.id, [markdown2], cache_time="1")

        if query.query.split()[0]=='fa':
            fa = query.query.split()[0]
            text = query.query.replace(fa ,"%20")
            r = req.get("https://api.beyond-dev.ir/translate/?from=en&to=fa&text={}".format(text) + "&simple=json")
            json_data = r.json()
            t = json_data['translate']
            markdown1 = types.InlineQueryResultArticle('1','🇮🇷Persian | پارسی🇮🇷', types.InputTextMessageContent(t ), reply_markup=i , description="🇮🇷Translate from English to Persian\n🇮🇷ترجمه از انگلیسی به فارسی", thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Flag_of_Iran.svg/255px-Flag_of_Iran.svg.png")
            bot.answer_inline_query(query.id, [markdown1], cache_time="1")

    except:
        print "Error"
############################################################################################################################################################
while True:
    try:
        bot.polling(True)
    except:
        print""
