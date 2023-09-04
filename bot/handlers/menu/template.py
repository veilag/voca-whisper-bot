from aiogram_dialog.widgets.text import Jinja

main_window_template: Jinja = Jinja("""
На данный момент доступно: <code>
• Alias с нейросетью
• ИИ Ассистент</code>

⚠ Нейросеть может работать нестабильно, если у вас возникли проблемы при ответе нейросети, воспользуйтесь им позже
""")

about_project_template: Jinja = Jinja("""
<b>Ссылки проекта</b>: <code> 
• Notion - о проекте
• Figma - дизайн ассеты
• GitHub - код </code>
""")
