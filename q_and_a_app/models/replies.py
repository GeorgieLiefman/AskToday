from main import db


class Reply(db.Model):
        # The tablename attributes species what the name of the table should exist in the database.
        __tablename__ = "replies"

        # These attributes specify what columns the table should have
        reply_id = db.Column(db.Integer, primary_key=True)
        reply_content = db.Column(db.String(2000), nullable=False)



