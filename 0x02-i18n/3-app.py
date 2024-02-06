#!/usr/bin/env python3
"""Flask app with internationalization using Babel"""

from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


@app.route('/')
def index():
    """Route handler for the / route."""
    return render_template('3-index.html', title=_('home_title'), header=_('home_header'))


@babel.localeselector
def get_locale():
    """Determine the best-matching language for the user."""
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    app.config.from_object(Config)
    app.run(host='0.0.0.0', port=5000)
