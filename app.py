from flask import Flask, render_template, request, session
from flask_babel import Babel
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('20223b185377e4778f8366afc34f9af0e0f0a88bd7217b52d7f1fbe4460fb554', 'default-secret-key')

app.config['BABEL_DEFAULT_LOCALE'] = 'ru'
babel = Babel(app)

def get_locale():
    return session.get('lang') or request.accept_languages.best_match(['ru', 'en'])

babel.locale_selector_func = get_locale


# Словари переводов
translations = {
    'ru': {
        'info_title': "PrankVzlom 📹📔",
        'disclaimer': "САЙТ СДЕЛАН ДЛЯ РАЗВЛЕКАТЕЛЬНЫХ ЦЕЛЯХ И МЫ НИКОГО НЕ ХОТИМ ОСКОРБИТЬ ИЛИ УНИЗИТЬ",
        'software': "Софты",
        'admins': "СПИСОК АДМИНОВ",
        'partners': "Партнёры",
        'main_admin': "Главный",
        'creators': "Создатели",
        'senior_admins': "Старшие админы",
        'junior_admins': "Младшие админы",
        'senior_mods': "Старшие модераторы",
        'copyright': "© 2025 PrankVzlom. Все права защищены.",
        'accept': "Принять",
        'modal_title': "ВНИМАНИЕ",
        'modal_content': "Этот сайт создан исключительно в развлекательных целях. Мы не хотим никого оскорбить или унизить. Продолжая, вы подтверждаете, что понимаете это."
    },
    'en': {
        'info_title': "PrankVzlom 📹📔",
        'disclaimer': "THE SITE IS MADE FOR ENTERTAINMENT PURPOSES...",
        'software': "Software",
        'admins': "ADMINS LIST",
        'partners': "Partners",
        'main_admin': "Main Admin",
        'creators': "Creators",
        'senior_admins': "Senior Admins",
        'junior_admins': "Junior Admins",
        'senior_mods': "Senior Moderators",
        'copyright': "© 2025 PrankVzlom. All rights reserved.",
        'accept': "Accept",
        'modal_title': "WARNING",
        'modal_content': "This site is made for entertainment purposes only..."
    }
}

@app.route('/')
def index():
    lang = session.get('lang', 'ru')
    site_data = {
        "info": {
            "title": translations[lang]['info_title'],
            "description": translations[lang]['disclaimer'],
            "links": [
                {"name": "ОФИЦИАЛЬНЫЙ КАНАЛ", "url": "https://t.me/+_dzIExBP_yViZDk9"},
                {"name": "ПЕРЕХОДНИК", "url": "https://t.me/prankzvon"},
                {"name": "ЧАТ", "url": "https://t.me/+gUAplPwH9GhiMDg1"},
                {"name": "ТУТОР ПО КАМЕРАМ", "url": "https://t.me/+1ZZKZBWjTHxjMDQ8"},
                {"name": "КАНАЛ С АУДИО", "url": "https://t.me/+Y77I8AtvLNM0OGUy"},
                {"name": "БОТ", "url": "https://t.me/prankvzlomnewbot"},
                {"name": "ТИК ТОК", "url": "https://www.tiktok.com/@jiarbuz"},
                {"name": "ПОДДЕРЖКА PRANKVZLOM", "url": "https://t.me/PrankVzlomUnban"}
            ]
        },
        "software": [
            {"name": "SmartPSS", "url": "https://cloud.mail.ru/public/11we/vbzNxnSQi"},
            {"name": "Nesca", "url": "https://cloud.mail.ru/public/J2sJ/3vuy7XC1n"},
            {"name": "Noon", "url": "https://cloud.mail.ru/public/4Cmj/yMeVGQXE6"},
            {"name": "Ingram", "url": "https://cloud.mail.ru/public/nPCQ/JA73sB4tq"},
            {"name": "SoundPad", "url": "https://mega.nz/file/Ck4jhZBL#bXmvrKCquhJrt2hMlHiV2QfpzMm3uj_lLjv9yFLEjgA"}
        ],
        "admins": {
            translations[lang]['main_admin']: [{"name": "Православный Бес", "url": "https://t.me/bes689"}],
            translations[lang]['creators']: [
                {"name": "Everyday", "url": "https://t.me/mobile_everyday"},
                {"name": "Андрей", "url": "https://t.me/prankzvon231"},
                {"name": "Lucper", "url": "https://t.me/lucper1"}
            ],
            translations[lang]['senior_admins']: [
                {"name": "Диванный воин Кчау", "url": "https://t.me/bestanov"},
                {"name": "JIARBUZ.exe", "url": "https://t.me/jiarbuz"},
                {"name": "ximi13p", "url": "https://t.me/ximi13p"},
                {"name": "Цыфра", "url": "https://t.me/himera_unturned"}
            ],
            translations[lang]['junior_admins']: [
                {"name": "k3stovski", "url": "https://t.me/k3stovski"},
                {"name": "Наполеонский пистолэтPRNKZV", "url": "https://t.me/prnkzvn"},
                {"name": "жук", "url": "https://t.me/werwse"},
                {"name": "kronaфacia", "url": "https://t.me/kronaphasia"}
            ],
            translations[lang]['senior_mods']: [
                {"name": "aiocryp", "url": "https://t.me/aiocryp"},
                {"name": "саня шпалин", "url": "https://t.me/sanya_shpalka"}
            ]
        },
        "partners": [
            {"name": "Совиный патруль", "url": "https://t.me/+x90aZWxcI8ljZmQy"}
        ],
        "translations": translations[lang]
    }
    return render_template('index.html', data=site_data, current_lang=lang)

@app.route('/set_language/<lang>')
def set_language(lang):
    if lang in ['ru', 'en']:
        session['lang'] = lang
    return '', 204  # No content

if __name__ == '__main__':
    app.run(debug=True)

