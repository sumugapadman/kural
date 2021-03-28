from flask import Flask, request

app = Flask(__name__,template_folder='src/views')

from src.routes.common import common_blueprint
app.register_blueprint(common_blueprint)

if __name__ == '__main__':
    app.run(threaded=True)