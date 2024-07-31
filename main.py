from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, User
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.kbd import Button, Row, Url, Column, Multiselect, Radio
from aiogram_dialog.widgets.text import Const, Format, Multi, Case
from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

router = Router()


class StartSG(StatesGroup):
    start = State()

class SecondDialogSG(StatesGroup):
    start = State()

class LearningDialogSG(StatesGroup):
    start = State()


class PythonLearningDialogSG(StatesGroup):
    window_1 = State()

class PlusesLearningDialogSG(StatesGroup):
    window_1 = State()

class GolangLearningDialogSG(StatesGroup):
    window_1 = State()

class PythonBackendDialogSG(StatesGroup):
    window_1 = State()
    window_2 = State()
    window_3 = State()
    window_4 = State()

class PythonAIdevDialogSG(StatesGroup):
    window_1 = State()
    window_2 = State()
    window_3 = State()
    window_4 = State()

class PythonDataEngDialogSG(StatesGroup):
    window_1 = State()
    window_2 = State()
    window_3 = State()
    window_4 = State()



async def go_start(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=StartSG.start, mode=StartMode.RESET_STACK)


async def start_second(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=SecondDialogSG.start)


async def learning_button_started(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=LearningDialogSG.start)


async def help_button_clicked(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
        await callback.message.answer_sticker('CAACAgIAAxkBAAEMj3Fmp9b-aBkIQ38RhudhhslpJWsILQACZwADQDHADXhtfVrKFwABjjUE')
        await callback.message.answer('<b><code>Создатель</code>\n @aboutwaste3d</b> - Николай Сороколетов\n\n<code>Python developer | DevOps engineer</code>\n\nПо всем вопросам/с предложениями к нему')

async def python_learn(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=PythonLearningDialogSG.window_1)

async def plusses_learn(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=PlusesLearningDialogSG.window_1)

async def golang_learn(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=GolangLearningDialogSG.window_1)

async def python_go_back(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.back()

async def python_go_next(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.next()
    
async def python_backend_cources(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=PythonBackendDialogSG.window_1)

async def python_aidev_course(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=PythonAIdevDialogSG.window_1)

async def python_data_engineering_course(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(state=PythonDataEngDialogSG.window_1)


async def username_getter(event_from_user: User, **kwargs):
    return {'username': event_from_user.username}


start_dialog = Dialog(
    Window(
        Format('<b>Привет, {username} 👋</b>\n'),
        Const('Нажми на кнопку, чтобы подтвердить, что ты не <code>робот</code>'),
        Button(Const('⚡️ Я не робот'), id='go_second', on_click=start_second),
        getter=username_getter,
        state=StartSG.start
    ),
)



second_dialog = Dialog(
    Window(
        Const('<b>Главное меню</b>'),
        Button(text=Const('Roadmaps'), id = 'learn_button', on_click = learning_button_started),
        Button(text=Const('Помощь'), id = 'help_button', on_click = help_button_clicked),
        state=SecondDialogSG.start
    ),
)

learning_dialog = Dialog(
    Window(
        Const('<code>Выберите язык для получения <b>roadmap</b></code>'),
        Column(
            Button(text=Const('🐍 Python'), id = 'python_learn', on_click=python_learn),
            Button(text=Const('💫 C++'), id = 'pluss_learn', on_click=plusses_learn),
            Button(text=Const('🦫 Golang'), id = 'go_learn', on_click=golang_learn),
        ),
        Button(text=Const('Назад'), id = 'back_button_menu', on_click=start_second),
        state = LearningDialogSG.start,
    ),
)

python_learn_dialog = Dialog(
    Window(
        Const('Выберите пункт из меню'),
        Button(Const('Backend'), id='backend_python_course', on_click=python_backend_cources),
        Button(Const('Data Science'), id = 'ML_developer_python_course', on_click=python_aidev_course),
        Button(Const('Data engineering'), id = 'data_eng_course', on_click=python_data_engineering_course),
        state=PythonLearningDialogSG.window_1
    )
)

python_backend_dialog = Dialog(
    Window(
        Const('Контроль версий Git'),
        Url(Const('Git'), url=Const('https://www.youtube.com/watch?v=O00FTZDxD0o'), id='git_py'),
        Button(Const('▶️ Вперед'), id = 'python_backend_next_1', on_click=python_go_next),
        Button(Const('Вернуться в меню'), id = 'python_backend_1_menu', on_click=learning_button_started),
        state=PythonBackendDialogSG.window_1
    ),
    Window(
        Const('Основы python + ООП'),
        Url(Const('База python'), url=Const('https://code-basics.com/ru/languages/python'), id = 'baza_py'),
        Url(Const('ООП'),url=Const('https://www.youtube.com/watch?v=Z7AY41tE-3U&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E'), id = 'oop_py'),
        Row(
            Button(Const('◀️ Назад'), id = 'python_backend_back_2', on_click=python_go_back),
            Button(Const("▶️ Вперед"), id = 'python_backend_next_2', on_click=python_go_next),
        ),
        Button(Const('Вернуться в меню'), id = 'python_backend_2_menu', on_click=learning_button_started),
        state=PythonBackendDialogSG.window_2
    ),
    Window(
        Const('Python FastAPI | Django'),
        Url(Const('Fast API'), url=Const('https://www.youtube.com/playlist?list=PLeLN0qH0-mCVQKZ8-W1LhxDcVlWtTALCS'), id='fastapi_py'),
        Url(Const('Django'), url=Const('https://www.youtube.com/watch?v=wOjicN2OXbs&list=PLBheEHDcG7-nyRX-kMT2jyudahDQ-A-Ss'), id='django_py'),
        Row(
            Button(Const('◀️ Назад'), id = 'python_backend_back_3', on_click=python_go_back),
            Button(Const("▶️ Вперед"), id = 'python_backend_next_3', on_click=python_go_next),
        ),
        Button(Const('Вернуться в меню'), id = 'python_backend_3_menu', on_click=learning_button_started),
        state=PythonBackendDialogSG.window_3
    ),
    Window(
        Const('Что делать дальше?'),
        Format('Вот ты и прочитал первый <code>роадмап</code>, созданный мной в рамках этого бота.\nНаверняка у тебя возник вопрос: "а что же делать дальше?"\n\nКонечно же изучать <b>сеть и интернет изнутри</b>, <b>разные БД</b> и развивать в себе <b>софт-скиллы</b>.\n\nМогу лишь посоветовать свой <code>мини-ТГК</code>, в который я буду сливать полезную информацию.'),
        Url(Const('ТГК с курсами'), url=Const('https://t.me/waste3dinfo'), id='tgk_mini'),
        Button(Const('◀️ Назад'), id = 'python_backend_next_4', on_click=python_go_back),
        Button(Const('Вернуться в меню'), id = 'python_backend_4_menu', on_click=learning_button_started),
        state=PythonBackendDialogSG.window_4,
        getter=username_getter,
    ),
)

python_data_science_dialog = Dialog(
   Window(
        Const('Базовые навыки статистики и математики\nСуществует огромное количество курсов в интернете, которые\nрасскажут тебе об основах статистики и мат. анализа,\nя посоветую это видео с ютуба'),
        Url(Const('Где и как учить математику ?'), url=Const('https://www.youtube.com/watch?v=6ajAbghWzrs&t=147s'), id='math_py'),
        Button(Const('▶️ Вперед'), id = 'python_ai_next_1', on_click=python_go_next),
        Button(Const('Вернуться в меню'), id = 'python_ai_1_menu', on_click=learning_button_started),
        state=PythonAIdevDialogSG.window_1
    ),
    Window(
        Const('<code>Основы python + ООП.</code> Python один из самых частых\nвыборов среди всех дата сайнтистов. Он пользуется <b>наибольшей популярностью</b>\n\n(ДА, И ЗДЕСЬ ПИТОН 🐍)'),
        Url(Const('База python'), url=Const('https://code-basics.com/ru/languages/python'), id = 'baza_py'),
        Url(Const('ООП'),url=Const('https://www.youtube.com/watch?v=Z7AY41tE-3U&list=PLA0M1Bcd0w8zPwP7t-FgwONhZOHt9rz9E'), id = 'oop_py'),
        Row(
            Button(Const('◀️ Назад'), id = 'python_ai_back_2', on_click=python_go_back),
            Button(Const("▶️ Вперед"), id = 'python_ai_next_2', on_click=python_go_next),
        ),
        Button(Const('Вернуться в меню'), id = 'python_ai_2_menu', on_click=learning_button_started),
        state=PythonAIdevDialogSG.window_2
    ),
    Window(
        Const('<code>Pandas, NumPy, Scipy</code> - самый частый выбор среди сайнтистов.\nЭти библиотеки пригодятся в <b>ЛЮБОМ</b> случае во время работы.\n\nБольшая часть информации на английском 🇬🇧'),
        Url(Const('Pandas'), url=Const('https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS'), id='pandas_py'),
        Url(Const('NumPy (арабский курс 👳🏻)'), url=Const('https://www.youtube.com/watch?v=5-5CrLmf2vk&list=PLIA_seGogbkGDYq-dnVCsELEIq_7HK7Ca'), id='num_py'),
        Url(Const('Scipy (github tutorial)'), url=Const('https://cs231n.github.io/python-numpy-tutorial/#scipy'), id = 'scipy_py'),
        Row(
            Button(Const('◀️ Назад'), id = 'python_ai_back_3', on_click=python_go_back),
            Button(Const("▶️ Вперед"), id = 'python_ai_next_3', on_click=python_go_next),
        ),
        Button(Const('Вернуться в меню'), id = 'python_ai_3_menu', on_click=learning_button_started),
        state=PythonAIdevDialogSG.window_3
    ),
    Window(
       Const('Что делать дальше?'),
        Format('Вот ты и прочитал воторой <code>роадмап</code>, созданный мной в рамках этого бота. (счет закончился)\nЧто делать дальше?\n\n Почитать еще роадмапы, изучить <b>базы данных</b>, <b>pytorch</b> и учить <b>МАТЕМАТИКУ!</b>.\n\nИ, да, опять впихну свой <code>мини-ТГК</code>, в который я буду сливать полезную инфу.'),
        Url(Const('ТГК с курсами'), url=Const('https://t.me/waste3dinfo'), id='tgk_mini'),
        Button(Const('◀️ Назад'), id = 'python_ai_next_4', on_click=python_go_back),
        Button(Const('Вернуться в меню'), id = 'python_ai_4_menu', on_click=learning_button_started),
        state=PythonAIdevDialogSG.window_4,
        getter=username_getter,
    ),
)

python_data_eng_dialog = Dialog(
    Window(
        Const('Python, python, python! 🐍'),
        Url(Const('PYTHON ДЛЯ АНАЛИЗА ДАННЫХ? (eng)'), url=Const('https://www.youtube.com/playlist?list=PL5-da3qGB5ICCsgW1IHykI9tC7mXXhxmr'), id='data_eng_py'),
        Button(Const('▶️ Вперед'), id = 'python_deng_next_1', on_click=python_go_next),
        Button(Const('Вернуться в меню'), id = 'python_deng_1_menu', on_click=learning_button_started),
        state=PythonDataEngDialogSG.window_1
    ),
    Window(
        Const('Apache (spark + hadoop), хз что это 🥷'),
        Row(
            Url(Const('Apache Spark 🦈 (Docs)'), url = Const('https://spark.apache.org/docs/latest/'), id = 'apache_py'),
            Url(Const('Apache Hadoop (Docs)'), url = Const('https://hadoop.apache.org/docs/stable/'), id = 'apache_had_py'),
        ),
        Row(
            Button(Const('◀️ Назад'), id = 'python_dataeng_back_2', on_click=python_go_back),
            Button(Const("▶️ Вперед"), id = 'python_dataeng_next_2', on_click=python_go_next),
        ),
        Button(Const('Вернуться в меню'), id = 'python_dataeng_2_menu', on_click=learning_button_started),
        state=PythonDataEngDialogSG.window_2
    ),
    Window(
        Const('Базы данных (PostgreSQL, MySQL...)'),
        Row(
            Url(text=Const('PostgreSQL'), url=Const('https://www.postgresqltutorial.com/'), id='postgres_py'),
            Url(text=Const('MySQL'), url = Const('https://www.mysqltutorial.org/'), id = 'my_sql_eng'),
            Url(Const('MongoDB'), url = Const('https://university.mongodb.com/'), id = 'mongodb'),
        ),
        Row(
            Button(Const('◀️ Назад'), id = 'python_dataeng_back_3', on_click=python_go_back),
            Button(Const("▶️ Вперед"), id = 'python_dataeng_next_3', on_click=python_go_next),
        ),
        Button(Const('Вернуться в меню'), id = 'python_dataeng_3_menu', on_click=learning_button_started),
        state=PythonDataEngDialogSG.window_3
    ),
    Window(
        Const('Что делать дальше?\n\nСоветую почитать данный роадмап (https://github.com/shnoh-hann/fo-data-engineer-roadmap). Информацию, кстати, я брал из него. <b>ТГК!</b>'),
        Url(Const('ТГК'), url=Const('https://t.me/waste3dinfo'), id = 'next_data_eng'),
        Button(Const('◀️ Назад'), id = 'python_dataeng_next_4', on_click=python_go_back),
        Button(Const('Вернуться в меню'), id = 'python_dataeng_4_menu', on_click=learning_button_started),
        state=PythonDataEngDialogSG.window_4
    ),
)

plusses_learn_dialog = Dialog(
    Window(
        Const('<b>первый</b>'),
        Button(Const('Вперед ▶️'), id='b_next', on_click=python_go_next),
        Button(text=Const('Вернуться в меню'), id = 'back_in_menu_pls_1', on_click=learning_button_started),
        state = PlusesLearningDialogSG.window_1
    )

)

golang_learn_dialog = Dialog(
    Window(
        Const('<b>первый</b>'),
        Button(Const('Вперед ▶️'), id='b_next', on_click=python_go_next),
        Button(text=Const('Вернуться в меню'), id = 'go_in_menu_1', on_click=learning_button_started),
        state = GolangLearningDialogSG.window_1
    )
)

@router.message(CommandStart())
async def start_proccess_command(message:Message, dialog_manager:DialogManager):
    await dialog_manager.start(state=StartSG.start, mode = StartMode.RESET_STACK)

dp.include_router(router)
dp.include_routers(start_dialog, second_dialog, learning_dialog, python_learn_dialog, golang_learn_dialog, plusses_learn_dialog, python_backend_dialog, python_data_eng_dialog, python_data_science_dialog)
setup_dialogs(dp)
dp.run_polling(bot)