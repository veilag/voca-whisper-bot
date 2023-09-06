from aiogram_dialog.widgets.text import Jinja

main_window_template: Jinja = Jinja("""
𝗩𝗼𝗰𝗮𝗪𝗵𝗶𝘀𝗽𝗲𝗿
Твой личный ассистент

<b>Попроси нейросеть</b> помочь объяснить слово или целое предложение,
<b>или помочь</b> объяснить смысл песни на английском
""")

correct_sentence_window_template: Jinja = Jinja("""
{% if not neuro_is_not_processing %}
<b>Исправленный ответ</b>: 
<code>{{ neuro_answer if neuro_answer != "" else "Загрузка..." }}</code>

<b>Объяснение</b>:
<code>{{ neuro_explanation if neuro_explanation != "" else "Загрузка..." }}</code>

{{ corrected_sentence }}

{% else %}
<b>Напиши предложение</b>, которое хочешь исправить

Нейросеть исправит ее и напишет исправленный вариант
{% endif %} 
""")
