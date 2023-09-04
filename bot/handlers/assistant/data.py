from aiogram_dialog import DialogManager


async def assistant_start_data(dialog_manager: DialogManager, **kwargs):
    return {
        "neuro_is_not_processing": dialog_manager.dialog_data.get("neuro_is_not_processing", True),
        "is_explanation_showing": dialog_manager.dialog_data.get("is_explanation_showing", False),

        "neuro_answer": dialog_manager.dialog_data.get("neuro_answer", ""),
        "neuro_explanation": dialog_manager.dialog_data.get("neuro_explanation", "")
    }
