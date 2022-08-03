from msilib.schema import ComboBox
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

class menuU:
    def __init__(self):
        self.menu1 = Tk()
        self.menu1.title("PRACTICA 1")
        self.menu1.geometry("500x450")
        
        self.frame = Frame(self.menu1)
        self.frame.configure(bg='aquamarine')
        self.frame.place(x=0, y=0, width=500, height=500)

#TEXTO DEL MENUu
        self.texto1 = Label(self.frame, text="Lab. Lenguajes Formales y de Programacion",bg='aquamarine2',fg = "violetRed4")
        self.texto1.place(x=5, y=20, width=300, height=20)
        self.texto1.configure(font=("Helvetica",10))

        self.texto2 = Label(self.frame, text="Nombre: Genesis Nahomi Aparicio Acan",bg='aquamarine',fg = "violetRed4")
        self.texto2.place(x=5, y=50, width=280, height=20)
        self.texto2.configure(font=("Helvetica",10))

        self.texto3 = Label(self.frame, text="Carne del Estudiante: 202113293",bg='aquamarine',fg = "violetRed4")
        self.texto3.configure(font=("Helvetica",10))
        self.texto3.place(x=5, y=80, width=230, height=20)

#BOTONES
        Button(self.frame, text="Cargar archivo",bg= "bisque3",fg="DeepSkyBlue4", command=self.func1).place(x=195, y=180, width=120, height=30)
        Button(self.frame, text="Gestionar Cursos", bg= "bisque3",fg="DeepSkyBlue4",command=self.func2).place(x=180, y=230, width=150, height=30)
        Button(self.frame, text="conteo de creditos", bg= "bisque3",fg="DeepSkyBlue4",command=self.Conte).place(x=180, y=280, width=150, height=30)
        Button(self.frame, text="salir", bg= "bisque3",fg="DeepSkyBlue4",command=self.menu1.quit).place(x=215, y=325, width=80, height=30)

#FIN MENUU
        self.menu1.mainloop()

#INICIO MENU2   SELECCIONAR ARCHIVO ********************************************************************************************************
    def func1(self):
        
        self.menu2 = Tk()
        self.menu2.title("seleccionar archivo")
        self.menu2.geometry("400x200")
        self.menu2.configure(bg='aquamarine2')

        self.ruta = Label(self.menu2, text="Ruta",bg='aquamarine2',fg = "violetRed4")
        self.ruta.place(x=20, y=40, width=50, height=20)
        self.ruta.configure(font=("Helvetica",11))

        self.rut = Entry(self.menu2)
        self.rut.place(x=80, y=40, width=250, height=20)


        #BOTON SALIR MENU2
        Button(self.menu2, text="regresar",bg= "bisque3",fg="DeepSkyBlue4",command=self.menu2.destroy).place(x=280, y=150, width=100, height=30)

        Button(self.menu2, text="Seleccionar",bg= "bisque3",fg="DeepSkyBlue4").place(x=160, y=80, width=100, height=30)
       
       # self.menu2.mainloop()

       
#INICIO MENU3 SELECIONAR ARCHIVO *********************************************************************************************************
    def func2(self):
        
        self.menu3 = Tk()
        self.menu3.title("seleccionar archivo")
        self.menu3.geometry("400x400")
        self.menu3.configure(bg='aquamarine2')

        Button(self.menu3, text="listar Cursos",bg= "bisque3",fg="DeepSkyBlue4",command=self.LISTAR).place(x=135, y=80, width=120, height=30)
        Button(self.menu3, text="Agregar Cursos", bg= "bisque3",fg="DeepSkyBlue4",command=self.agrgr).place(x=120, y=130, width=150, height=30)
        Button(self.menu3, text="Editar cursos", bg= "bisque3",fg="DeepSkyBlue4",command=self.EDIT).place(x=120, y=175, width=150, height=30)
        Button(self.menu3, text="Eliminar Cursos", bg= "bisque3",fg="DeepSkyBlue4", command=self.ELIMINI).place(x=120, y=225, width=150, height=30)
 
        #BOTON SALIR MENU3
        Button(self.menu3, text="regresar", bg= "bisque3",fg="DeepSkyBlue4",command=self.menu3.destroy).place(x=155, y=275, width=80, height=30)
       

        #self.menu3.mainloop()


    #ELIMINAR CURSO-----------------------------

    def ELIMINI(self):
        
        self.elimi = Tk()
        self.elimi.title("seleccionar archivo")
        self.elimi.geometry("400x200")
        self.elimi.configure(bg='aquamarine2')
        self.menu3.destroy()

        self.cod = Label(self.elimi, text="Codigo de Curso",bg='aquamarine2',fg = "violetRed4")
        self.cod.place(x=10, y=40, width=150, height=20)
        self.cod.configure(font=("Helvetica",11))

        self.rut1 = Entry(self.elimi)
        self.rut1.place(x=150, y=40, width=200, height=20)

        #BOTON SALIR MENU2
        Button(self.elimi, text="regresar",bg= "bisque3",fg="DeepSkyBlue4",command=self.ele).place(x=280, y=150, width=100, height=30)

        Button(self.elimi, text="Seleccionar",bg= "bisque3",fg="DeepSkyBlue4").place(x=160, y=80, width=80, height=30)
         # self.menu2.mainloop()

    #eliminar todo de menu3
    def ele(self):
        self.elimi.destroy()
        self.func2()



    #LISTAR CURSO--------------------------
    def LISTAR(self):
        
        self.listar = Tk()
        self.listar.title("listar Cursos")
        self.listar .geometry("700x500")
        self.listar.configure(bg='aquamarine2')
        self.menu3.destroy()


        Button(self.listar, text="regresar",bg= "bisque3",fg="DeepSkyBlue4",command=self.eles).place(x=550, y=450, width=120, height=30)
       
    def eles(self):
        self.listar.destroy()
        self.func2()


    #AGREGAR CURSOS ------------------

    def agrgr(self):
        
        self.agr= Tk()
        self.agr.title("Agregar Cursos")
        self.agr .geometry("450x450")
        self.agr.configure(bg='aquamarine2')
        self.menu3.destroy()

