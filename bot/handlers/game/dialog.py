from .events import get_random_word
from aiogram_dialog import Dialog, DialogManager

from .windows import (start_game_window, main_game_window, success_guessed_word_window,
                      unsuccessful_guessed_word_window,
                      end_of_game_window, neuro_error_window)


async def set_global_state(
    _,
    dialog_manager: DialogManager
) -> None:

    random_word: str = await get_random_word()
    await dialog_manager.update({
        "word": random_word,
        "successfully_attempts": 0
    })


dialog: Dialog = Dialog(
    start_game_window,
    main_game_window,
    success_guessed_word_window,
    unsuccessful_guessed_word_window,
    neuro_error_window,
    end_of_game_window,

    on_start=set_global_state
)
