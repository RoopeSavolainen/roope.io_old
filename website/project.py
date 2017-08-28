from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

project = Blueprint('project', __name__, template_folder='templates/projects')

@project.route('/<project>')
def render(project):
    try:
        return render_template('%s.html' % project)
    except TemplateNotFound:
        abort(404)

