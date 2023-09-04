from aiogram.enums import ParseMode
from aiogram.types import ContentType

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Cancel, SwitchTo, Checkbox
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.input import TextInput

from .data import assistant_start_data
from .events import on_user_sentence_input
from .template import main_window_template, correct_sentence_window_template
from ..states import AssistantDialogWindows

main_window: Window = Window(
    StaticMedia(
        path="bot/static/media/assistant/cover.jpg",
        type=ContentType.PHOTO
    ),

    main_window_template,

    Button(
        text=Const("Объяснить слово/фразу"),
        id="nothing",
    ),
    SwitchTo(
        text=Const("Исправить предложение"),
        id="go_to_correct_sentence",
        state=AssistantDialogWindows.correct_sentence
    ),
    Cancel(
        text=Const("« Вернуться назад"),
        id="back_to_menu_button"
    ),

    state=AssistantDialogWindows.main,
    parse_mode=ParseMode.HTML,
    getter=assistant_start_data
)

correct_sentence_window: Window = Window(
    StaticMedia(
        path="bot/static/media/assistant/cover.jpg",
        type=ContentType.PHOTO
    ),
    correct_sentence_window_template,

    TextInput(
        id="user_sentence_input",
        on_success=on_user_sentence_input
    ),

    Checkbox(
        checked_text=Const("✓ Объяснение на русском"),
        unchecked_text=Const("Объяснение на русском"),
        id="get_explanation_in_russian",
        default=True
    ),

    SwitchTo(
        text=Const("« Вернуться назад"),
        id="back_to_main_button",
        state=AssistantDialogWindows.main
    ),

    state=AssistantDialogWindows.correct_sentence,
    parse_mode=ParseMode.HTML,
    getter=assistant_start_data
)
