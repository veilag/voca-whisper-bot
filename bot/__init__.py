from aiogram import Dispatcher
from aiogram_dialog import setup_dialogs
from aiogram.fsm.storage.memory import MemoryStorage

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio.engine import AsyncEngine

from config import Config

from .handlers import start_router, game_router, menu_router, assistant_router
from .middlewares.db import DbSessionMiddleware


async_engine: AsyncEngine = create_async_engine(
    url=Config.DATABASE_URL
)

session_maker = async_sessionmaker(
    bind=async_engine
)

storage: MemoryStorage = MemoryStorage()

dp: Dispatcher = Dispatcher(
    storage=storage
)

dp.update.outer_middleware(
    DbSessionMiddleware(session_pool=session_maker)
)

dp.include_routers(
    menu_router, game_router, assistant_router, start_router
)

setup_dialogs(dp)
