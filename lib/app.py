from bottle import route,run,request,template

@route('/')
def main():
    return "Hello World!"

@route('/dev')
def dev():
	return "REST Route."

# We need to implement a POST, GET, DELETE, and PUT request handler.
@route('/dev/connect')
def connect():
	 return '''
         <form action="/dev/connect" method="post">
            Enter your key : <input name="hashkey" type="text" placeholder="Enter your Hash Key" />
            <input value="Hash It !" type="submit" />
        </form>
         '''  
     
@route('/dev/connect', method='POST')
def connect():
     hashkey = request.forms.get('hashkey')
     return template("Your Key is {{hk}}",hk=hashkey)   

# @delete('/dev/connect')
# @put('/dev/connect')

# We need a config file.

run(host='localhost', port=1600, debug=True) # Running on port 1600 to make it easier, plus it matches with Project name
