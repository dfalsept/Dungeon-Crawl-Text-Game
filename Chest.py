import random

class Chest:

    puzzles = {
        0: ["What happens once in a minute and twice in a moment?", "m"],
        1: ["I have keys, but can't open doors.", "piano"],
        2: ["The poor have me, the rich need me.", "nothing"],
        3: ["I run around the garden, yet don't move.", "fence"],
        4: ["To keep me, you must give me.", "word"]
    }

    def __init__(self, content):

        self.locked = True
        self.content = content