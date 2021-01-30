from flask import Flask, render_template
import data


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


@app.route('/data')
def show_all():
    response = '<h1>Все туры:</h1>'
    for id in data.tours.keys():
        item = data.tours[id]
        response += f'<p>{item["country"]}: <a href="/data/tours/{id}">{item["title"]} & {item["price"]} {item["stars"]} </a></p>'
    return response


@app.route('/data/departures/<departure>')
def show_direction(departure):
    response = f'<h1>Туры по направлению {data.cities[departure]}:</h1>'
    for id in data.tours.keys():
        item = data.tours[id]
        if item['departure'] == departure:
            response += f'<p>{item["country"]}: <a href="/data/tours/{id}">{item["title"]} & {item["price"]} {item["stars"]} </a></p>'
    return response


@app.route('/data/tours/<tour_id>')
def show_tour(tour_id):
    item = data.tours[int(tour_id)]
    response = f'<h1>{item["country"]}: {item["title"]} {item["price"]}:</h1>'
    response += f'<p>{item["nights"]} ночей</p>'
    response += f'<p>{item["price"]} рублей</p>'
    response += f'<p>{item["description"]}</p>'
    return response


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', 5000)
