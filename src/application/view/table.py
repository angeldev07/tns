import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def run(cols):
    selected_item_value = None

    def on_closing():
        """Función que se llama al intentar cerrar la ventana"""
        nonlocal selected_item_value
        if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir?"):
            root.destroy()
            if selected_item_value:
                root.quit()  # Termina el bucle principal
            return selected_item_value

    def on_item_select(event):
        """Función que se llama cuando se selecciona una fila en el Treeview"""
        nonlocal selected_item_value
        selected_item = tree.selection()
        if selected_item:
            item_values = tree.item(selected_item, "values")
            if item_values:
                selected_item_value = item_values
                messagebox.showinfo(
                    "Fila Seleccionada",
                    f"Seleccionaste: ID = {item_values[0]}, Nombre = {item_values[1]}",
                )
                on_closing()

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Lista de Tablas")

    # Crear un marco para el Treeview y las barras de desplazamiento
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Crear el widget Treeview
    tree = ttk.Treeview(frame, columns=("ID", "Nombre"), show="headings")

    # Definir los encabezados de las columnas
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")

    # Definir el ancho de las columnas (opcional)
    tree.column("ID", width=100)
    tree.column("Nombre", width=200)

    # Insertar datos en el Treeview
    for i, row in enumerate(cols):
        tree.insert("", tk.END, values=(i, row))

    # Crear y agregar las barras de desplazamiento
    vsb = tk.Scrollbar(frame, orient="vertical", command=tree.yview)
    hsb = tk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    vsb.pack(side="right", fill="y")
    hsb.pack(side="bottom", fill="x")
    tree.pack(side="left", fill="both", expand=True)

    # Configurar el manejo del evento de cierre de la ventana
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Configurar el manejo de selección de filas
    tree.bind("<<TreeviewSelect>>", on_item_select)

    # Iniciar el bucle de eventos
    root.mainloop()

    # Después de cerrar el mainloop, retornar el valor seleccionado
    return selected_item_value


def run2(cols):
    def on_closing():
        """Función que se llama al intentar cerrar la ventana"""
        if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir?"):
            root.destroy()

    def on_item_select(event):
        """Función que se llama cuando se selecciona una fila en el Treeview"""
        selected_items = tree.selection()
        if selected_items:
            selected_values = []
            for item in selected_items:
                item_values = tree.item(item, "values")
                selected_values.append(item_values)
            # Mostrar los valores de las filas seleccionadas
            messagebox.showinfo(
                "Filas Seleccionadas",
                f"Seleccionaste:\n"
                + "\n".join([f"ID = {v[0]}, Nombre = {v[1]}" for v in selected_values]),
            )

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Lista de Tablas")

    # Crear un marco para el Treeview y las barras de desplazamiento
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Crear el widget Treeview con opción de selección múltiple
    tree = ttk.Treeview(
        frame, columns=("ID", "Nombre"), show="headings", selectmode="extended"
    )

    # Definir los encabezados de las columnas
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")

    # Definir el ancho de las columnas (opcional)
    tree.column("ID", width=100)
    tree.column("Nombre", width=200)

    # Insertar datos en el Treeview
    for i, row in enumerate(cols):
        tree.insert("", tk.END, values=(i, row))

    # Crear y agregar las barras de desplazamiento
    vsb = tk.Scrollbar(frame, orient="vertical", command=tree.yview)
    hsb = tk.Scrollbar(frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    vsb.pack(side="right", fill="y")
    hsb.pack(side="bottom", fill="x")
    tree.pack(side="left", fill="both", expand=True)

    # Configurar el manejo del evento de cierre de la ventana
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Configurar el manejo de selección de filas
    tree.bind("<<TreeviewSelect>>", on_item_select)

    # Iniciar el bucle de eventos
    root.mainloop()
