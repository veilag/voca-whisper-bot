from aiogram.filters.state import StatesGroup, State


class StartDialogWindows(StatesGroup):
    main: State = State()


class GameDialogWindows(StatesGroup):
    start: State = State()
    main: State = State()

    neuro_process: State = State()

    successful_guessed_word: State = State()
    unsuccessful_guessed_word: State = State()
    end_of_game: State = State()

    error_neuro: State = State()


class MenuDialogWindows(StatesGroup):
    main: State = State()

    about: State = State()
    report: State = State()


class AssistantDialogWindows(StatesGroup):
    main: State = State()

    correct_sentence: State = State()
