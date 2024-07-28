import random
from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, User
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.kbd import Button, Row, Url, Column
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

async def first_button_clicked(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await callback.message.edit_text(text='<b>курсы по Python</b>')
    await dialog_manager.done()

async def second_button_clicked(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await callback.message.edit_text(text='<b>курсы по C++</b>')
    await dialog_manager.done()

async def third_button_clicked(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await callback.message.edit_text(text='<b>курсы по Go</b>')
    await dialog_manager.done()

async def name_getter(event_from_user: User, **kwargs):
    return{'name': event_from_user.first_name}


start_dialog = Dialog(
    Window(
        Format('Привет, {name}! выбери пункт из меню.'),
        Column(
            Button(text=Const('Python'), id = 'first_button', on_click=first_button_clicked),
            Button(text=Const('C++'), id='second_button', on_click=second_button_clicked),
            Button(text=Const('Go'), id = 'third_button', on_click=third_button_clicked)
        ),
        state=StartSG.start,
        getter=name_getter,
    ),
)

@router.message(CommandStart())
async def start_proccess_command(message:Message, dialog_manager:DialogManager):
    await dialog_manager.start(state=StartSG.start, mode = StartMode.RESET_STACK)

dp.include_router(router)
dp.include_router(start_dialog)
setup_dialogs(dp)
dp.run_polling(bot)