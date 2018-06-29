
from flask_script import Manager

from utils.functions import create_app

app = create_app()
manage = Manager(app=app)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    manage.run()
