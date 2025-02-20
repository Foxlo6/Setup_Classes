import keyboard
import time
import classes_build_classes as c

language = "php"

c.new_classes()

time.sleep(3)

if language == "php":
    for y in range(len(c.klassen)):
        keyboard.write("class " + c.klassen[y].name + "{" + "\n")
        eig = c.klassen[y].eigen
        eig_nomen = list(eig.keys())

        for el in eig_nomen:
            keyboard.write("\n" + eig[el] + " $" + el + ";\n")

        keyboard.write("\nfunction __construct(")
        for i in range(len(eig_nomen)):
            if i != 0:
                keyboard.write(", ")
            keyboard.write("$v" + str(i))
        keyboard.write("){\n")
        for j in range(len(eig_nomen)):
            keyboard.write("$this->set_" + eig_nomen[j] + "($v" + str(j) + ");\n")
        keyboard.write("}\n")


        keyboard.write("\n\n" + "# Space for custom functions.\n\n\n")

        for el in eig_nomen:
            # get-Methode
            keyboard.write("function get_" + el + "(){" + "\n")
            keyboard.write("return $this->" + el + ";\n")
            keyboard.write("}\n\n")

            # set-Methode
            keyboard.write("function set_" + el + "($var){" + "\n")
            keyboard.write("if (gettype($var) != Null){\n")
            keyboard.write("$this->" + el + " = $var;\n")
            keyboard.write("}\n}\n\n")

        for j in range(3):
            keyboard.send("backspace")
        keyboard.write("}\n\n")
    for i in range(4):
        keyboard.send("backspace")


elif language == "python":
    pass

else:
    exit("Error: Unknown language selected.")