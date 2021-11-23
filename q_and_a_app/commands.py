import faker
from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("create")
def create_db():
    """Creates tables in the database based on the models."""
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("drop")
def drop_db():
    """Drops all tables in the database."""
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted!")

@db_commands.cli.command("seed")
def seed_db():
    from models.posts import Post
    from faker import Faker
    faker = Faker()

    for i in range(20):
        post = Post(faker.catch_phrase())
        db.session.add(post)

    db.session.commit()
    print("Tables seeded!")

@db_commands.cli.command("reset")
def reset_db():
    """Drops, creates and seeds tables in one step."""
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted!")
    
    db.create_all()
    print("Tables created!")

    from models.posts import Post
    from faker import Faker
    faker = Faker()

    for i in range(20):
        post = Post(faker.catch_phrase())
        db.session.add(post)

    db.session.commit()
    