from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import ManagedCheckbox

from ..neuro import process_prompt


async def correct_user_sentence(sentence: str) -> str | None:
    prompt: str = f"""
            Correct the sentence: {sentence}
            You have to answer with only corrected sentence
            """

    return await process_prompt(prompt)


async def answer_user_question(get_explanation_in_russian: bool,
                               question: str) -> str | None:

    prompt: str = ""

    if get_explanation_in_russian:
        prompt = f"""
                Ты должен ответить на вопрос, который будет ниже
                Вопрос: {question}
                
                Ты должен ответить на русском языке    
            """

    else:
        prompt = f"""
                You have to answer the question below
                The question: {question}
            """

    return await process_prompt(prompt)


async def get_correcting_explanation(get_explanation_in_russian: bool,
                                     sentence: str,
                                     corrected_sentence: str) -> str:
    prompt: str = ""

    if get_explanation_in_russian:
        prompt = f"""
                    Ты получаешь предложение: {sentence}
                    А также его исправленный вариант: {corrected_sentence}

                    Напиши, какие исправления были совершены и почему.
                    Твой ответ должно быть не более 800 символов в длину.
                    """

    else:
        prompt = f"""
                    You get an sentence: {sentence}
                    And its corrected version: {corrected_sentence}

                    Write down what corrections were made and why.
                    Your answer should not be longer than 800 characters in length.
                    """

    return await process_prompt(prompt)


async def on_user_sentence_input(message: Message,
                                 input: ManagedTextInput,
                                 dialog_manager: DialogManager,
                                 message_text: str):

    get_explanation_in_russian: ManagedCheckbox = dialog_manager.find("get_explanation_in_russian")

    await dialog_manager.update({
        "neuro_is_not_processing": False,
        "neuro_answer": "",
        "neuro_explanation": ""
    })

    corrected_sentence = await correct_user_sentence(message_text)

    await dialog_manager.update({
        "neuro_is_not_processing": False,
        "neuro_answer": corrected_sentence,
    })

    correcting_explanation = await get_correcting_explanation(get_explanation_in_russian=get_explanation_in_russian.is_checked(),
                                                              sentence=message_text,
                                                              corrected_sentence=corrected_sentence)

    limited_explanation = correcting_explanation[:1024 - len(corrected_sentence) - 50] + "..." if len(correcting_explanation) - len(corrected_sentence) - 50 > 1024 else correcting_explanation

    await dialog_manager.update({
        "neuro_explanation": limited_explanation
    })


async def on_user_question_input(message: Message,
                                 input: ManagedTextInput,
                                 dialog_manager: DialogManager,
                                 message_text: str):
    get_explanation_in_russian: ManagedCheckbox = dialog_manager.find("get_explanation_in_russian")

    await dialog_manager.update({
        "neuro_is_not_processing": False,
        "neuro_answer": "",
        "neuro_explanation": ""
    })

    neuro_answer = await answer_user_question(get_explanation_in_russian.is_checked(), message_text)

    await dialog_manager.update({
        "neuro_is_not_processing": False,
        "neuro_answer": neuro_answer,
    })

