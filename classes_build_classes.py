klassen = []

class Klasse:
    def __init__(self, name, eigen, erbtvon=None):
        self.name = name
        self.eigen = eigen
        self.erbtvon = erbtvon
        klassen.append(self)

def new_classes():
    class1 = Klasse("Name1", {"var1":"private", "var2":"protected", "var3":"public"}, None)
    class2 = Klasse("Name2", {"var1":"private", "var2":"protected", "var3":"public"}, None)