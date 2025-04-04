# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# QuizManager manages the quiz content
import os.path
import os
import quizparser
import datetime


class QuizManager:
    def __init__(self, quizfolder):
        self.quizfolder = quizfolder
        #TODO: the most recently selected quiz
        self.the_quiz = None

        #TODO: initialize the collection of quizzes
        self.quizzes = dict()
        #TODO: stores the results of the most recent quiz
        self.results = None

        #TODO: the name of the person taking the quiz
        self.quiztaker =""

        #TODO: make sure that the quiz folder exists
        if (os.path.exists(quizfolder) == False):
            raise FileNotFoundError("The quiz folder does not seem to exist")

        #TODO: build the list of quizzes
        self._build_quiz_list()

    def _build_quiz_list(self):
        dircontents = os.scandir(self.quizfolder)
        #TODO: parse the XML files in the directory
        for i, f in enumerate(dircontents):
            if f.is_file():
                parser = quizparser.QuizParser()
                self.quizzes[i+1] = parser.parse_quiz(f)

    #TODO: print a list of the currently installed quizzes
    def list_quizzes(self):
        for k,v in self.quizzes.items():
            print(f"({k}): {v.name}")

    # start the given quiz for the user and return the results
    def take_quiz(self, quizid, username):
        pass

    # prints the results of the most recently taken quiz
    def print_results(self):
        pass

    # save the results of the most recent quiz to a file
    # the file is named using the current date as
    # QuizResults_YYYY_MM_DD_N (N is incremented until unique)
    def save_results(self):
        pass


if __name__ == "__main__":
    qm = QuizManager("Quizzes")
    qm.list_quizzes()
