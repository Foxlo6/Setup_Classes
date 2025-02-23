klassen = []


class Klasse:
    def __init__(self, name, eigen, erbtvon=None):
        self.name = name
        self.eigen = eigen
        self.erbtvon = erbtvon
        klassen.append(self)


def data_checknuse(tmp_dic_class):
    if tmp_dic_class == {}:
        exit(0)
    elif type(tmp_dic_class) != dict:
        exit("Wrong datatype in line 15.")
    else:
        for name in tmp_dic_class:
            Klasse(name, tmp_dic_class[name])

def new_classes():
    class1 = Klasse("Name1", {"var1":"public", "var2":"protected", "var3":"private"}, None)
    class2 = Klasse("Name2", {"var1":"public", "var2":"protected", "var3":"private"}, None)

