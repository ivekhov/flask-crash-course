from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


app.debug = True
app.run('0.0.0.0', 5000)
