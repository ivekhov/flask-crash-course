from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
# def template():
#     # output = render_template('test.html')
#
#     output = render_template('test.html', name="Alex", place="Lab")
#     # рендерим шаблон, передавая переменные
#
#     return output


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


app.debug = True
app.run('0.0.0.0', 5000)
