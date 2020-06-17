"""app/manage.py
"""
from flask_script import Manager

from apis.models import db
from run import app

manager = Manager(app)


@manager.command
def migrate():
    """migrate
    """
    db.create_all()


if __name__ == '__main__':
    manager.run()
