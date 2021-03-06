from flask import Flask, url_for, request
import summarizer, json

app = Flask(__name__,static_url_path='')


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/booger')
def booger():
	return "Booger balls!"

@app.route('/egregious')
def egreg():
	return "Remarkable!"



@app.route('/search/<topic>')
def search(topic):
	data = summarizer.build_idea_tree(topic)
	print(data)
	message = {}
	if data is None:
		message['message'] = 'Topic not found'
	else:
		message['message'] = 'Topic found'
		message['data'] = data
	return json.dumps(message)

@app.route('/explorer')
def explorer():
    return app.send_static_file('pack.html')


@app.route('/hello')
def html():
	return '<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>'

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


'''
with app.test_request_context():
	print(url_for('hello'))
	print(url_for('html'))
	print(url_for('booger', next='/'))
	print(url_for('profile', username='CC'))
'''



if __name__ == "__main__":
#   Uncomment these to run in debug mode
#	app.debug = True
#	app.run()
	app.run(host='0.0.0.0')
