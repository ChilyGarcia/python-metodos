import tkinter as tk
from tkinter import ttk
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def es_homogenea(ecuacion):
    x, y = sp.symbols('x y')
    f = sp.sympify(ecuacion)
    try:
        t = sp.symbols('t')
        f_tx_ty = f.subs({x: t*x, y: t*y})
        terminos = f_tx_ty.as_ordered_terms()
        grados = [sp.degree(termino, t) for termino in terminos]
        n = max(grados)
        return all(grado == n for grado in grados)
    except:
        return False


def verificar_ecuacion():
    ecuacion_str = entrada_ecuacion.get()
    try:
        ecuacion = sp.sympify(ecuacion_str)
        if es_homogenea(ecuacion):
            etiqueta_resultado.config(text="La ecuación es homogénea.", foreground="green")
            metodo_selector.pack(fill=tk.X, padx=20, pady=5)
            boton_resolver.pack(fill=tk.X, padx=20, pady=5)
        else:
            etiqueta_resultado.config(text="La ecuación es heterogénea.", foreground="red")
            metodo_selector.pack_forget()
            boton_resolver.pack_forget()
    except sp.SympifyError:
        etiqueta_resultado.config(text="Entrada inválida. Asegúrate de ingresar una ecuación válida.", foreground="red")

def resolver_ecuacion():
    metodo = metodo_seleccionado.get()
    if metodo == "Euler":
        resolver_euler()
    elif metodo == "Runge-Kutta":
        resolver_runge_kutta()
    elif metodo == "Taylor":
        resolver_taylor()

def resolver_euler():
    x, y = sp.symbols('x y')
    ecuacion_str = entrada_ecuacion.get()
    ecuacion = sp.sympify(ecuacion_str)
    f = sp.lambdify((x, y), ecuacion, 'numpy')

    x0, y0 = 1, 1  # Valores iniciales (evitamos x0 = 0 para evitar división por cero)
    h = 0.1  # Paso
    n = 100  # Número de iteraciones

    xs = [x0]
    ys = [y0]

    for i in range(n):
        y0 += h * f(x0, y0)
        x0 += h
        xs.append(x0)
        ys.append(y0)

    fig, ax = plt.subplots()
    ax.plot(xs, ys, label="Euler")
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Método de Euler')

    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()

    etiqueta_info = ttk.Label(ventana, text=f"Ecuación: {ecuacion_str}\nValor inicial: x0 = {xs[0]}, y0 = {ys[0]}\nPaso: h = {h}\nNúmero de iteraciones: {n}\nValor final aproximado: x = {xs[-1]}, y = {ys[-1]}", font=('Berlin Sans FB Demi', 10, 'bold'), anchor="w", justify="left", background=color_pastel)
    etiqueta_info.pack(padx=20, pady=10)

def resolver_runge_kutta():
    x, y = sp.symbols('x y')
    ecuacion_str = entrada_ecuacion.get()
    ecuacion = sp.sympify(ecuacion_str)
    f = sp.lambdify((x, y), ecuacion, 'numpy')

    x0, y0 = 1, 1  # Valores iniciales (evitamos x0 = 0 para evitar división por cero)
    h = 0.1  # Paso
    n = 100  # Número de iteraciones

    xs = [x0]
    ys = [y0]

    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + 0.5*h, y0 + 0.5*k1)
        k3 = h * f(x0 + 0.5*h, y0 + 0.5*k2)
        k4 = h * f(x0 + h, y0 + k3)
        y0 += (k1 + 2*k2 + 2*k3 + k4) / 6
        x0 += h
        xs.append(x0)
        ys.append(y0)

    fig, ax = plt.subplots()
    ax.plot(xs, ys, label="Runge-Kutta")
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Método de Runge-Kutta de Orden 4')

    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()

    etiqueta_info = ttk.Label(ventana, text=f"Ecuación: {ecuacion_str}\nValor inicial: x0 = {xs[0]}, y0 = {ys[0]}\nPaso: h = {h}\nNúmero de iteraciones: {n}\nValor final aproximado: x = {xs[-1]}, y = {ys[-1]}", font=('Berlin Sans FB Demi', 10, 'bold'), anchor="w", justify="left", background=color_pastel)
    etiqueta_info.pack(padx=20, pady=10)

