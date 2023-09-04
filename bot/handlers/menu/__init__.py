from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from .dialog import dialog
from ..states import MenuDialogWindows

router: Router = Router()
router.include_router(dialog)


@router.message(Command("menu"))
async def handle_menu(message: Message,
                      dialog_manager: DialogManager):

    await dialog_manager.start(
        state=MenuDialogWindows.main,
        mode=StartMode.RESET_STACK
    )
