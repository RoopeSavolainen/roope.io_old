def app(environ, start_response):
    f = open('res.txt', 'r')
    data = f.read()
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Lenth', str(len(data)))
        ])
    return iter([data])
