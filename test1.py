from bottle import route,run

@route('/')
def hello():
    reutrn "Hello World!"

run(host='localhost', port=8080, debug=True)
