from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.ext.asyncio import AsyncSession

from .dialog import dialog
from ..states import StartDialogWindows

router: Router = Router()
router.include_router(dialog)


@router.message(Command("start"))
async def handle_user_start(message: Message,
                            dialog_manager:
                            DialogManager,
                            session: AsyncSession):

    await dialog_manager.start(
        state=StartDialogWindows.main,
        mode=StartMode.RESET_STACK
    )
