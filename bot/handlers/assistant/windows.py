from aiogram.enums import ParseMode
from aiogram.types import ContentType

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, SwitchTo, Checkbox
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.input import TextInput

from .data import assistant_start_data
from .events import on_user_sentence_input, on_user_question_input
from .template import main_window_template, correct_sentence_window_template, free_answer_window_template
from ..states import AssistantDialogWindows

main_window: Window = Window(
    StaticMedia(
        path="bot/media/assistant/cover.jpg",
        type=ContentType.PHOTO
    ),

    main_window_template,

    SwitchTo(
        text=Const("Свободный вопрос"),
        id="go_to_free_answer",
        state=AssistantDialogWindows.free_answer
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
        path="bot/media/assistant/cover.jpg",
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
        default=False
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

free_answer_window: Window = Window(
    StaticMedia(
        path="bot/media/assistant/cover.jpg",
        type=ContentType.PHOTO
    ),

    free_answer_window_template,

    TextInput(
        id="user_sentence_input",
        on_success=on_user_question_input
    ),

    Checkbox(
        checked_text=Const("✓ Объяснение на русском"),
        unchecked_text=Const("Объяснение на русском"),
        id="get_explanation_in_russian",
        default=False
    ),

    SwitchTo(
        text=Const("« Вернуться назад"),
        id="back_to_main_button",
        state=AssistantDialogWindows.main
    ),

    state=AssistantDialogWindows.free_answer,
    parse_mode=ParseMode.HTML,
    getter=assistant_start_data
)
