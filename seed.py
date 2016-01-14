# seed database from csv files for noredink challenge

"""
seeding data from questions.csv

[0]strand_id
[1]strand_name
[2]standard_id
[3]standard_name
[4]question_id
[5]difficulty

"""

# import models from model.py
from model import connect_to_db, db, Quiz
from server import app


def load_quiz_data():
    """Load quiz question data to db from questions.csv"""

    # marker for first line
    line_count = 1

    # read lines from file and write to db
    for line in open("questions.csv"):

        # skip line 1
        if line_count == 1:
            line_count = None
            continue

        # actually read in data from non-header lines
        line = line.strip().split(",")

        strand_id = line[0]
        strand_name = line[1]
        standard_id = line[2]
        standard_name = line[3]
        question_id = line[4]
        difficulty = line[5]

        # assign data to appropriate db field

        quiz_data = Quiz(strand_id=strand_id,
                         strand_name=strand_name,
                         standard_id=standard_id,
                         standard_name=standard_name,
                         question_id=question_id,
                         difficulty=difficulty)

        db.session.add(quiz_data)

        # visual of progress
        print quiz_data

    # commit all new adds to db
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # create all tables
    db.create_all()

    # import quiz data into database
    load_quiz_data()

    # confirmation
    print "It's done!"
