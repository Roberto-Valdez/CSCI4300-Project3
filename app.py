def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    response = " "
    return response.encode()
