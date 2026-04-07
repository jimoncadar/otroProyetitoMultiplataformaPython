import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from conexion import MiConexion
import mysql.connector
from tkinter import messagebox


""" Ventana """
root = ttk.Window()
root.title = "Proyectito"
root.geometry("900x500")

ttk.Label(root, text="Empleado", font=('Sans Serif', 14)).place(x=150, y=5)

ttk.Label(root, text="ID:").place(x=30, y=50)
txtID = ttk.Entry(root)
txtID.place(x=110, y=40, width=200)

ttk.Label(root, text="Código").place(x=30, y=90)
txtCodigo = ttk.Entry(root)
txtCodigo.place(x=110, y=80, width=200)

ttk.Label(root, text="Empleado:").place(x=30, y=130)
txtEmpleado = ttk.Entry(root)
txtEmpleado.place(x=110, y=120, width=200)

ttk.Label(root, text="Puesto:").place(x=30, y=170)
txtPuesto = ttk.Entry(root)
txtPuesto.place(x=110, y=160, width=200)

ttk.Label(root, text="Departamento:").place(x=30, y=210)
txtDepartamento = ttk.Entry(root)
txtDepartamento.place(x=140, y=200, width=170)

ttk.Label(root, text="Salario:").place(x=30, y=250)
txtSalario = ttk.Entry(root)
txtSalario.place(x=110, y=240, width=200)

tree = ttk.Treeview(
    root,
    columns=("id", "codigo", "empleado", "puesto", "departamento", "salario"),
    # displaycolumns="#all",
    height=22,
    selectmode="extended",
    show="headings",        
)
tree.place(x=30, y=280, width=850, height=200)
tree.heading("id", text="ID")
tree.heading("codigo", text="Código")
tree.heading("empleado", text="Empleado")
tree.heading("puesto", text="Puesto")
tree.heading("departamento", text="Departamento")
tree.heading("salario", text="Salario")

tree.column("id", width=30, stretch=False, anchor="center")
tree.column("codigo", width=20, anchor="center")
tree.column("empleado", width=20, anchor="center")
tree.column("puesto", width=20, anchor="center")
tree.column("departamento", width=20, anchor="center")
tree.column("salario", width=20, anchor="center")

scroll_y = ttk.Scrollbar(tree, orient="vertical")
scroll_y.pack(side="right", fill="y")


btnModificar = ttk.Button(root, text="Modificar", bootstyle="warning")
btnModificar.place(x=560, y=40, width=150, height=90)

btnEliminar = ttk.Button(root, text="Eliminar", bootstyle="danger")
btnEliminar.place(x=720, y=40, width=150, height=90)

def mostrarDatos():
    for filas in tree.get_children():
        tree.delete(filas)

    try:
        conn = MiConexion()        
        cursor = conn.cursor()
        sql = "select * from empleados"
        cursor.execute(sql, conn)
        datos = cursor.fetchall()

        for dato in datos:
            tree.insert("", tk.END, values=dato)
                    
    except mysql.connector.Error as e:
        messagebox.showerror(f"Error:{e}")


mostrarDatos()    


def insertarDatos():
    codigo = txtCodigo.get()
    empleado = txtEmpleado.get()
    puesto = txtPuesto.get()
    departamento = txtDepartamento.get()
    salario = txtSalario.get()

    if codigo == "" or empleado == "" or puesto == "" or departamento == "" or salario == "":
        messagebox.showwarning("Aviso", "Ingresar todos los datos del formulario.")
        return
    
    try:
        con = MiConexion()
        cursor = con.cursor()
        sql_insertar = "insert into empleados(codigo, nombre, puesto, departamento, salario) values(%s,%s,%s,%s,%s)"
        valores = (codigo, empleado, puesto, departamento, salario)

        cursor.execute(sql_insertar, valores)
        con.commit()
        con.close()

        mostrarDatos() 
        limpiarCampos()   
        messagebox.showinfo("Registro", "Registro éxitoso.")

    except Exception as e:
        messagebox.showerror("Error", f"Problemas:{e}")

btnInsertar = ttk.Button(root, text="Insertar", command=insertarDatos)
btnInsertar.place(x=400, y=40, width=150, height=90)

def limpiarCampos():
    txtID.delete(0, tk.END)
    txtCodigo.delete(0, tk.END)
    txtDepartamento.delete(0, tk.END)
    txtEmpleado.delete(0, tk.END)
    txtPuesto.delete(0, tk.END)
    txtSalario.delete(0, tk.END)  
    
btnLimpiar = ttk.Button(root, text="Limpiar", command=limpiarCampos)
btnLimpiar.place(x=400, y=150, width=150, height=90)


def seleccionar(event):
    item = tree.focus()
    if item:
        datos = tree.item(item, "values")

        txtID.delete(0, tk.END)
        txtID.insert(0, datos[0])

        txtCodigo.delete(0, tk.END)
        txtCodigo.insert(0, datos[1])

        txtEmpleado.delete(0, tk.END)
        txtEmpleado.insert(0, datos[2])

        txtPuesto.delete(0, tk.END)
        txtPuesto.insert(0, datos[3])
        
        txtDepartamento.delete(0, tk.END)
        txtDepartamento.insert(0, datos[4])
        
        txtSalario.delete(0, tk.END)
        txtSalario.insert(0, datos[5])



tree.bind("<Button-1>", seleccionar)

root.mainloop()