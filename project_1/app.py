from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def show_deparutes(departure):
    return render_template('departure.html')


@app.route('/tours/<id>/')
def show_tours(id):
    return render_template('tour.html')


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', 5000)
