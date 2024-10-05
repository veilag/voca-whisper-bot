from asyncio import run
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from bot import dp
from config import Config

# Run on python 3.10 and higher
# GitHub: veilag/voca-whisper-bot


async def main() -> None:
    bot: Bot = Bot(
        token=Config.TELEGRAM_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    try:
        await bot.delete_webhook(
            drop_pending_updates=True
        )

        await dp.start_polling(bot)

    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == "__main__":
    run(main())
