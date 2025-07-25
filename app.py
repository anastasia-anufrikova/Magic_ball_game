from flask import Flask, render_template, request
import random

app = Flask(__name__)

answers = [
    'Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да',
    'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего',
    'Хорошие перспективы', 'Знаки говорят - да', 'Да',
    'Пока не ясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать',
    'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
    'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
    'Перспективы не очень хорошие', 'Весьма сомнительно'
]

@app.route('/', methods=['GET', 'POST'])
def magic_ball():
    answer = None
    question = None

    if request.method == 'POST':
        question = request.form.get('question')
        if question:
            answer = random.choice(answers)
        else:
            answer = "Пожалуйста, задайте вопрос, чтобы я мог ответить!"

    return render_template('index.html', question=question, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)