#-----------------------
        self.cd = Label(self.agr, text="Codigo",bg='aquamarine2',fg = "violetRed4")
        self.cd.place(x=20, y=50, width=50, height=20)
        self.cd.configure(font=("Helvetica",11))

        self.ent1 = Entry(self.agr)
        self.ent1.place(x=140, y=50, width=250, height=20)

#-----------------------
        self.name = Label(self.agr, text="Nombre",bg='aquamarine2',fg = "violetRed4")
        self.name.place(x=20, y=85, width=50, height=20)
        self.name.configure(font=("Helvetica",11))

        self.ent2 = Entry(self.agr)
        self.ent2.place(x=140, y=85, width=250, height=20)

#-----------------------
        self.pre = Label(self.agr, text="Pre Requisito",bg='aquamarine2',fg = "violetRed4")
        self.pre.place(x=20, y=125, width=90, height=20)
        self.pre.configure(font=("Helvetica",11))

        self.ent3 = Entry(self.agr)
        self.ent3.place(x=140, y=125, width=250, height=20)
#-----------------------

        self.opc = Label(self.agr, text="Opcionalidad",bg='aquamarine2',fg = "violetRed4")
        self.opc.place(x=20, y=165, width=90, height=20)
        self.opc.configure(font=("Helvetica",11))

        self.ent4 = Entry(self.agr)
        self.ent4.place(x=140, y=165, width=250, height=20)
#-----------------------

        self.cre = Label(self.agr, text="Creditos        ",bg='aquamarine2',fg = "violetRed4")
        self.cre.place(x=20, y=200, width=90, height=20)
        self.cre.configure(font=("Helvetica",11))

        self.ent5 = Entry(self.agr)
        self.ent5.place(x=140, y=200, width=250, height=20)
#-----------------------          
        self.Esta= Label(self.agr, text="Estado         ",bg='aquamarine2',fg = "violetRed4")
        self.Esta.place(x=20, y=240, width=90, height=20)
        self.Esta.configure(font=("Helvetica",11))

        self.ent6 = Entry(self.agr)
        self.ent6.place(x=140, y=240, width=250, height=20)
        
      #-------------------------------------

        Button(self.agr, text="Agregar",bg= "bisque3",fg="DeepSkyBlue4").place(x=210, y=300, width=80, height=30)
        Button(self.agr, text="regresar",bg= "bisque3",fg="DeepSkyBlue4",command=self.elem).place(x=310, y=400, width=100, height=30)
      
    def elem(self):
        self.agr.destroy()
        self.func2()

#EDITAR

 #EDITAR CURSOS ------------------

    def EDIT(self):
        
        self.edit= Tk()
        self.edit.title("editar")
        self.edit .geometry("450x450")
        self.edit.configure(bg='aquamarine2')
        self.menu3.destroy()

#-----------------------
        self.cd = Label(self.edit, text="Codigo",bg='aquamarine2',fg = "violetRed4")
        self.cd.place(x=20, y=50, width=50, height=20)
        self.cd.configure(font=("Helvetica",11))

        self.ent1 = Entry(self.edit)
        self.ent1.place(x=140, y=50, width=250, height=20)

#-----------------------
        self.name = Label(self.edit, text="Nombre",bg='aquamarine2',fg = "violetRed4")
        self.name.place(x=20, y=85, width=50, height=20)
        self.name.configure(font=("Helvetica",11))

        self.ent2 = Entry(self.edit)
        self.ent2.place(x=140, y=85, width=250, height=20)

