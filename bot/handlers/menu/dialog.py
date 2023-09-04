from aiogram_dialog import Dialog
from .windows import main_window, about_window, report_window

dialog: Dialog = Dialog(
    main_window,

    about_window,
    report_window
)
