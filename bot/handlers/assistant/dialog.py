from aiogram_dialog import Dialog
from aiogram_dialog import DialogManager

from .windows import main_window, correct_sentence_window

dialog: Dialog = Dialog(
    main_window,
    correct_sentence_window
)
