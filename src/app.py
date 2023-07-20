import os
from flask import Flask
from flask_cors import CORS

from todos.routes import todo
app = Flask(__name__)


app.register_blueprint(todo, url_prefix='/todos')
# app.register_blueprint(contacts, url_prefix='/contacts')

CORS(app)

@app.route('/')
def index():
    return 'Hello World! hola'


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3001))
    app.run(host='0.0.0.0', port=PORT, debug=True)