import tkinter as tk
from tkinter import ttk


def a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        raise ValueError("El tamaño debe ser un número entero válido.")


class EquipoLlenoError(Exception):
    pass


class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    def __init__(self, nombre, universidad, lenguaje, tamano):
        if not 2 <= tamano <= 3:
            raise ValueError("El equipo debe tener entre 2 y 3 programadores.")
        self.nombre = nombre
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.tamano = tamano
        self.programadores = []

    def esta_completo(self):
        return len(self.programadores) == self.tamano

    @staticmethod
    def validar_texto(valor, campo):
        if valor.strip() == "":
            raise ValueError(f"El {campo} no puede estar vacío.")
        if any(c.isdigit() for c in valor):
            raise ValueError(f"El {campo} no puede tener dígitos.")
        if len(valor) >= 20:
            raise ValueError(f"El {campo} debe tener menos de 20 caracteres.")

    def agregar_programador(self, nombre, apellidos):
        if self.esta_completo():
            raise EquipoLlenoError("El equipo está lleno.")
        self.validar_texto(nombre, "nombre")
        self.validar_texto(apellidos, "apellido")
        self.programadores.append(Programador(nombre, apellidos))

    def resumen(self):
        lineas = [f"Equipo: {self.nombre} | Universidad: {self.universidad} | Lenguaje: {self.lenguaje}",
                  f"Programadores ({len(self.programadores)}/{self.tamano}):"]
        lineas += [f"  - {p.nombre} {p.apellidos}" for p in self.programadores]
        return "\n".join(lineas)


class VentanaEquipo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Equipo de maratón de programación")
        self.equipo = None
        f = ttk.Frame(self, padding=10)
        f.pack()

        self.nom = self.campo(f, "Nombre del equipo:", 0)
        self.uni = self.campo(f, "Universidad:", 1)
        self.leng = self.campo(f, "Lenguaje:", 2)
        self.tam = self.campo(f, "Tamaño (2 o 3):", 3)
        ttk.Button(f, text="Crear equipo", command=self.crear).grid(row=4, column=0, columnspan=2, pady=6)

        self.pn = self.campo(f, "Nombre programador:", 5)
        self.pa = self.campo(f, "Apellidos programador:", 6)
        ttk.Button(f, text="Añadir programador", command=self.anadir).grid(row=7, column=0, columnspan=2, pady=6)

        self.out = tk.Text(f, height=9, width=60, state="disabled")
        self.out.grid(row=8, column=0, columnspan=2, pady=8)

    def campo(self, parent, etiqueta, fila):
        ttk.Label(parent, text=etiqueta).grid(row=fila, column=0, sticky="w", pady=3)
        e = ttk.Entry(parent, width=30)
        e.grid(row=fila, column=1, pady=3, padx=6)
        return e

    def escribir(self, texto):
        self.out.config(state="normal")
        self.out.delete("1.0", "end")
        self.out.insert("end", texto)
        self.out.config(state="disabled")

    def crear(self):
        try:
            self.equipo = EquipoMaratonProgramacion(
                self.nom.get(), self.uni.get(), self.leng.get(), a_entero(self.tam.get()))
            self.escribir("Equipo creado.\n" + self.equipo.resumen())
        except ValueError as e:
            self.escribir(f"Error: {e}")

    def anadir(self):
        if self.equipo is None:
            self.escribir("Primero debe crear el equipo.")
            return
        try:
            self.equipo.agregar_programador(self.pn.get(), self.pa.get())
            self.escribir(self.equipo.resumen())
        except (ValueError, EquipoLlenoError) as e:
            self.escribir(f"Error: {e}\n\n" + self.equipo.resumen())


if __name__ == "__main__":
    VentanaEquipo().mainloop()
