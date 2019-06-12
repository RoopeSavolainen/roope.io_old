from flask import render_template, abort
from jinja2 import TemplateNotFound

def error_page(e):
    try:
        return render_template('error.html', error=e), 404
    except TemplateNotFound:
        abort(500)
