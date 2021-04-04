from src.config import app, db, migrate
from src.models import ThirukuralModel

from src.routes.common import common_blueprint
app.register_blueprint(common_blueprint)

if __name__ == '__main__':
    app.run(threaded=True)