# database models for noredink challenge


# importing to use database

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# there's something wrong here. whern I try to seed the database I get
# ImportError: No module named flask_sqlalchemy
# need to find the bug to seed.


#strand_id,strand_name,standard_id,standard_name,question_id,difficulty

class Quiz(db.model):
    """Quiz question categorization"""

    __tablename__ = "quiz_questions"

    quiz_q = db.Column(db.Integer, autoincrement=True, primary_key=True)
    strand_id = db.Column(db.Integer)
    strand_name = db.Column(db.String(25))
    standard_id = db.Column(db.Integer)
    standard_name = db.Column(db.String(25))
    question_id = db.Column(db.Integer)
    difficulty = db.Column(db.Float)


# Helper functions
def connect_to_db(app):
    """Connect database to Flask app."""

    # Configure to use SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from noredinkchallenge.py import app
    connect_to_db(app)
    print "Connected to DB."
