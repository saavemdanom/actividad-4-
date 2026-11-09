import tkinter as tk
from tkinter import ttk


class PruebaExcepciones:
    @staticmethod
    def primer_bloque(num, den):
        r = []
        try:
            r.append("Ingresando al primer try")
            cociente = int(int(num) / int(den))
            r.append(f"Resultado de la división: {cociente}")
            r.append("Después de la división")
        except ValueError:
            r.append("Error: Debe ingresar números enteros válidos.")
        except ZeroDivisionError:
            r.append("División por cero (Capturado)")
        finally:
            r.append("Ingresando al primer finally")
        return r

    @staticmethod
    def segundo_bloque():
        r = []
        try:
            r.append("Ingresando al segundo try")
            objeto = None
            objeto.upper()  # AttributeError (equivale al NullPointerException)
            r.append("Imprimiendo objeto")
        except ZeroDivisionError:
            r.append("División por cero")
        except Exception:
            r.append("Ocurrió una excepción (Capturado)")
        finally:
            r.append("Ingresando al segundo finally")
        return r

    @staticmethod
    def fuera_de_limite():
        try:
            texto = "Programación"
            return f"El carácter es: {texto[14]}"
        except IndexError:
            return "Índice de string por fuera del límite"

    @staticmethod
    def formato_numero():
        r = []
        try:
            numero = int("Número")
            r.append(f"El número es: {numero}")
        except ValueError:
            r.append("Excepción de formato de número (Capturado)")
        finally:
            r.append("Ingresando al finally")
        return "\n".join(r)


class VentanaExcepciones(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Excepciones")
        f = ttk.Frame(self, padding=10)
        f.pack()

        ttk.Label(f, text="Ingrese el numerador:").grid(row=0, column=0, sticky="w", pady=3)
        self.num = ttk.Entry(f, width=30)
        self.num.grid(row=0, column=1, columnspan=2, pady=3, padx=6)

        ttk.Label(f, text="Ingrese el denominador:").grid(row=1, column=0, sticky="w", pady=3)
        self.den = ttk.Entry(f, width=30)
        self.den.grid(row=1, column=1, columnspan=2, pady=3, padx=6)

        ttk.Button(f, text="Prueba Excepciones", command=self.probar).grid(row=2, column=0, pady=6)
        ttk.Button(f, text="Probar límite de string",
                   command=lambda: self.escribir(PruebaExcepciones.fuera_de_limite())).grid(row=2, column=1)
        ttk.Button(f, text="Probar formato número",
                   command=lambda: self.escribir(PruebaExcepciones.formato_numero())).grid(row=2, column=2)

        self.out = tk.Text(f, height=11, width=62, state="disabled")
        self.out.grid(row=3, column=0, columnspan=3, pady=8)

    def escribir(self, texto):
        self.out.config(state="normal")
        self.out.delete("1.0", "end")
        self.out.insert("end", texto)
        self.out.config(state="disabled")

    def probar(self):
        lineas = (PruebaExcepciones.primer_bloque(self.num.get(), self.den.get())
                  + [""] + PruebaExcepciones.segundo_bloque())
        self.escribir("\n".join(lineas))


if __name__ == "__main__":
    VentanaExcepciones().mainloop()
