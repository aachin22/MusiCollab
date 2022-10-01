from flask import Flask
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def hello_world():
    return 'Hello World'

# main driver function
if __name__ == '__main__':
    app.run()
