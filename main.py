import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

""" Ventana """

root = ttk.Window()
root.title = "Proyectito"
root.geometry("900x400")

ttk.Label(root, text="Empleado", font=('Sans Serif', 14)).place(x=150, y=5)

ttk.Label(root, text="ID:").place(x=30, y=50)
txtID = ttk.Entry(root, state=READONLY).place(x=110, y=40, width=200)

ttk.Label(root, text="Código").place(x=30, y=90)
txtCodigo = ttk.Entry(root).place(x=110, y=80, width=200)

ttk.Label(root, text="Empleado:").place(x=30, y=130)
txtEmpleado = ttk.Entry(root).place(x=110, y=120, width=200)

ttk.Label(root, text="Puesto:").place(x=30, y=170)
txtPuesto = ttk.Entry(root).place(x=110, y=160, width=200)

ttk.Label(root, text="Departamento:").place(x=30, y=210)
txtDepartamento = ttk.Entry(root).place(x=140, y=200, width=170)

ttk.Label(root, text="Salario:").place(x=30, y=250)
txtSalario = ttk.Entry(root).place(x=110, y=240, width=200)

tree = ttk.Treeview(
    root,
    columns=("id", "codigo", "empleado", "puesto", "departamento", "salario"),
    # displaycolumns="#all",
    height=22,
    selectmode="extended",
    show="headings"    
)
tree.place(x=30, y=280, width=850, height=100)
tree.heading("id", text="ID")
tree.heading("codigo", text="Código")
tree.heading("empleado", text="Empleado")
tree.heading("puesto", text="Puesto")
tree.heading("departamento", text="Departamento")
tree.heading("salario", text="Salario")

tree.column("id", width=30, stretch=False)
tree.column("codigo", width=20)
tree.column("empleado", width=20)
tree.column("puesto", width=20)
tree.column("departamento", width=20)
tree.column("salario", width=20)



root.mainloop()