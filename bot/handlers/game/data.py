from aiogram.types import ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment


async def game_start_data(dialog_manager: DialogManager, **kwargs):
    return {
        "cancel_state_opened": dialog_manager.dialog_data.get("cancel_state_opened", False),
        "cancel_state_closed": dialog_manager.dialog_data.get("cancel_state_closed", True),

        "is_neuro_not_processing": dialog_manager.dialog_data.get("is_neuro_not_processing", True),

        "neuro_word": dialog_manager.dialog_data.get("neuro_word", ""),
        "game_in_progress": dialog_manager.dialog_data.get("game_in_progress", True),

        "word": dialog_manager.dialog_data.get("word", None),
        "word_list": dialog_manager.dialog_data.get("word_list", None),

        "successfully_attempts": dialog_manager.dialog_data.get("successfully_attempts", 0),
        "photo": dialog_manager.dialog_data.get("photo", MediaAttachment(
            type=ContentType.PHOTO,
            path="bot/media/game/process.jpg"
        ))
    }
