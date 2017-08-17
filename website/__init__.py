from flask import Flask, render_template
from werkzeug.contrib.fixers import ProxyFix

site = Flask(__name__)
site.wsgi_app = ProxyFix(site.wsgi_app)

@site.route('/')
def hello():
    return page('index')

@site.route('/<page>')
def page(page):
    return render_template('pages/' + page + '.html')
