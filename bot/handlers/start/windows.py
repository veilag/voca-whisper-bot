from aiogram.types import ContentType
from aiogram_dialog import Window, StartMode

from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.media import StaticMedia

from .template import welcome_window_template
from ..states import StartDialogWindows, MenuDialogWindows

welcome_window: Window = Window(
    StaticMedia(
        path="bot/static/media/cover.jpg",
        type=ContentType.PHOTO
    ),

    welcome_window_template,

    Start(
        text=Const("✨ Открыть меню"),
        id="start_open_menu_button",
        state=MenuDialogWindows.main,
        mode=StartMode.RESET_STACK
    ),

    state=StartDialogWindows.main,
    parse_mode="HTML"
)
