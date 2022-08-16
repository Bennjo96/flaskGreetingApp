# flask App

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "Down_in_the_dm12"


@app.route('/home')
def home():
    flash("what's your name?, welcome to körber Pharma. please enter down below your name.")
    return render_template('index.html')


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    flash("Hi " + str(
        request.form['name_input']) + ", great to see you.. Welcome to Körber Pharma we deliver the Difference.")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
