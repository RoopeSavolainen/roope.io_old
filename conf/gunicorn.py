workers = 4
pidfile = 'gunicorn.pid'
bind = 'unix:gunicorn.sock'
pythonpath = 'src'
timeout = 10
daemon = True
