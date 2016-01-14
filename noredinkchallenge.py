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

### CLASS DEFINITIONS ###


class Quiz(object):

    def __init__(self, children=None):
        self.root = root
        self.children = children or []

class Strand(object):

    def __init__(self, children=None):
        self.children = children or []

class Standard(object):

    def __init__(self, children=None):
        self.children = children or []

class Question(object):

    def __init__(self, children=None):
        self.children = children or []



### PROGRAM FUNCTIONALITY ###

# read file data
for line in open(questions.csv):
    # read data, categorize appropriately, and create instance of correct class
    pass

# determine number of questions
num_questions = int(raw_input("how many questions would you like?"))

# initialize output list
quiz_qs = []

# ask questions for required number of times
while num_questions < 0:
    # determine which question to ask
    # add question_id to output list
    quiz_qs.append(question_id)
    # decrement question variable
    num_questions -= 1

# return output list
return quiz_qs
