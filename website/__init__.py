from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from website.content import pages, blogs

from website.page import page
from website.blog import blog

from markdown import markdown

site = Flask(__name__, template_folder='content')
site.wsgi_app = ProxyFix(site.wsgi_app)

@site.context_processor
def inject_navlinks():
    return dict(navlinks=pages)

@page.context_processor
def inject_blogs():
    return dict(bloglinks=blogs)

@site.template_filter('markdown')
def markdown_filter(text):
    return markdown(text, extensions=['extra'])

site.register_blueprint(page)
site.register_blueprint(blog, url_prefix='/blog')
