# database models for noredink challenge

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


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
