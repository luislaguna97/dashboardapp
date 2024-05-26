# clientes_gui.py
import tkinter as tk
from db_connection import DBConnection

class ClientesGUI:
    def __init__(self, root):
        self.db = DBConnection()
        self.root = root
        self.root.title("Gestión de Clientes")
        self.create_widgets()
        self.populate_list()

    def create_widgets(self):
        self.id_label = tk.Label(self.root, text="ID Cliente")
        self.id_label.grid(row=0, column=0)
        self.id_entry = tk.Entry(self.root)
        self.id_entry.grid(row=0, column=1)

        self.name_label = tk.Label(self.root, text="Nombre Cliente")
        self.name_label.grid(row=1, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=1, column=1)

        self.address_label = tk.Label(self.root, text="Dirección")
        self.address_label.grid(row=2, column=0)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=2, column=1)

        self.contact_label = tk.Label(self.root, text="Información de Contacto")
        self.contact_label.grid(row=3, column=0)
        self.contact_entry = tk.Entry(self.root)
        self.contact_entry.grid(row=3, column=1)

        self.insert_button = tk.Button(self.root, text="Insertar", command=self.insert_record)
        self.insert_button.grid(row=4, column=0)

        self.update_button = tk.Button(self.root, text="Actualizar", command=self.update_record)
        self.update_button.grid(row=4, column=1)

        self.delete_button = tk.Button(self.root, text="Eliminar", command=self.delete_record)
        self.delete_button.grid(row=4, column=2)

        self.query_button = tk.Button(self.root, text="Consultar", command=self.query_records)
        self.query_button.grid(row=4, column=3)

        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.grid(row=5, column=0, columnspan=4)
        self.listbox.bind('<<ListboxSelect>>', self.load_record)

    def insert_record(self):
        query = "INSERT INTO clientes (ID_Cliente, Nombre_Cliente, Direccion, Informacion_Contacto) VALUES (%s, %s, %s, %s)"
        params = (
            self.id_entry.get(),
            self.name_entry.get(),
            self.address_entry.get(),
            self.contact_entry.get()
        )
        self.db.execute_query(query, params)
        self.populate_list()

    def update_record(self):
        query = "UPDATE clientes SET Nombre_Cliente=%s, Direccion=%s, Informacion_Contacto=%s WHERE ID_Cliente=%s"
        params = (
            self.name_entry.get(),
            self.address_entry.get(),
            self.contact_entry.get(),
            self.id_entry.get()
        )
        self.db.execute_query(query, params)
        self.populate_list()

    def delete_record(self):
        query = "DELETE FROM clientes WHERE ID_Cliente=%s"
        params = (self.id_entry.get(),)
        self.db.execute_query(query, params)
        self.populate_list()

    def query_records(self):
        self.populate_list()

    def populate_list(self):
        self.listbox.delete(0, tk.END)
        query = "SELECT * FROM clientes"
        records = self.db.fetch_query(query)
        for row in records:
            self.listbox.insert(tk.END, row)

    def load_record(self, event):
        selected_record = self.listbox.get(self.listbox.curselection())
        self.id_entry.delete(0, tk.END)
        self.id_entry.insert(tk.END, selected_record[0])
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(tk.END, selected_record[1])
        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(tk.END, selected_record[2])
        self.contact_entry.delete(0, tk.END)
        self.contact_entry.insert(tk.END, selected_record[3])

if __name__ == "__main__":
    root = tk.Tk()
    app = ClientesGUI(root)
    root.mainloop()
