from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Document:
    state: str = "<empty>"

    def modify(self, change: str | None):
        print("Document.modify()")
        print("  document state before: ", self.state)
        if change is not None:
            self.state = change
        else:
            self.state = "<empty>"
        print("  document state after:  ", self.state)

    def append(self, text: str, times: int = 1):
        print(f"Document::append({text!r}, {times!r})")
        print("  document state before: ", self.state)
        self.state += text * times
        print("  document state after:  ", self.state)


class Command(ABC):  # noqa: F811
    history = []  # Note this is a class variable!
    redo_stack = []

    def __init__(self, doc: Document):
        self.doc = doc
        self.saved_state = ""

    @abstractmethod
    def do_execute(self): ...

    def execute(self):
        Command.redo_stack.clear()
        self._execute_keeping_redo_stack()

    def _undo_execution(self):
        self.doc.modify(self.saved_state)

    def _execute_keeping_redo_stack(self):
        self.saved_state = self.doc.state
        Command.history.append(self)
        self.do_execute()


def undo():
    if not Command.history:
        return
    last = Command.history.pop()
    Command.redo_stack.append(last)
    last._undo_execution()  # noqa


def redo():
    if not Command.redo_stack:
        return
    last = Command.redo_stack.pop()
    last._execute_keeping_redo_stack()  # noqa
