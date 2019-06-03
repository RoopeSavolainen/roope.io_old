from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from website.link import Link

blogs = [
    Link('Example', 'example'),
]

blog = Blueprint('blog', __name__, template_folder='content/blog')

@blog.route('/<blog>')
def render(blog):
    try:
        return render_template('%s.html' % blog)
    except TemplateNotFound:
        abort(404)

