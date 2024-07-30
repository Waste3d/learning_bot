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
from dialogs.dialogs import python_backend_dialog

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
        await callback.message.answer('<b><code>Создатель</code>\n @waste3d</b> - Николай Сороколетов\n\n<code>Python developer | DevOps engineer</code>\n\nПо всем вопросам/с предложениями к нему')

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

python_backend_dialog(Dialog)

python_data_science_dialog = Dialog(
   Window(
        Const(''),
        Button(Const('▶️ Вперед'), id = 'python_datascience_next_1', on_click=python_go_next),
        Button(Const('Вернуться в меню'), id = 'python_datascience_1_menu', on_click=learning_button_started),
        state=PythonAIdevDialogSG.window_1
    ),
    Window(
        Const('data science 2'),
        Row(
            Button(Const('◀️ Назад'), id = 'python_datascience_back_2', on_click=python_go_back),
            Button(Const("▶️ Вперед"), id = 'python_datascience_next_2', on_click=python_go_next),
        ),
        Button(Const('Вернуться в меню'), id = 'python_datascience_2_menu', on_click=learning_button_started),
        state=PythonAIdevDialogSG.window_2
    ),
    Window(
        Const('data science 3'),
        Row(
            Button(Const('◀️ Назад'), id = 'python_datascience_back_3', on_click=python_go_back),
            Button(Const("▶️ Вперед"), id = 'python_datascience_next_3', on_click=python_go_next),
        ),
        Button(Const('Вернуться в меню'), id = 'python_datascience_3_menu', on_click=learning_button_started),
        state=PythonAIdevDialogSG.window_3
    ),
    Window(
        Const('data science 4'),
        Button(Const('◀️ Назад'), id = 'python_datascience_next_4', on_click=python_go_back),
        Button(Const('Вернуться в меню'), id = 'python_datascience_4_menu', on_click=learning_button_started),
        state=PythonAIdevDialogSG.window_4
    ),
)

python_data_eng_dialog = Dialog(
    Window(
        Const('data engineering 1'),
        Button(Const('▶️ Вперед'), id = 'python_dataeng_next_1', on_click=python_go_next),
        Button(Const('Вернуться в меню'), id = 'python_dataeng_1_menu', on_click=learning_button_started),
        state=PythonDataEngDialogSG.window_1
    ),
    Window(
        Const('data engineering 2'),
        Row(
            Button(Const('◀️ Назад'), id = 'python_dataeng_back_2', on_click=python_go_back),
            Button(Const("▶️ Вперед"), id = 'python_dataeng_next_2', on_click=python_go_next),
        ),
        Button(Const('Вернуться в меню'), id = 'python_dataeng_2_menu', on_click=learning_button_started),
        state=PythonDataEngDialogSG.window_2
    ),
    Window(
        Const('data engineering 3'),
        Row(
            Button(Const('◀️ Назад'), id = 'python_dataeng_back_3', on_click=python_go_back),
            Button(Const("▶️ Вперед"), id = 'python_dataeng_next_3', on_click=python_go_next),
        ),
        Button(Const('Вернуться в меню'), id = 'python_dataeng_3_menu', on_click=learning_button_started),
        state=PythonDataEngDialogSG.window_3
    ),
    Window(
        Const('data engineering 4'),
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