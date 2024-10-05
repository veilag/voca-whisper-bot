from aiogram import Dispatcher
from aiogram_dialog import setup_dialogs
from aiogram.fsm.storage.memory import MemoryStorage
from .handlers import start_router, game_router, menu_router, assistant_router

storage: MemoryStorage = MemoryStorage()

dp: Dispatcher = Dispatcher(
    storage=storage
)
dp.include_routers(
    menu_router, game_router,
    assistant_router, start_router
)

setup_dialogs(dp)
