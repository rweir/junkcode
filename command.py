class App(object):
    def __init__(self):
        self.actions = []
        self.notes = []

class Note(object):
    def __init__(self, title, body):
        self.title = title
        self.body = body
        
class AddNote(object):
    def __init__(self, app, title, body):
        self.app = app
        self.note = Note(title, body)
        
    def do(self):
        self.app.notes.append(self.note)

    def undo(self):
        self.app.notes.pop()

class DelNote(object):
    def __init__(self, app, id):
        self.app = app
        self.id = id

    def do(self):
        self.note = self.app.notes.pop(self.id)

    def undo(self):
        self.app.notes.insert(self.id, self.note)

class EditNote(object):
    def __init__(self, app, id, title, body):
        self.app = app
        self.id = id
        self.title = title
        self.body = body

    def do(self):
        self.original_note = self.app.notes(self.id)
        self.app.notes[self.id] = Note(self.title, self.body)

    def undo(self):
        self.app.notes[self.id] = self.original_note
