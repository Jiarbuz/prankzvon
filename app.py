from flask import Flask, render_template, request, session
from flask_babel import Babel
from dotenv import load_dotenv
import os

# Загрузка переменных окружения
load_dotenv()

# Инициализация Flask приложения
app = Flask(__name__)
app.secret_key = os.getenv('1bcb3078b20ca1ad5f223f4fb9a2ca34a2aaeec55971bd69f8d539dc1c6a99e3', 'default-secret-key')

# Настройка Babel для интернационализации
app.config['BABEL_DEFAULT_LOCALE'] = 'ru'
babel = Babel(app)

def get_locale():
    """Определение языка из сессии или использование языка по умолчанию"""
    return session.get('lang', 'ru')

babel.locale_selector_func = get_locale

# Полные переводы для приложения
translations = {
    'ru': {
        'info_title': "PrankVzlom 📹📔",
        'disclaimer': "САЙТ СДЕЛАН ДЛЯ РАЗВЛЕКАТЕЛЬНЫХ ЦЕЛЕЙ И МЫ НИКОГО НЕ ХОТИМ ОСКОРБИТЬ ИЛИ УНИЗИТЬ",
        'software': "Софты",
        'admins': "Администрация",
        'partners': "Партнёры",
        'main_admin': "Главный администратор",
        'creators': "Создатели",
        'senior_admins': "Старшие администраторы",
        'junior_admins': "Младшие администраторы",
        'senior_mods': "Старшие модераторы",
        'copyright': "© 2025 PrankVzlom. Все права защищены.",
        'accept': "Принять",
        'modal_title': "ВНИМАНИЕ",
        'modal_content': "Этот сайт создан исключительно в развлекательных целях. Мы не хотим никого оскорбить или унизить.",
        'links': {
            'official_channel': "ОФИЦИАЛЬНЫЙ КАНАЛ",
            'redirect': "ПЕРЕХОДНИК",
            'chat': "ЧАТ",
            'tutorial': "ТУТОРИАЛ ПО КАМЕРАМ",
            'audio': "АУДИО КАНАЛ",
            'bot': "БОТ",
            'tiktok': "ТИК ТОК",
            'support': "ПОДДЕРЖКА"
        },
        'partner_owl': "Скоро..."
    },
    'en': {
        'info_title': "PrankVzlom 📹📔",
        'disclaimer': "THIS SITE IS FOR ENTERTAINMENT PURPOSES ONLY AND WE DON'T WANT TO OFFEND OR HUMILIATE ANYONE",
        'software': "Software",
        'admins': "Administration",
        'partners': "Partners",
        'main_admin': "Main Admin",
        'creators': "Creators",
        'senior_admins': "Senior Admins",
        'junior_admins': "Junior Admins",
        'senior_mods': "Senior Moderators",
        'copyright': "© 2025 PrankVzlom. All rights reserved.",
        'accept': "Accept",
        'modal_title': "WARNING",
        'modal_content': "This site is made for entertainment purposes only. We don't want to offend or humiliate anyone.",
        'links': {
            'official_channel': "OFFICIAL CHANNEL",
            'redirect': "REDIRECT",
            'chat': "CHAT",
            'tutorial': "CAMERA TUTORIAL",
            'audio': "AUDIO CHANNEL",
            'bot': "BOT",
            'tiktok': "TIKTOK",
            'support': "SUPPORT"
        },
        'partner_owl': "Soon..."
    }
}

