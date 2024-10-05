from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram_dialog import DialogManager, StartMode

from .dialog import dialog
from ..states import StartDialogWindows

router: Router = Router()
router.include_router(dialog)


@router.message(Command("start"))
async def handle_user_start(
    _: Message,
    dialog_manager: DialogManager
):
    await dialog_manager.start(
        state=StartDialogWindows.main,
        mode=StartMode.RESET_STACK
    )
