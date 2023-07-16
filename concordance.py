"Quick example of generating a concordance - an alphabetical list of the words in a text"

import collections

test = """once upon a time
there was a time
once
"""


class Word(object):
    def __init__(self):
        self.hits = 0
        self.lines = []


class Hit(object):
    def __init__(self, line_no, line):
        self.line_no = line_no
        self.line = line


def process(text):
    concordance = collections.defaultdict(Word)
    line_no = 0

    for line in text.splitlines():
        for word in line.split():
            word = word.lower().strip("(){}[];:'\",.?!")
            concordance[word].hits += 1
            concordance[word].lines.append(Hit(line_no, line))
    return concordance


def printConcordance(yourtext):
    concordance = process(yourtext)

    for word in sorted(concordance.keys()):
        print("Word:", word)
        print("Number of Occurrences: ", concordance[word].hits)
        print(
            "Appears on: \n",
            " \n ".join(
                "Line %d: %s" % (hit.line_no, hit.line)
                for hit in concordance[word].lines
            ),
        )
        print()


printConcordance(test)
