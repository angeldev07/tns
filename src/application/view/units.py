import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import ttk


class UnitsView:

    def __init__(self, cols):
        # Configuración de la ventana
        self.root = tk.Tk()
        self.root.title("Reportar unidades")  # Título de la ventana
        self.root.geometry("600x300")  # Tamaño inicial de la ventana

        self.conf_table(cols)
        self.root.mainloop()

    def get_cols_name(self, value):
        return tuple(list(value.to_json().keys()))

    def conf_table(self, cols_name):
        # Crear un marco para el Treeview y las barras de desplazamiento
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Crear el widget Treeview con opción de selección múltiple
        tree = ttk.Treeview(
            frame,
            columns=self.get_cols_name(cols_name[0]),
            show="headings",
            selectmode="extended",
        )

        # Definir los encabezados de las columnas
        for col in self.get_cols_name(cols_name[0]):
            tree.heading(col, text=col.upper())
            tree.column(col, width=200)

        for value in cols_name:
            tree.insert("", tk.END, values=tuple(value.to_json().values()))

        # Crear y agregar las barras de desplazamiento
        vsb = tk.Scrollbar(frame, orient="vertical", command=tree.yview)
        hsb = tk.Scrollbar(frame, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        tree.pack(side="left", fill="both", expand=True)

    def cerrar_ventana(self):
        # Confirmar si el usuario realmente quiere cerrar la ventana
        if messagebox.askokcancel("Cerrar", "¿Realmente quieres salir?"):
            self.root.destroy()  # Cerrar la ventana
