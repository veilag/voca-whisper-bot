from asyncio import AbstractEventLoop, new_event_loop, set_event_loop

from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode

from bot import dp, async_engine
from bot.database.base import Base
from config import Config


# Run on python 3.10 and higher
# GitHub:

async def main() -> None:
    bot: Bot = Bot(
        token=Config.TELEGRAM_TOKEN,
        parse_mode=ParseMode.MARKDOWN
    )

    try:
        await bot.delete_webhook(
            drop_pending_updates=True
        )

        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

        await dp.start_polling(bot)

    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == "__main__":
    loop: AbstractEventLoop = new_event_loop()
    set_event_loop(loop)

    try:
        loop.run_until_complete(main())

    except KeyboardInterrupt as error:
        loop.close()
        print("Работа программы завершена")
