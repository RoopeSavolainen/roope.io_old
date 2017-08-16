workers = 4
pidfile = 'gunicorn.pid'
bind = 'unix:gunicorn.sock'
errorlog = 'error.log'
timeout = 10
daemon = True
