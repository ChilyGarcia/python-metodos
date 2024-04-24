import tkinter as tk
from tkinter import messagebox
from sympy import symbols, Function, Eq, diff, simplify, collect

class EcuacionesDiferencialesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Identificación de Ecuaciones Diferenciales")
        
        self.label_ecuacion = tk.Label(root, text="Ingrese la ecuación diferencial:")
        self.label_ecuacion.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        self.ecuacion_entry = tk.Entry(root, width=50)
        self.ecuacion_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        self.identificar_button = tk.Button(root, text="Identificar", command=self.identificar_ecuacion)
        self.identificar_button.grid(row=1, column=1, padx=10, pady=5, sticky="e")
    
    def identificar_ecuacion(self):
        ecuacion_str = self.ecuacion_entry.get()
        
        if not ecuacion_str:
            messagebox.showerror("Error", "Ingrese una ecuación.")
            return
        
        x = symbols('x')
        y = Function('y')(x)
        
        try:
            ecuacion = Eq(simplify(eval(ecuacion_str)), 0)  # Convertir la entrada en una ecuación
        except:
            messagebox.showerror("Error", "La ecuación ingresada no es válida.")
            return
        
        # Extraer términos de la ecuación
        terminos = ecuacion.lhs.as_ordered_terms()
        
        # Colectar términos en y y sus derivadas
        y_terms = collect(terminos, y)
        
        # Si no hay términos que contengan y o sus derivadas, la ecuación es homogénea
        es_homogenea = y_terms == 0
        
        if es_homogenea:
            messagebox.showinfo("Resultado", "La ecuación es homogénea.")
        else:
            messagebox.showinfo("Resultado", "La ecuación es heterogénea.")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = EcuacionesDiferencialesApp(root)
    root.mainloop()
