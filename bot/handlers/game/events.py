from aiogram.types import CallbackQuery, Message, ContentType
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.api.entities import MediaAttachment
from httpx import AsyncClient
from gpt.utils import process_prompt
from ..states import GameDialogWindows


async def guess_word_by_description(user_description: str) -> str | None:
    prompt: str = f"""
        You guess the words from the description.
        Your task is to determine which word will be described below.

        Be aware that the description may contain grammatical errors, 
        since it is written by a person who does not know English.

        Instead of trying to communicate with user, just say the word, that you guessed.

        Description: {user_description}
        """

    neuro_word: str | None = await process_prompt(prompt)
    return neuro_word


RANDOM_WORD_API = "https://random-word-api.vercel.app/api?words=1"
async def get_random_word() -> str:
    async with AsyncClient() as client:
        response = await client.get(RANDOM_WORD_API)
        return response.json()[0]


async def show_cancel_state(
    _: CallbackQuery,
    __: Button,
    dialog_manager: DialogManager
):

    await dialog_manager.update({
        "cancel_state_opened": True,
        "cancel_state_closed": False,
        "photo": MediaAttachment(
            type=ContentType.PHOTO,
            path="bot/media/game/stop.jpg"
        )
    })


async def hide_cancel_state(
    _: CallbackQuery,
    __: Button,
    dialog_manager: DialogManager
):

    await dialog_manager.update({
        "cancel_state_opened": False,
        "cancel_state_closed": True,
        "photo": MediaAttachment(
            type=ContentType.PHOTO,
            path="bot/static/media/game/process.jpg"
        )
    })


async def on_user_guess_input(
    _: Message,
    __: ManagedTextInput,
    dialog_manager: DialogManager,
    message_text: str
):

    await dialog_manager.update({
        "is_neuro_not_processing": False,
        "photo": MediaAttachment(
            type=ContentType.PHOTO,
            path="bot/media/game/neuro/process.jpg"
        )
    })

    word = dialog_manager.dialog_data.get("word")
    gpt_guess: str | None = await guess_word_by_description(
        user_description=message_text.lower()
    )

    if gpt_guess is None:
        await dialog_manager.switch_to(
            state=GameDialogWindows.error_neuro
        )
        return

    if word in gpt_guess.lower():
        await dialog_manager.update({
            "user_answer": message_text,
            "successfully_attempts": dialog_manager.dialog_data.get("successfully_attempts") + 1
        })

        await dialog_manager.switch_to(
            state=GameDialogWindows.successful_guessed_word
        )
        return

    await dialog_manager.update({
        "user_answer": message_text,
        "neuro_word": gpt_guess.lower()
    })

    await dialog_manager.switch_to(
        state=GameDialogWindows.unsuccessful_guessed_word
    )


async def continue_game(
    callback: CallbackQuery,
    _: Button,
    dialog_manager: DialogManager
):

    random_word: str = await get_random_word()
    await dialog_manager.update({
        "word": random_word,
        "is_neuro_not_processing": True,
        "photo": MediaAttachment(
            type=ContentType.PHOTO,
            path="bot/media/game/process.jpg"
        )
    })

    await callback.answer(
        text="Прыгаем дальше!"
    )

    await dialog_manager.switch_to(
        state=GameDialogWindows.main
    )


async def repeat_on_neuro_error(
    _: CallbackQuery,
    __: Button,
    dialog_manager: DialogManager
):

    await dialog_manager.update({
        "is_neuro_not_processing": True,
        "photo": MediaAttachment(
            type=ContentType.PHOTO,
            path="bot/media/game/process.jpg"
        )
    })

    await dialog_manager.switch_to(
        state=GameDialogWindows.main
    )


async def handle_next_word(
    callback: CallbackQuery,
    _: Button,
    dialog_manager: DialogManager
):

    random_word: str = await get_random_word()
    await callback.answer(
        text="Новое слово загружено"
    )

    await dialog_manager.update({
        "word": random_word,
    })
