import keyboard
import time
#import classes_build_GUI as GUI
import classes_build_classes as c

language = "php"

c.new_classes()

time.sleep(3)

#erstellte_objekte = GUI.objekt_erstellen_gui()

if language == "php":

    for y in range(len(c.klassen)):
        keyboard.write("class " + c.klassen[y].name + "{" + "\n") # Zeilenumbruch?
        eig = c.klassen[y].eigen

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
            keyboard.write("function set_" + el + "($var){" + "\n")
            keyboard.write("if (gettype($var) != Null){\n")
            if eig[el] != "private":
                keyboard.write("this->")
            keyboard.write(el + " = $var;\n")
            keyboard.write("}\n}\n\n")

        for j in range(3):
            keyboard.send("backspace")
        keyboard.write("}\n\n")
    for i in range(4):
        keyboard.send("backspace")


