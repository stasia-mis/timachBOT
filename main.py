import requests
from telegram import InlineQueryResultAudio, InlineQueryResultVoice
from telegram.ext import CommandHandler, Application, InlineQueryHandler

AUDIO_FILES = [
    {"title": "Если я пишу то ты кукарекаешь", "file_url": "https://raw.githubusercontent.com/stasia-mis/timachBOT/main/%D0%BA%D1%83%D0%BA%D0%B0%D1%80%D0%B5%D0%BA%D0%B0%D0%B5%D1%88%D1%8C.ogg"},
    {"title": "Ты ебанутый", "file_url": "https://raw.githubusercontent.com/stasia-mis/timachBOT/main/%D1%82%D1%8B-%D0%B5%D0%B1%D0%B0%D0%BD%D1%83%D1%82%D1%8B%D0%B9.ogg"},
    {"title": "Я сказал тебе закрыть рот", "file_url": "https://raw.githubusercontent.com/stasia-mis/timachBOT/main/%D1%8F-%D1%81%D0%BA%D0%B0%D0%B7%D0%B0%D0%BB-%D1%82%D0%B5%D0%B1%D0%B5-%D0%B7%D0%B0%D0%BA%D1%80%D1%8B%D1%82%D1%8C-%D1%80%D0%BE%D1%82.ogg"},
    {"title": "Скот поебать", "file_url": "https://raw.githubusercontent.com/stasia-mis/timachBOT/main/%D1%81%D0%BA%D0%BE%D1%82-%D0%BF%D0%BE%D0%B5%D0%B1%D0%B0%D1%82%D1%8C.ogg"}
]

# Проверка доступности аудиофайла
def check_file_access(url):
    try:
        response = requests.head(url)
        # Если ответ успешный (код 200)
        if response.status_code == 200:
            return True
    except Exception as e:
        print(f"Ошибка проверки файла {url}: {e}")
    return False

async def inline_query(update, context):
    results = []
    for audio in AUDIO_FILES:
        file_url = audio["file_url"]
        title = audio["title"]

        if check_file_access(file_url):
            # Отправка файла через InlineQueryResultAudio
            results.append(InlineQueryResultAudio(
                id=audio["title"], title=title, audio_url=file_url
            ))
        else:
            print(f"Не удалось загрузить файл: {title}")

    await update.inline_query.answer(results)

def main():
    application = Application.builder().token("7634770574:AAHOG5jyDzTYgqnufAS1nnYRYHhQZXwY3F8").build()

    application.add_handler(InlineQueryHandler(inline_query))

    application.run_polling()

if __name__ == '__main__':
    main()