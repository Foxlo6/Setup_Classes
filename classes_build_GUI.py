import tkinter as tk
import classes_build_classes as c


def objekt_erstellen_gui():
    anzahl = int
    def generiere_felder():
        for widget in frame.winfo_children():
            widget.destroy()

        try:
            nonlocal anzahl
            anzahl = int(entry_anzahl.get())
        except ValueError:
            label_info.config(text="Bitte eine gültige Zahl eingeben!", fg="red")
            return

        label_info.config(text="Gib die Namen der Objekte ein:", fg="black")

        for i in range(anzahl):
            tk.Label(frame, text=f"Objekt {i + 1}:").grid(row=i, column=0)
            eingabe = tk.Entry(frame)
            eingabe.grid(row=i, column=1)
            eingaben.append(eingabe)

        tk.Button(frame, text="Erstellen", command=instanzen_erstellen).grid(row=anzahl, columnspan=2)

    def instanzen_erstellen():
        for i in range(anzahl):
            exec(str("class"+str(i)+" = c.Klasse("+ str(eingaben[i].get().strip())+", {})"))
        print("Erstellte Objekte:", c.klassen)
        root.quit()

    root = tk.Tk()
    root.title("Objekte erstellen")

    tk.Label(root, text="Anzahl der Objekte:").pack()
    entry_anzahl = tk.Entry(root)
    entry_anzahl.pack()
    tk.Button(root, text="Weiter", command=generiere_felder).pack()

    label_info = tk.Label(root, text="")
    label_info.pack()

    frame = tk.Frame(root)
    frame.pack()

    eingaben = []

    root.mainloop()


def what_classes():
    # Hauptaufruf der GUI
    objekt_erstellen_gui()
    print("Liste der Instanzen nach GUI:", c.klassen)

what_classes()