# Главная страница
@app.route('/')
def index():
    lang = session.get('lang', 'ru')
    t = translations[lang]
    
    site_data = {
        "info": {
            "title": t['info_title'],
            "description": t['disclaimer'],
            "links": [
                {"name": t['links']['official_channel'], "url": "https://t.me/+_dzIExBP_yViZDk9"},
                {"name": t['links']['redirect'], "url": "https://t.me/prankzvon"},
                {"name": t['links']['chat'], "url": "https://t.me/+gUAplPwH9GhiMDg1"},
                {"name": t['links']['tutorial'], "url": "https://t.me/+1ZZKZBWjTHxjMDQ8"},
                {"name": t['links']['audio'], "url": "https://t.me/+Y77I8AtvLNM0OGUy"},
                {"name": t['links']['bot'], "url": "https://t.me/prankvzlomnewbot"},
                {"name": t['links']['tiktok'], "url": "https://www.tiktok.com/@jiarbuz"},
                {"name": t['links']['support'], "url": "https://t.me/PrankVzlomUnban"}
            ]
        },
        "software": [
            {"name": "SmartPSS", "url": "https://cloud.mail.ru/public/11we/vbzNxnSQi"},
            {"name": "Nesca", "url": "https://cloud.mail.ru/public/J2sJ/3vuy7XC1n"},
            {"name": "Noon", "url": "https://cloud.mail.ru/public/4Cmj/yMeVGQXE6"},
            {"name": "Ingram", "url": "https://cloud.mail.ru/public/nPCQ/JA73sB4tq"},
            {"name": "SoundPad", "url": "https://mega.nz/file/Ck4jhZBL#bXmvrKCquhJrt2hMlHiV2QfpzMm3uj_lLjv9yFLEjgA"},
            {"name": "iVMS-4200", "url": "https://cloud.mail.ru/public/8t1M/g5zfvA8Lq"},
            {"name": "MVFPS", "url": "https://cloud.mail.ru/public/26ae/58VrzdvYT"},
            {"name": "KPortScan", "url": "https://cloud.mail.ru/public/yrup/9PQyDe86G"}
        ],
        "admins": {
            t['main_admin']: [
                {
                    "name": "Православный Бес", 
                    "url": "https://t.me/bes689",
                    "avatar": "https://ltdfoto.ru/images/2025/07/25/photo_2025-07-25_06-19-13.jpg"
                }
            ],
            t['creators']: [
                {
                    "name": "Everyday", 
                    "url": "https://t.me/mobile_everyday",
                    "avatar": "https://i.ibb.co/spKRJcmK/photo-2025-05-23-16-45-24.jpg"
                },
                {
                    "name": "Андрей", 
                    "url": "https://t.me/prankzvon231",
                    "avatar": None
                },
                {
                    "name": "Lucper", 
                    "url": "https://t.me/lucper1",
                    "avatar": "https://i.ibb.co/TMbSG0jp/photo-2025-07-20-01-44-45-2.gif"
                }
            ],
            t['senior_admins']: [
                {
                    "name": "Диванный воин Кчау", 
                    "url": "https://t.me/bestanov",
                    "avatar": "https://i.ibb.co/rKLcJ70c/photo-2025-04-23-02-37-37.jpg"
                },
                {
                    "name": "JIARBUZ.exe", 
                    "url": "https://t.me/jiarbuz",
                    "avatar": "https://i.ibb.co/kgBVDqM8/photo-2025-06-10-15-16-39.jpg"
                },
                {
                    "name": "ximi13p", 
                    "url": "https://t.me/ximi13p",
                    "avatar": None
                }
            ],
            t['junior_admins']: [
                {
                    "name": "k3stovski", 
                    "url": "https://t.me/k3stovski",
                    "avatar": "https://ltdfoto.ru/images/2025/07/25/photo_2025-07-24_23-01-05.jpg"
                },
                {
                    "name": "kronaфacia", 
                    "url": "https://t.me/kronaphasia",
                    "avatar": None
                },
                {
                    "name": "Жук", 
                    "url": "https://t.me/werwse",
                    "avatar": "https://ltdfoto.ru/images/2025/07/25/photo_2025-07-23_22-07-41.md.jpg"
                },
                {
                    "name": "Цыфра", 
                    "url": "https://t.me/himera_unturned",
                    "avatar": "https://ltdfoto.ru/images/2025/07/25/photo_2025-07-01_00-52-02.md.jpg"
                },
                {
                    "name": "Наполеонский пистолэт", 
                    "url": "https://t.me/prnkzvn",
                    "avatar": "https://ltdfoto.ru/images/2025/07/25/photo_2025-07-20_04-28-28.jpg"
                }
            ],
            t['senior_mods']: [
                {
                    "name": "Paul Du Rove", 
                    "url": "tg://openmessage?user_id=7401067755",
                    "avatar": "https://ltdfoto.ru/images/2025/07/25/photo_2025-05-03_16-27-45.jpg"
                },
                {
                    "name": "aiocryp", 
                    "url": "https://t.me/aiocryp",
                    "avatar": "https://ltdfoto.ru/images/2025/07/25/photo_2025-07-25_00-37-50.jpg"
                },
                {
                    "name": "саня шпалин", 
                    "url": "https://t.me/sanya_shpalka",
                    "avatar": "https://ltdfoto.ru/images/2025/07/25/photo_2025-07-22_03-52-56.md.jpg"
                }
            ]
        },
        "partners": [
            {
                "name": t['partner_owl'],
                "url": "https://youtu.be/dQw4w9WgXcQ",
                "avatar": "https://cdn-icons-png.flaticon.com/512/8890/8890972.png"
            }
        ],
        "translations": t
    }
    return render_template('index.html', data=site_data, current_lang=lang)

# Установка языка
@app.route('/set_language/<lang>')
def set_language(lang):
    if lang in ['ru', 'en']:
        session['lang'] = lang
    return '', 204

# Обработчик 404 ошибки
@app.errorhandler(404)
def page_not_found(e):
    lang = session.get('lang', 'ru')
    t = translations[lang]
    
    if lang == 'ru':
        error_texts = {
            "title": "Упс!",
            "error_title": "404 - Страница потерялась",
            "error_message": "Похоже, эта страница решила взять выходной или переехала без предупреждения.",
            "fun_text": "Может быть, она ушла в запой с другими страницами?",
            "go_home": "Вернуться на главную"
        }
    else:
        error_texts = {
            "title": "Oops!",
            "error_title": "404 - Page Gone Missing",
            "error_message": "Looks like this page decided to take a vacation or moved without notice.",
            "fun_text": "Maybe it went partying with other pages?",
            "go_home": "Go to Homepage"
        }
    
    error_data = {
        "translations": {
            "title": t['info_title'],
            "error_texts": error_texts,
            "copyright": t['copyright']
        }
    }
    return render_template('404.html', data=error_data), 404

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)