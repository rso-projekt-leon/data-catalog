import sys

from flask.cli import FlaskGroup

from app import create_app, db
from app.api.users.models import User


app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(User(username='michael', email="hermanmu@gmail.com", name_surname="Michael Herman"))
    db.session.add(User(username='michaelherman', email="michael@mherman.org", name_surname="Michael Lukaj"))
    db.session.add(User(username='michael2', email="raki@gmail.com", name_surname="Michael Fluko"))
    db.session.add(User(username='juki', email="juki@mherman.org", name_surname="Michael Lukaj"))
    db.session.commit()


if __name__ == '__main__':
    cli()


