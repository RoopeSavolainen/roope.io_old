from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

page = Blueprint('page', __name__, template_folder='templates/pages')

@page.route('/', defaults={'page': 'index'})
@page.route('/<page>')
def render(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)

