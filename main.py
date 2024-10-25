from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


# Route для главной страницы
@app.route('/')
def index():
    try:
        # Получаем случайную цитату с API, отключив проверку SSL-сертификата
        response = requests.get('https://api.quotable.io/random', verify=False)
        if response.status_code == 200:
            quote_data = response.json()
            quote = quote_data['content']
            author = quote_data['author']
        else:
            quote = "Не удалось загрузить цитату"
            author = ""
    except requests.exceptions.RequestException as e:
        quote = "Ошибка подключения к API"
        author = ""
        print(f"Error occurred: {e}")

    return render_template('index.html', quote=quote, author=author)


if __name__ == '__main__':
    app.run(debug=True)

