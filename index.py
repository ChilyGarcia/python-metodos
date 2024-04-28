import tkinter as tk
from tkinter import ttk
import sympy as sp

def es_homogenea(ecuacion):

    x, y = sp.symbols('x y')
    ecuacion_expandida = ecuacion.expand()
    terminos = ecuacion_expandida.as_ordered_terms()

    try:
        grado = sp.Poly(terminos[0], x, y).total_degree()

        for termino in terminos[1:]:
            if sp.Poly(termino, x, y).total_degree() != grado:
                return False
    except sp.PolynomialError:
        return False

    return True

def verificar_ecuacion():
    ecuacion_str = entrada_ecuacion.get()
    try:
        ecuacion = sp.sympify(ecuacion_str)
        resultado = "homogénea" if es_homogenea(ecuacion) else "heterogénea"
        etiqueta_resultado.config(text=f"La ecuación es {resultado}.", foreground="green")
    except sp.SympifyError:
        etiqueta_resultado.config(text="Entrada inválida. Asegúrate de ingresar una ecuación válida.", foreground="red")

ventana = tk.Tk()
ventana.title("Ecuaciones diferenciales")
ventana.maxsize(500, 200)  

ventana.iconbitmap("./iconmetods.ico")  

color_pastel = "#d8f8e1" 
ventana.configure(bg=color_pastel)

ttk.Label(ventana, text="Ingresa la ecuación diferencial en términos de x e y, por ejemplo 'y' + x*y':", font=('Berlin Sans FB Demi', 10, 'bold'), anchor="center", justify="center", background=color_pastel).pack(padx=20, pady=10)

entrada_ecuacion = ttk.Entry(ventana, width=40, font=('Berlin Sans FB Demi', 10, 'bold'))
entrada_ecuacion.pack(fill=tk.X, padx=20, pady=5)

boton_verificar = ttk.Button(ventana, text="Verificar", command=verificar_ecuacion, style='Bold.TButton')
boton_verificar.pack(fill=tk.X, padx=20, pady=5)

etiqueta_resultado = ttk.Label(ventana, text="", font=('Berlin Sans FB Demi', 10, 'bold'), anchor="center", justify="center", background=color_pastel)
etiqueta_resultado.pack(padx=20, pady=10)

s = ttk.Style()
s.configure('TEntry', foreground="gray")
s.configure('Bold.TButton', foreground="black", font=('Berlin Sans FB Demi', 10, 'bold'))

ventana.mainloop()
