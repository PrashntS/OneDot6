from bottle import route,run

@route('/')
def main():
    return "Hello World!"

@route('/dev')
def dev():
	return "REST Route."

# We need to implement a POST, GET, DELETE, and PUT request handler.
@route('/dev/connect')
def connect():
	return "Connect Route."

run(host='localhost', port=75, debug=True)