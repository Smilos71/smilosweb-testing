# app.py
from flask import Flask, render_template, request, redirect, url_for
from database import create_form, get_forms, create_response

app = Flask(__name__)

@app.route('/')
def index():
    forms = get_forms()
    return render_template('index.html', forms=forms)

@app.route('/create_form', methods=['GET', 'POST'])
def create_form():
    if request.method == 'POST':
        title = request.form['title']
        questions = request.form['questions']
        create_form(title, questions)
        return redirect(url_for('index'))
    return render_template('create_form.html')

@app.route('/fill_form/<int:form_id>', methods=['GET', 'POST'])
def fill_form(form_id):
    if request.method == 'POST':
        response = request.form['response']
        create_response(form_id, response)
        return redirect(url_for('index'))
    form = get_form(form_id)
    return render_template('fill_form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
