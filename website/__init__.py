from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from website.page import page

site = Flask(__name__)
site.wsgi_app = ProxyFix(site.wsgi_app)

site.register_blueprint(page)