def resolver_taylor():
    x, y = sp.symbols('x y')
    ecuacion_str = entrada_ecuacion.get()
    ecuacion = sp.sympify(ecuacion_str)
    f = sp.lambdify((x, y), ecuacion, 'numpy')

    x0, y0 = 1, 1  # Valores iniciales (evitamos x0 = 0 para evitar división por cero)
    h = 0.1  # Paso
    n = 100  # Número de iteraciones

    xs = [x0]
    ys = [y0]

    for i in range(n):
        # Calcular la aproximación de Taylor de orden 4
        y_siguiente = y0 + h * f(x0, y0) + (h**2/2) * sp.diff(f(x, y), x).subs({x: x0, y: y0}) + (h**3/6) * sp.diff(f(x, y), x, 2).subs({x: x0, y: y0}) + (h**4/24) * sp.diff(f(x, y), x, 3).subs({x: x0, y: y0})
        x0 += h
        y0 = y_siguiente
        xs.append(x0)
        ys.append(y0)

    fig, ax = plt.subplots()
    ax.plot(xs, ys, label="Taylor")
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Método de Taylor de Orden 4')

    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas.draw()
    canvas.get_tk_widget().pack()

    etiqueta_info = ttk.Label(ventana, text=f"Ecuación: {ecuacion_str}\nValor inicial: x0 = {xs[0]}, y0 = {ys[0]}\nPaso: h = {h}\nNúmero de iteraciones: {n}\nValor final aproximado: x = {xs[-1]}, y = {ys[-1]}", font=('Berlin Sans FB Demi', 10, 'bold'), anchor="w", justify="left", background=color_pastel)
    etiqueta_info.pack(padx=20, pady=10)


ventana = tk.Tk()
ventana.title("Ecuaciones diferenciales")
ventana.maxsize(1000, 600)

ventana.iconbitmap("./iconmetods.ico")

color_pastel = "#d8f8e1"
ventana.configure(bg=color_pastel)

ttk.Label(ventana, text="Ingresa la ecuación diferencial en términos de x e y, por ejemplo '(y/x)':", font=('Berlin Sans FB Demi', 10, 'bold'), anchor="center", justify="center", background=color_pastel).pack(padx=20, pady=10)

entrada_ecuacion = ttk.Entry(ventana, width=40, font=('Berlin Sans FB Demi', 10, 'bold'))
entrada_ecuacion.pack(fill=tk.X, padx=20, pady=5)

boton_verificar = ttk.Button(ventana, text="Verificar", command=verificar_ecuacion, style='Bold.TButton')
boton_verificar.pack(fill=tk.X, padx=20, pady=5)

etiqueta_resultado = ttk.Label(ventana, text="", font=('Berlin Sans FB Demi', 10, 'bold'), anchor="center", justify="center", background=color_pastel)
etiqueta_resultado.pack(padx=20, pady=10)

metodo_seleccionado = tk.StringVar()
metodo_selector = ttk.Combobox(ventana, textvariable=metodo_seleccionado, state='readonly', font=('Berlin Sans FB Demi', 10, 'bold'))
metodo_selector['values'] = ["Euler", "Runge-Kutta", "Taylor"]
metodo_selector.pack_forget()

boton_resolver = ttk.Button(ventana, text="Resolver", command=resolver_ecuacion, style='Bold.TButton')
boton_resolver.pack_forget()

s = ttk.Style()
s.configure('TEntry', foreground="gray")
s.configure('Bold.TButton', foreground="black", font=('Berlin Sans FB Demi', 10, 'bold'))

ventana.mainloop()
