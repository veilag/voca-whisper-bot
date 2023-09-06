from aiogram_dialog.widgets.text import Jinja

main_window_template: Jinja = Jinja("""
𝗩𝗼𝗰𝗮𝗪𝗵𝗶𝘀𝗽𝗲𝗿
Твой личный ассистент
""")

about_project_template: Jinja = Jinja("""
𝗩𝗼𝗰𝗮𝗪𝗵𝗶𝘀𝗽𝗲𝗿
Твой личный ассистент

<b>Ссылки проекта</b>: <code> 
• Notion - о проекте
• Figma - дизайн ассеты
• GitHub - код </code>
""")
