from aiogram.enums import ParseMode
from aiogram.types import ContentType

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Row, Start, SwitchTo, Back, Url
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.media import StaticMedia

from .template import main_window_template, about_project_template
from ..states import MenuDialogWindows, GameDialogWindows, AssistantDialogWindows

main_window: Window = Window(
    StaticMedia(
        path="bot/static/media/start/cover.jpg",
        type=ContentType.PHOTO
    ),
    main_window_template,

    Row(
        Start(
            text=Const("🎮 Игра"),
            id="go_to_game_dialog_button",
            state=GameDialogWindows.start
        ),
        Start(
            text=Const("🤖 ИИ Ассистент"),
            id="go_to_assistant_dialog_button",
            state=AssistantDialogWindows.main
        )
    ),

    Button(
        text=Const("⭐ Оценить"),
        id="nothing"
    ),

    Row(
        SwitchTo(
            text=Const("О проекте"),
            id="go_to_about_window_button",
            state=MenuDialogWindows.about
        ),
        SwitchTo(
            text=Const("Репорт"),
            id="review_error_button",
            state=MenuDialogWindows.report
        ),
    ),

    state=MenuDialogWindows.main,
    parse_mode=ParseMode.HTML
)

about_window: Window = Window(
    StaticMedia(
        path="bot/static/media/start/cover.jpg",
        type=ContentType.PHOTO
    ),
    about_project_template,

    Url(
        text=Const("📝 Notion"),
        id="notion_url_button",
        url=Const("https://notion.co")
    ),

    Row(
        Url(
            text=Const("🎨 Figma"),
            id="figma_url_button",
            url=Const("https://figma.com")
        ),
        Url(
            text=Const("‍💻 GitHub"),
            id="github_url_button",
            url=Const("https://github.com")
        ),
    ),

    Back(
        text=Const("« Вернуться назад")
    ),

    state=MenuDialogWindows.about,
    parse_mode=ParseMode.HTML
)

report_window: Window = Window(
    StaticMedia(
        path="bot/static/media/menu/report/cover.jpg",
        type=ContentType.PHOTO
    ),

    Button(
        text=Const("✏ Описать проблему"),
        id="nothing"
    ),
    Button(
        text=Const("📸 Прикрепить скриншот"),
        id="nothing"
    ),

    SwitchTo(
        text=Const("« Вернуться назад"),
        state=MenuDialogWindows.main,
        id="back_to_menu_button"
    ),

    state=MenuDialogWindows.report
)