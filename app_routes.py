from flask import abort
from flask import render_template
from flask import request
from flask import url_for

from services import db_service


def router(app):
    @app.route('/')
    def home():
        titles = db_service.get_titles()
        home_style =  url_for('static', filename='css/index.css')
        home_page_script =  url_for('static', filename='js/index.js')
        return render_template(
            'home.html',
            home_style=home_style,
            home_page_script=home_page_script,
            titles=titles
        )

    @app.route('/create', methods=['GET', 'POST'])
    def create_question():
        style_sheet =  url_for('static', filename='css/style.css')
        if request.method == 'GET':
            return render_template(
                'create_question.html',
                style_sheet=style_sheet
            )
        if request.method == 'POST':
            title = request.form['title']
            question = request.form['question']
            answer = request.form['answer']
            db_service.post_question(
                {
                    'title': title,
                    'question': question,
                    'answer': answer
                }
            )
            return render_template(
                'feedback/success.html',
                question=question,
                style_sheet=style_sheet
            )
        else:
            return "Invalid Request."

    @app.route('/question/<title>', methods=['GET', 'POST', 'DELETE'])
    def answer_question(title):
        style_sheet = url_for('static', filename='css/style.css')
        question = db_service.get_question(title)
        if question:
            if request.method == 'GET':
                return render_template(
                    'answer_question.html',
                    question=question['question'],
                    style_sheet=style_sheet
                )
            if request.method == 'POST':
                submitted_answer = request.form['answer']
                answer = question['answer']

                if str(submitted_answer).lower() in str(answer).lower():
                    return render_template(
                        'feedback/correct.html',
                        question=question['question'],
                        submitted_answer=submitted_answer,
                        style_sheet=style_sheet
                    )
                else:
                    return render_template(
                        'feedback/oops.html',
                        submitted_answer=submitted_answer,
                        answer=answer,
                        style_sheet=style_sheet
                    )
        else:
            abort(404)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('feedback/404.html'), 404