#-----------------------
        self.pre = Label(self.edit, text="Pre Requisito",bg='aquamarine2',fg = "violetRed4")
        self.pre.place(x=20, y=125, width=90, height=20)
        self.pre.configure(font=("Helvetica",11))

        self.ent3 = Entry(self.edit)
        self.ent3.place(x=140, y=125, width=250, height=20)
#-----------------------

        self.opc = Label(self.edit, text="Opcionalidad",bg='aquamarine2',fg = "violetRed4")
        self.opc.place(x=20, y=165, width=90, height=20)
        self.opc.configure(font=("Helvetica",11))

        self.ent4 = Entry(self.edit)
        self.ent4.place(x=140, y=165, width=250, height=20)
#-----------------------

        self.cre = Label(self.edit, text="Creditos        ",bg='aquamarine2',fg = "violetRed4")
        self.cre.place(x=20, y=200, width=90, height=20)
        self.cre.configure(font=("Helvetica",11))

        self.ent5 = Entry(self.edit)
        self.ent5.place(x=140, y=200, width=250, height=20)
#-----------------------          
        self.Esta= Label(self.edit, text="Estado         ",bg='aquamarine2',fg = "violetRed4")
        self.Esta.place(x=20, y=240, width=90, height=20)
        self.Esta.configure(font=("Helvetica",11))

        self.ent6 = Entry(self.edit)
        self.ent6.place(x=140, y=240, width=250, height=20)
        
      #-------------------------------------

        Button(self.edit, text="Editar",bg= "bisque3",fg="DeepSkyBlue4").place(x=210, y=300, width=80, height=30)
        Button(self.edit, text="regresar",bg= "bisque3",fg="DeepSkyBlue4",command=self.elemt).place(x=310, y=400, width=100, height=30)
      
    def elemt(self):
        self.edit.destroy()
        self.func2()


#INICIO MENU4*********************************************************************************************************
    def Conte(self):
        
        self.cont = Tk()
        self.cont.title("seleccionar archivo")
        self.cont.geometry("480x400")
        self.cont.configure(bg='aquamarine2')
        

        self.cre = Label(self.cont, text="Creditos Aprobados:",bg='aquamarine2',fg = "violetRed4")
        self.cre.place(x=10, y=40, width=150, height=20)
        self.cre.configure(font=("Helvetica",11))

        self.crec = Label(self.cont, text="Creditos Cursados:",bg='aquamarine2',fg = "violetRed4")
        self.crec.place(x=10, y=70, width=150, height=20)
        self.crec.configure(font=("Helvetica",11))

        self.crep = Label(self.cont, text="Creditos Pendientes:",bg='aquamarine2',fg = "violetRed4")
        self.crep.place(x=10, y=100, width=150, height=20)
        self.crep.configure(font=("Helvetica",11))

        self.creo = Label(self.cont, text="Creditos obligatorios hasta semestre N :",bg='aquamarine2',fg = "violetRed4")
        self.creo.place(x=10, y=130, width=280, height=20)
        self.creo.configure(font=("Helvetica",11))

        self.entt = Text(self.cont)
        self.entt.place(x=290, y=130, width=80, height=20)

        self.sem = Label(self.cont, text="semestre :",bg='aquamarine2',fg = "violetRed4")
        self.sem.place(x=100, y=180, width=150, height=20)
        self.sem.configure(font=("Helvetica",11))

        self.se=Combobox(self.cont)
        self.se.place(x=210, y=180, width=50, height=20)
        
        
        Button(self.cont, text="Contar",bg= "bisque3",fg="DeepSkyBlue4").place(x=280, y=180, width=80, height=20)

        self.cres = Label(self.cont, text="Creditos del semestre :",bg='aquamarine2',fg = "violetRed4")
        self.cres.place(x=10, y=230, width=280, height=20)
        self.cres.configure(font=("Helvetica",11))


        self.sem = Label(self.cont, text="semestre :",bg='aquamarine2',fg = "violetRed4")
        self.sem.place(x=100, y=260, width=150, height=20)
        self.sem.configure(font=("Helvetica",11))

        self.se=Combobox(self.cont)
        self.se.place(x=210, y=260, width=50, height=20)
        
        
        Button(self.cont, text="Contar",bg= "bisque3",fg="DeepSkyBlue4").place(x=280, y=260, width=80, height=20)
        
        Button(self.cont, text="regresar",bg= "bisque3",fg="DeepSkyBlue4",command=self.cont.destroy).place(x=350, y=320, width=90, height=20)









               #self.txt1 = Text(self.agr)
        #self.txt1.place(x=0, y=150, width=200, height=50)

      

        #Entry(self.agr,bg= "bisque3",fg="DeepSkyBlue4").place(x=550, y=450, width=120, height=30)



#FIN DE LA CLASE

menuU()

