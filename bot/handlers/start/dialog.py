from aiogram_dialog import Dialog, LaunchMode

from .windows import (welcome_window)

dialog: Dialog = Dialog(
    welcome_window,
    launch_mode=LaunchMode.ROOT
)
