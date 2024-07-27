from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '58777yg9483647777777f8467677677ggh7'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
