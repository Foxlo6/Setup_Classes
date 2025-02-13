import keyboard
import time

language = "php"

klassen = []

class Klasse:
    def __init__(self, name, eigen):
        self.name = name
        self.eigen = eigen
        klassen.append(self)


class1 = Klasse("Name1", {"var1":"private", "var2":"protected", "var3":"public"})
class2 = Klasse("Name2", {"var1":"private", "var2":"protected", "var3":"public"})

time.sleep(3)

if language == "php":

    for y in range(len(klassen)):
        keyboard.write("class " + klassen[y].name + "{" + "\n") # Zeilenumbruch?
        eig = klassen[y].eigen

        for el in eig.keys():
            keyboard.write("\n" + eig[el] + " $" + el + ";\n")
        keyboard.write("\n\n" + "# Space for custom functions.\n\n\n")

        for el in eig.keys():
            # get-Methode
            keyboard.write("function get_" + el + "(){" + "\n")
            keyboard.write("return $")
            if eig[el] != "private":
                keyboard.write("this->")
            keyboard.write(el + ";\n")
            keyboard.write("}\n\n")
            # set-Methode
            # TODO: set-Methode

        keyboard.write("}\n\n")
    keyboard.send("backspace")


