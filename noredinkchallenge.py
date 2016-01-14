# write a program to select questions for a quiz. use any libraries you choose.

# * The program should prompt the user for the number of questions to put in
# the quiz. Any integer value greater than 0 is acceptable.
# * The expected output is to display a list of question_ids
# * Use each strand as close as possible to an equal number of times. (e.g.
# There are two strands, so if the user asks for a 3 question quiz, it's okay
# to choose one strand twice and the other once.)
# * Use each standard as close as possible to an equal number of times.
# * Duplicating questions in the quiz is OKAY!
# * Not completing the basic requirements IS NOT FAILURE.  We'd rather see a
# beautiful attempt than a complete attempt.
# * Please use git to track progress. E.g. progressively commit changes so we
# can track your thought process.

# general plan:
# read data from csvs into a data structure. tree makes most sense initially
# ask user for number of questions/ save as variable
# determine which questions to ask (think about how to do this within reqs)
# return list of question_ids (index 4 in line of csv)

# basic structure of data:
# quiz is root of tree, children are strands
# strands are 2nd tier, children are standards
# standards are 3rd tier, children are questions
# questions are 4th tier and are leaves w no children
# each of the above has specific data associated with them
# these are each different, i.e. are required to be instances of different classes
# classes could each be subclasses/inherit from parents or could be separate since different data etc

# we could also do this by building a database of all this info
# and that actually might be a better idea.


# using flask framework for app
# to use flask-sqlalchemy
from flask import Flask

# Import database & classes from model.py
from model import connect_to_db, db, Quiz

# make it a Flask app
app = Flask(__name__)




### CLASS DEFINITIONS ###
# these guys should probably be eliminated if we're going the "build a database" route

class Quiz(object):
    """Quiz class. Root of quiz taxonomy."""

    def __init__(self, children=None):
        if children:
            for child in children:
                assert isinstance(child, Strand)
        self.root = root
        self.children = children or []

class Strand(object):
    """Strand class. Categorizes parts of speech."""

    def __init__(self, children=None):
        if children:
            for child in children:
                assert isinstance(child, Standard)
        self.children = children or []

class Standard(object):
    """Standard class. Categorizes types of strand."""

    def __init__(self, children=None):
        if children:
            for child in children:
                assert isinstance(child, Question)
        self.children = children or []

class Question(object):
    """Question class. Categorizes questions within a standard."""

    def __init__(self, children=None):
        self.children = children or []



### PROGRAM FUNCTIONALITY ###


### line 90-105 is moving into seed.py to seed the database
# # read file data
# line_count = 1
# for line in open("questions.csv"):
#     # skip 1st line content
#     # I know there's a way to use this info to create a data model more efficiently
#     # but I don't know how to do it
#     # googling suggests I use the csv module so I may try that if i have time
#     if line_count == 1:
#         line_count = None
#         continue
    
#     # read data, categorize appropriately, and create instance of correct class
#     line = line.strip().split(",")

#     pass

# determine number of questions
num_questions = int(raw_input("how many questions would you like?"))

# initialize output list
quiz_qs = []

# ask questions for required number of times
while num_questions < 0:
    # determine which question to ask
    # pseudocode: do this with an if/elif/else
    # 


    # add question_id to output list
    quiz_qs.append(question_id)
    # decrement question variable
    num_questions -= 1

# return output list
return quiz_qs
