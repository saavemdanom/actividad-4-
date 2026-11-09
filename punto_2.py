import tkinter as tk
from tkinter import ttk


def a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        raise ValueError("La edad debe ser un número entero válido.")


class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    def imprimir(self):
        return (f"Nombre del vendedor = {self.nombre}\n"
                f"Apellidos del vendedor = {self.apellidos}\n"
                f"Edad del vendedor = {self.edad}")

    def verificar_edad(self, edad):
        if not 0 <= edad <= 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        if edad < 18:  # mayor de edad (18 inclusive). Si el profe pide > 18, cambia a <= 18
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        self.edad = edad


class VentanaVendedor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vendedor")
        f = ttk.Frame(self, padding=10)
        f.pack()

        ttk.Label(f, text="Nombre:").grid(row=0, column=0, sticky="w", pady=3)
        self.nom = ttk.Entry(f, width=30)
        self.nom.grid(row=0, column=1, pady=3, padx=6)

        ttk.Label(f, text="Apellidos:").grid(row=1, column=0, sticky="w", pady=3)
        self.ape = ttk.Entry(f, width=30)
        self.ape.grid(row=1, column=1, pady=3, padx=6)

        ttk.Label(f, text="Edad:").grid(row=2, column=0, sticky="w", pady=3)
        self.edad = ttk.Entry(f, width=30)
        self.edad.grid(row=2, column=1, pady=3, padx=6)

        ttk.Button(f, text="Crear vendedor", command=self.crear).grid(row=3, column=0, columnspan=2, pady=6)

        self.out = tk.Text(f, height=8, width=55, state="disabled")
        self.out.grid(row=4, column=0, columnspan=2, pady=8)

    def escribir(self, texto):
        self.out.config(state="normal")
        self.out.delete("1.0", "end")
        self.out.insert("end", texto)
        self.out.config(state="disabled")

    def crear(self):
        try:
            v = Vendedor(self.nom.get(), self.ape.get())
            v.verificar_edad(a_entero(self.edad.get()))
            self.escribir("Vendedor creado:\n" + v.imprimir())
        except ValueError as e:
            self.escribir(f"Error: {e}")


if __name__ == "__main__":
    VentanaVendedor().mainloop()
