import tkinter as tk
from tkinter import ttk, filedialog


class LeerArchivo:
    @staticmethod
    def leer(ruta):
        with open(ruta, encoding="utf-8") as archivo:
            return archivo.read()


class VentanaLeerArchivo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lectura de archivos")
        f = ttk.Frame(self, padding=10)
        f.pack()

        ttk.Button(f, text="Elegir archivo .txt", command=self.abrir).pack(pady=6)

        self.out = tk.Text(f, height=15, width=70, state="disabled")
        self.out.pack(pady=8)

    def escribir(self, texto):
        self.out.config(state="normal")
        self.out.delete("1.0", "end")
        self.out.insert("end", texto)
        self.out.config(state="disabled")

    def abrir(self):
        ruta = filedialog.askopenfilename(filetypes=[("Texto", "*.txt")])
        if not ruta:
            return
        try:
            self.escribir(LeerArchivo.leer(ruta))
        except (OSError, UnicodeDecodeError):
            self.escribir("No se pudo leer el archivo.")


if __name__ == "__main__":
    VentanaLeerArchivo().mainloop()
