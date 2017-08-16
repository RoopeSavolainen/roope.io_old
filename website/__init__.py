from flask import Flask
#from werkzeug.contrib.fixers import ProxyFix

#from site import views

site = Flask(__name__)
@site.route('/')
def hello():
    return 'Hello Flask!'

#app.wsgi_app = ProxyFix(app.wsgi_app)
