from aiogram.enums import ParseMode
from aiogram.types import ContentType
from aiogram_dialog import Window

from aiogram_dialog.widgets.kbd import Button, Cancel, Row, Column, Back, SwitchTo, Group
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.media import StaticMedia, DynamicMedia

from .template import (welcome_window_template,
                       unsuccessful_guessed_word_window_template, end_of_game_window_template,
                       error_neuro_window_template, start_window_template)

from ..states import GameDialogWindows
from .data import game_start_data
from .events import show_cancel_state, hide_cancel_state, on_user_guess_input, continue_game, repeat_on_neuro_error, \
    handle_next_word

start_game_window: Window = Window(
    StaticMedia(
        path="bot/static/media/game/cover.jpg",
        type=ContentType.PHOTO
    ),
    start_window_template,

    SwitchTo(
        text=Const("🔥 Начать игру"),
        id="nothing",
        state=GameDialogWindows.main
    ),

    Cancel(
        text=Const("« Вернуться назад")
    ),

    state=GameDialogWindows.start,
    parse_mode=ParseMode.HTML
)

main_game_window: Window = Window(
    DynamicMedia("photo"),
    welcome_window_template,

    TextInput(
        id="game_user_guess_input",
        on_success=on_user_guess_input
    ),

    Group(
        Column(
            Button(
                text=Const("Остановить игру"),
                id="game_cancel_button",
                when="cancel_state_closed",
                on_click=show_cancel_state
            ),
            Button(
                text=Const("Пропустить слово »"),
                id="pass_word_button",
                on_click=handle_next_word,
                when="cancel_state_closed",
            ),
        ),

        Row(
            SwitchTo(
                text=Const("Да"),
                id="end_game_button",
                state=GameDialogWindows.end_of_game
            ),

            Button(
                text=Const("Продолжить"),
                id="continue_game_button",
                on_click=hide_cancel_state
            ),
            when="cancel_state_opened"
        ),
        when="is_neuro_not_processing"
    ),

    state=GameDialogWindows.main,
    parse_mode="HTML",
    getter=game_start_data
)

success_guessed_word_window: Window = Window(
    StaticMedia(
        path="bot/static/media/game/neuro/success.jpg",
        type=ContentType.PHOTO
    ),

    Button(
        id="continue_game_button",
        text=Const("Продолжить"),
        on_click=continue_game
    ),

    state=GameDialogWindows.successful_guessed_word,
    parse_mode=ParseMode.HTML,
    getter=game_start_data
)

unsuccessful_guessed_word_window: Window = Window(
    StaticMedia(
        path="bot/static/media/game/neuro/unsuccessfully.jpg",
        type=ContentType.PHOTO
    ),
    unsuccessful_guessed_word_window_template,

    Button(
        id="continue_game_button",
        text=Const("Продолжить"),
        on_click=continue_game
    ),

    state=GameDialogWindows.unsuccessful_guessed_word,
    parse_mode=ParseMode.HTML,
    getter=game_start_data
)

end_of_game_window: Window = Window(
    StaticMedia(
        path="bot/static/media/game/cover.jpg",
        type=ContentType.PHOTO
    ),
    end_of_game_window_template,

    Cancel(
        text=Const("« Вернуться назад")
    ),

    state=GameDialogWindows.end_of_game,
    getter=game_start_data,
    parse_mode=ParseMode.HTML
)

neuro_error_window: Window = Window(
    StaticMedia(
        path="bot/static/media/game/neuro/error.jpg",
        type=ContentType.PHOTO
    ),
    error_neuro_window_template,

    Cancel(
        text=Const("Завершить")
    ),
    SwitchTo(
        text=Const("↻ Попробовать еще раз"),
        state=GameDialogWindows.main,
        id="retry_attempt_button",
        on_click=repeat_on_neuro_error
    ),

    state=GameDialogWindows.error_neuro,
    parse_mode=ParseMode.HTML
)
