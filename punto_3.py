import math
import tkinter as tk
from tkinter import ttk


def a_decimal(texto):
    try:
        return float(texto)
    except ValueError:
        raise ValueError("Debe ingresar un número válido.")


class CalculosNumericos:
    @staticmethod
    def logaritmo_neperiano(valor):
        if valor <= 0:
            raise ArithmeticError("El número debe ser positivo.")
        return math.log(valor)

    @staticmethod
    def raiz_cuadrada(valor):
        if valor <= 0:
            raise ArithmeticError("El número debe ser positivo.")
        return math.sqrt(valor)


class VentanaCalculos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cálculos numéricos")
        f = ttk.Frame(self, padding=10)
        f.pack()

        ttk.Label(f, text="Ingrese un valor:").grid(row=0, column=0, sticky="w", pady=3)
        self.valor = ttk.Entry(f, width=30)
        self.valor.grid(row=0, column=1, columnspan=2, pady=3, padx=6)

        ttk.Button(f, text="Logaritmo neperiano",
                   command=lambda: self.calcular(CalculosNumericos.logaritmo_neperiano, "ln")
                   ).grid(row=1, column=1, pady=6)
        ttk.Button(f, text="Raíz cuadrada",
                   command=lambda: self.calcular(CalculosNumericos.raiz_cuadrada, "√")
                   ).grid(row=1, column=2)

        self.out = tk.Text(f, height=6, width=55, state="disabled")
        self.out.grid(row=2, column=0, columnspan=3, pady=8)

    def escribir(self, texto):
        self.out.config(state="normal")
        self.out.delete("1.0", "end")
        self.out.insert("end", texto)
        self.out.config(state="disabled")

    def calcular(self, funcion, simbolo):
        try:
            x = a_decimal(self.valor.get())
            self.escribir(f"{simbolo}({x}) = {funcion(x)}")
        except ArithmeticError as e:
            self.escribir(f"Excepción aritmética: {e}")
        except ValueError as e:
            self.escribir(f"Entrada inválida: {e}")


if __name__ == "__main__":
    VentanaCalculos().mainloop()
