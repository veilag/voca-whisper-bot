from aiogram_dialog import Dialog
from .windows import main_window, about_window, report_window, about_design_window, about_code_window

dialog: Dialog = Dialog(
    main_window,

    about_window,
    about_design_window,
    about_code_window,

    report_window
)
