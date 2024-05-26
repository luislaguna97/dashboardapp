# main_gui.py
import tkinter as tk
from almacenes_gui import AlmacenesGUI
from clientes_gui import ClientesGUI
# from libreta_gui import LibretaGUI
# from productos_lacteos_gui import ProductosLacteosGUI
# from movimientos_inventarios_gui import MovimientosInventariosGUI
# from pedidos_gui import PedidosGUI

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vitamilk DB Management")
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self.root, text="Almacenes", command=self.open_almacenes).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Clientes", command=self.open_clientes).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Libreta", command=self.open_libreta).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Productos Lácteos", command=self.open_productos_lacteos).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Movimientos de Inventarios", command=self.open_movimientos_inventarios).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Pedidos", command=self.open_pedidos).grid(row=2, column=1, padx=10, pady=10)

    def open_almacenes(self):
        new_window = tk.Toplevel(self.root)
        AlmacenesGUI(new_window)

    def open_clientes(self):
        new_window = tk.Toplevel(self.root)
        ClientesGUI(new_window)

    def open_libreta(self):
        new_window = tk.Toplevel(self.root)
        LibretaGUI(new_window)

    def open_productos_lacteos(self):
        new_window = tk.Toplevel(self.root)
        ProductosLacteosGUI(new_window)

    def open_movimientos_inventarios(self):
        new_window = tk.Toplevel(self.root)
        MovimientosInventariosGUI(new_window)

    def open_pedidos(self):
        new_window = tk.Toplevel(self.root)
        PedidosGUI(new_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainGUI(root)
    root.mainloop()


