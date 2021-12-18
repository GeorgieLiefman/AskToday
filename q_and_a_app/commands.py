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
    from schemas.post_schema import posts_schema
    from models.comments import Comment
    from schemas.comment_schema import comments_schema
    from models.users import User
    from schemas.user_schema import users_schema
    

    post = Post.query.all()
    post_information = posts_schema.dump(post)
    post_data = str(post_information)

    user = User.query.all()
    user_information = users_schema.dump(user)
    user_data = str(user_information)

    comment = Post.query.all()
    comment_information = comments_schema.dump(comment)
    comment_data = str(comment_information)
    
    

    # Use schemas to convert to dictionary which can be written to txt file
    # Use string command to turn dictionary to txt and write that text to a file

    

    text_file = open("data.txt", "w")
    text_file.write(post_data)
    text_file.write(user_data)
    text_file.write(comment_data)
    text_file.close()

    #flask db-custom export
    