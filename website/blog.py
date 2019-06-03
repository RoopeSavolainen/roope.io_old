from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

blog = Blueprint('blog', __name__, template_folder='content/blog')

@blog.route('/<blog>')
def render(blog):
    try:
        return render_template('%s.html' % blog)
    except TemplateNotFound:
        abort(404)

