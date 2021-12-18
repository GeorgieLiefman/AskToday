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
    from models.comments import Comment
    from models.users import User
    from faker import Faker
    faker = Faker()

    for i in range(20):
        post = Post(faker.catch_phrase())
        db.session.add(post)

    for i in range(20):
        user = User(faker.catch_phrase())
        db.session.add(user)

    for i in range(20):
        comment = Comment(faker.catch_phrase())
        db.session.add(comment)

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




@db_commands.cli.command("export")
def export_data():
    """Outputs all of the data in the database to a .txt file."""
    from models.posts import Post
    from models.comments import Comment
    from models.users import User

    post_list = Post.query.all()
    comment_list = Comment.query.all()
    user_list = User.query.all()


    # Use schemas to convert to dictionary which can be written to txt file
    # Use string command to turn dictionary to txt and write that text to a file
    