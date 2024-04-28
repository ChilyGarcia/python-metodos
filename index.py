import tkinter as tk
from tkinter import ttk
import sympy as sp

def es_homogenea(ecuacion):
    # Creamos los símbolos necesarios
    x, y = sp.symbols('x y')

    # Expandimos y simplificamos la ecuación
    ecuacion_expandida = ecuacion.expand()

    # Obtenemos los términos de la ecuación
    terminos = ecuacion_expandida.as_ordered_terms()

    # Verificamos si todos los términos tienen el mismo grado
    try:
        # Obtenemos el grado del primer término
        grado = sp.Poly(terminos[0], x, y).total_degree()

        for termino in terminos[1:]:
            if sp.Poly(termino, x, y).total_degree() != grado:
                return False
    except sp.PolynomialError:
        # Si hay un error al obtener el grado, la ecuación no es homogénea
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

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ecuaciones diferenciales")
ventana.maxsize(500, 200)  # Ancho máximo: 500px, Alto máximo: 200px

# Establecer el icono de la ventana
ventana.iconbitmap("./iconmetods.ico")  # Reemplaza "ruta_del_archivo.ico" con la ruta de tu archivo de icono

# Establecer color de fondo
color_pastel = "#F0E8D9"  # Color pastel clarito
ventana.configure(bg=color_pastel)

# Etiqueta de instrucciones
ttk.Label(ventana, text="Ingresa la ecuación diferencial en términos de x e y, por ejemplo 'y' + x*y':", font=('Berlin Sans FB Demi', 10, 'bold'), anchor="center", justify="center", background=color_pastel).pack(padx=20, pady=10)

# Entrada para la ecuación
entrada_ecuacion = ttk.Entry(ventana, width=40, font=('Berlin Sans FB Demi', 10, 'bold'))
entrada_ecuacion.pack(fill=tk.X, padx=20, pady=5)

# Botón para verificar
boton_verificar = ttk.Button(ventana, text="Verificar", command=verificar_ecuacion, style='Bold.TButton')
boton_verificar.pack(fill=tk.X, padx=20, pady=5)

# Etiqueta para mostrar el resultado
etiqueta_resultado = ttk.Label(ventana, text="", font=('Berlin Sans FB Demi', 10, 'bold'), anchor="center", justify="center", background=color_pastel)
etiqueta_resultado.pack(padx=20, pady=10)

# Personalizar estilos de la entrada y el botón
s = ttk.Style()
s.configure('TEntry', foreground="gray")
s.configure('Bold.TButton', foreground="black", font=('Berlin Sans FB Demi', 10, 'bold'))

# Iniciar el bucle de eventos
ventana.mainloop()
