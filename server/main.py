from flask import (render_template)


def setup_routes(app):
    @app.route('/')
    def my_index():
        return render_template('index.html', flask_token='Hello world')
