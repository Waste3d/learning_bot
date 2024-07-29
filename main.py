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
    window_2 = State()
    window_3 = State()
    window_4 = State()

class PlusesLearningDialogSG(StatesGroup):
    window_1 = State()
    window_2 = State()
    window_3 = State()
    window_4 = State()

class GolangLearningDialogSG(StatesGroup):
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
        await callback.message.answer('<b><code>Создатель</code>\n @waste3d</b> - Николай Сороколетов\n\n<code>Python developer | DevOps engineer</code>\n\nПо всем вопросам/с отзывами к нему')

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
        Button(text=Const('Обучение'), id = 'learn_button', on_click = learning_button_started),
        Button(text=Const('Помощь'), id = 'help_button', on_click = help_button_clicked),
        state=SecondDialogSG.start
    ),
)

learning_dialog = Dialog(
    Window(
        Const('<code>Выберите язык для <b>обучения</b></code>'),
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
        Const('Приветствую тебя на <b>первом</b> этапе обучения <code>Python</code>'),
        Button(Const('Вперед ▶️'), id='b_next', on_click=python_go_next),
        Button(Const('Вернуться в меню'), id = 'back_in_menu_py_1', on_click=learning_button_started),
        getter=username_getter,
        state=PythonLearningDialogSG.window_1
    ),
    Window(
        Const('Приветствую тебя на <b>втором</b> этапе обучения <code>Python</code>'),
        Row(
            Button(Const('◀️ Назад'), id='b_back', on_click=python_go_back),
            Button(Const('Вперед ▶️'), id='b_next', on_click=python_go_next),
        ),
        
        Button(Const('Вернуться в меню'), id = 'back_in_menu_py_2', on_click=learning_button_started),
        state=PythonLearningDialogSG.window_2
    ),
    Window(
        Const('Приветствую тебя на <b>третьем</b> этапе обучения <code>Python</code>'),
        Row(
            Button(Const('◀️ Назад'), id='b_back', on_click=python_go_back),
            Button(Const('Вперед ▶️'), id='b_next', on_click=python_go_next),
        ),
        Button(Const('Вернуться в меню'), id = 'back_in_menu_py_3', on_click=learning_button_started),
        state=PythonLearningDialogSG.window_3
    ),
    Window(
        Const('Приветствую тебя на <b>четвером</b> этапе обучения <code>Python</code>'),
        Button(Const('◀️ Назад'), id='b_back', on_click=python_go_back),
        Button(Const('Вернуться в меню'), id = 'back_in_menu_py_4', on_click=learning_button_started),
        state=PythonLearningDialogSG.window_4
    ),
)


plusses_learn_dialog = Dialog(
    Window(
        Const('<b>первый</b>'),
        Button(Const('Вперед ▶️'), id='b_next', on_click=python_go_next),
        Button(text=Const('Вернуться в меню'), id = 'back_in_menu_pls_1', on_click=learning_button_started),
        state = PlusesLearningDialogSG.window_1
    ),
    Window(
        Const('<b>второй</b>'),
        Row(
        Button(Const('◀️ Назад'), id='b_back', on_click=python_go_back),
        Button(Const('Вперед ▶️'), id='b_next', on_click=python_go_next),
        ),
        Button(text=Const('Вернуться в меню'), id = 'back_in_menu_pls_2', on_click=learning_button_started),
        state = PlusesLearningDialogSG.window_2
    ),
    Window(
        Const('<b>третий</b>'),
        Row(
        Button(Const('◀️ Назад'), id='b_back', on_click=python_go_back),
        Button(Const('Вперед ▶️'), id='b_next', on_click=python_go_next),
        ),
        Button(text=Const('Вернуться в меню'), id = 'back_in_menu_pls_3', on_click=learning_button_started),
        state = PlusesLearningDialogSG.window_3
    ),
    Window(
        Const('<b>четвертый</b>'),
        Button(Const('◀️ Назад'), id='b_back', on_click=python_go_back),
        Button(text=Const('Вернуться в меню'), id = 'back_in_menu_pls_4', on_click=learning_button_started),
        state = PlusesLearningDialogSG.window_4
    ),

)

golang_learn_dialog = Dialog(
    Window(
        Const('<b>первый</b>'),
        Button(Const('Вперед ▶️'), id='b_next', on_click=python_go_next),
        Button(text=Const('Вернуться в меню'), id = 'go_in_menu_1', on_click=learning_button_started),
        state = GolangLearningDialogSG.window_1
    ),
    Window(
        Const('<b>второй</b>'),
        Row(
        Button(Const('◀️ Назад'), id='b_back', on_click=python_go_back),
        Button(Const('Вперед ▶️'), id='b_next', on_click=python_go_next),
        ),
        Button(text=Const('Вернуться в меню'), id = 'go_in_menu_2', on_click=learning_button_started),
        state = GolangLearningDialogSG.window_2
    ),
    Window(
        Const('<b>третий</b>'),
        Row(
        Button(Const('◀️ Назад'), id='b_back', on_click=python_go_back),
        Button(Const('Вперед ▶️'), id='b_next', on_click=python_go_next),
        ),
        Button(text=Const('Вернуться в меню'), id = 'go_in_menu_3', on_click=learning_button_started),
        state = GolangLearningDialogSG.window_3
    ),
    Window(
        Const('<b>четвертый</b>'),
        Button(Const('◀️ Назад'), id='b_back', on_click=python_go_back),
        Button(text=Const('Вернуться в меню'), id = 'go_in_menu_4', on_click=learning_button_started),
        state = GolangLearningDialogSG.window_4
    ),
)

@router.message(CommandStart())
async def start_proccess_command(message:Message, dialog_manager:DialogManager):
    await dialog_manager.start(state=StartSG.start, mode = StartMode.RESET_STACK)

dp.include_router(router)
dp.include_routers(start_dialog, second_dialog, learning_dialog, python_learn_dialog, golang_learn_dialog, plusses_learn_dialog)
setup_dialogs(dp)
dp.run_polling(bot)