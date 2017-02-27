from garbage import Garbage


class PlasticGarbage(Garbage):

    def __init__(self, name, is_clean):
        self.name = name
        self.is_clean = is_clean

    def clean(self):
        if not self.is_clean:
            self.is_clean = True
