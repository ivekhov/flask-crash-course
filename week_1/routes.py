from flask import Flask # сперва подключим модуль

app = Flask(__name__) # объявим экземпляр фласка


@app.route('/')
def render_main():
    return 'Здесь будет главная'


@app.route('/products/')
def render_products():
    return 'Продукты'


@app.route('/about/')
def render_about():
    return 'Информация о проекте'


@app.route('/videos/<video_id>/')
def render_videos_item(video_id):
    return "Здесь будет видео " + video_id


@app.route('/book/<int:book_id>/')
def render_book(book_id):
    print(type(book_id))
    return ""


@app.route('/temp/<float:temp_value>/')
def render_temp(temp_value):
    print(type(temp_value))
    return ""


@app.errorhandler(404)
def render_not_found(error):
    return "Что-то не так, но мы все починим:\n{}".format(error), 404


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим", 500


app.debug = True
app.run('0.0.0.0', 5000)
