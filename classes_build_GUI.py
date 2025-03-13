import tkinter as tk
from tkinter import ttk


def eintrags_manager():
    ergebnisse = {}

    def add_haupteintrag():
        """ Fügt einen neuen Haupt-Eintrag hinzu """
        frame = tk.Frame(main_frame, borderwidth=2, relief="solid", padx=5, pady=5)
        frame.pack(fill="x", padx=10, pady=5)
        haupt_frames.append(frame)

        eintrag_name = tk.Entry(frame)
        eintrag_name.pack(side="left")

        remove_button = tk.Button(frame, text="-", command=lambda: remove_haupteintrag(frame, eintrag_name))
        remove_button.pack(side="left")

        untereintrag_frame = tk.Frame(frame)
        untereintrag_frame.pack()

        add_button = tk.Button(frame, text="+ Eigenschaft", command=lambda: add_untereintrag(eintrag_name, untereintrag_frame))
        add_button.pack()

        haupteintraege.append((eintrag_name, []))

    def remove_haupteintrag(frame, entry):
        """ Entfernt einen Haupt-Eintrag """
        index = next((i for i, (e, _) in enumerate(haupteintraege) if e == entry), None)
        if index is not None:
            haupteintraege.pop(index)
            frame.destroy()

    def add_untereintrag(entry_widget, frame):
        """ Fügt einen neuen Untereintrag hinzu (auch bei leeren Hauptnamen) """
        untereintrag_frame = tk.Frame(frame)
        untereintrag_frame.pack()

        untereintrag_name = tk.Entry(untereintrag_frame)
        untereintrag_name.pack(side="left")

        if language_var.get() == "python":
            eigenschaft_var_intern = tk.StringVar(value="python")
        else:
            eigenschaft_var_intern = tk.StringVar(value="protected")
            eigenschaften_dropdown = ttk.Combobox(untereintrag_frame, textvariable=eigenschaft_var_intern, values=["public", "protected", "privat"])
            eigenschaften_dropdown.pack(side="left")

        remove_button = tk.Button(untereintrag_frame, text="-", command=lambda: remove_untereintrag(entry_widget, untereintrag_frame, untereintrag_name))
        remove_button.pack(side="left")

        # Untereintrag zur zugehörigen Hauptliste hinzufügen
        for eintrag, unterlist in haupteintraege:
            if eintrag == entry_widget:
                unterlist.append((untereintrag_name, eigenschaft_var_intern))
                break

    def remove_untereintrag(entry_widget, untereintrag_frame, entry):
        """ Entfernt einen Untereintrag """
        for eintrag, unterlist in haupteintraege:
            if eintrag == entry_widget:
                unterlist[:] = [e for e in unterlist if e[0] != entry]
                break
        untereintrag_frame.destroy()

    def speichern_und_schliessen():
        nonlocal ergebnisse
        """ Speichert die Daten und schließt das Fenster """
        ergebnisse = {
            "Sprache": language_var.get(),
            "Klassen": {}
        }
        for eintrag, unterlist in haupteintraege:
            name = eintrag.get().strip()
            untereintraege = {}
            for e in unterlist:
                if e[0].get().strip():
                    if language_var.get() == "python":
                        untereintraege[e[0].get()] = "python"
                    elif e[1].get() == "python":
                        untereintraege[e[0].get()] = "public"
                    else:
                        untereintraege[e[0].get()]  = e[1].get()
            if name or untereintraege:
                ergebnisse["Klassen"][name if name else "(Unbenannt)"] = untereintraege
        root.quit()

    root = tk.Tk()
    root.title("Eintrags-Manager")

    top_frame = tk.Frame(root)
    top_frame.pack(fill="x", padx=10, pady=5, anchor="w")

    tk.Label(top_frame, text="Sprache:").pack(side="left")
    language_var = tk.StringVar(value="php")
    language_dropdown = ttk.Combobox(top_frame, textvariable=language_var, values=["php", "python"])
    language_dropdown.pack(side="left")

    # Hauptbereich für Einträge
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True, padx=10, pady=5)

    haupt_frames = []
    haupteintraege = []

    add_haupt_button = tk.Button(root, text="+ Neue Klasse", command=add_haupteintrag)
    add_haupt_button.pack()

    label_warn = tk.Label(text="Wenn du auf fertig drückst, beginnt das Prgramm nach 3 s an zu schreiben.\nSei vorsichtig, welche Textzeile du ausgewählt hast!", font=("TkDefaultFont", 7))
    label_warn.pack()

    # "Fertig"-Button ganz unten
    fertig_button = tk.Button(root, text="Fertig", command=speichern_und_schliessen)
    fertig_button.pack(side="bottom", pady=10)

    root.mainloop()
    return ergebnisse

# This code was generated using ChatGPT.