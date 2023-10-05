#!/usr/bin/env python3
"""
basic flask app
"""


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """ configures available languages """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/')
def index():
    """ homepage """
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """ Retrieves locale from request """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)

if __name__ == '__main__':
    app.run()
