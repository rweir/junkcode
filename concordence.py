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
    concordence = collections.defaultdict(Word)
    line_no = 0

    for line in text.splitlines():
        for word in line.split():
            print word
            word = word.lower().strip("(){}[];:\'\",.?!")
            concordence[word].hits += 1
            concordence[word].lines.append(Hit(line_no, line))
    return concordence

def printConcordence(yourtext):
    concordence = process(yourtext)

    for word in sorted(concordence.keys()):
        print "Word:", word
        print "Number of Occurrences: ", concordence[word].hits
        print "Appears on: ", '\n'.join("Line %d: %s" % (hit.line_no, hit.line) for hit in concordence[word].lines)

printConcordence(test)
