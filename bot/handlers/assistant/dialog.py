from aiogram_dialog import Dialog
from .windows import main_window, correct_sentence_window, free_answer_window

dialog: Dialog = Dialog(
    main_window,
    correct_sentence_window,
    free_answer_window
)
