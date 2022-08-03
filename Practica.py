from tkinter import *
from tkinter import messagebox

class menuU:
    def __init__(self):
        self.menu1 = Tk()
        self.menu1.title("PRACTICA 1")
        self.menu1.geometry("500x500")
        
        self.frame = Frame(self.menu1)
        self.frame.configure(bg='aquamarine2')
        self.frame.place(x=0, y=0, width=500, height=500)

#TEXTO DEL MENUu
        self.texto1 = Label(self.frame, text="Lab. Lenguajes Formales y de Programacion",bg='aquamarine2',fg = "violetRed4")
        self.texto1.place(x=5, y=20, width=300, height=20)
        self.texto1.configure(font=("Helvetica",10))

        self.texto2 = Label(self.frame, text="Nombre: Genesis Nahomi Aparicio Acan",bg='aquamarine2',fg = "violetRed4")
        self.texto2.place(x=5, y=50, width=280, height=20)
        self.texto2.configure(font=("Helvetica",10))

        self.texto3 = Label(self.frame, text="Carne del Estudiante: 202113293",bg='aquamarine2',fg = "violetRed4")
        self.texto3.configure(font=("Helvetica",10))
        self.texto3.place(x=5, y=80, width=230, height=20)

#BOTONES
        Button(self.frame, text="Cargar archivo",bg= "bisque3",fg="DeepSkyBlue4", command=self.func1).place(x=195, y=180, width=120, height=30)
        Button(self.frame, text="Gestionar Cursos", bg= "bisque3",fg="DeepSkyBlue4",command=self.func2).place(x=180, y=230, width=150, height=30)
        Button(self.frame, text="conteo de creditos", bg= "bisque3",fg="DeepSkyBlue4").place(x=180, y=280, width=150, height=30)
        Button(self.frame, text="salir", bg= "bisque3",fg="DeepSkyBlue4",command=self.menu1.quit).place(x=215, y=325, width=80, height=30)

#FIN MENUU
        self.menu1.mainloop()

#INICIO MENU2--------------------------------------------------------------------------------------------------------------------------------
    def func1(self):
        
        self.menu2 = Tk()
        self.menu2.title("seleccionar archivo")
        self.menu2.geometry("400x200")
        self.menu2.configure(bg='aquamarine2')


#BOTON SALIR MENU2
        Button(self.menu2, text="regresar",bg= "bisque3",fg="DeepSkyBlue4",command=self.menu2.destroy).place(x=250, y=110, width=120, height=30)
       
       # self.menu2.mainloop()

       
#INICIO MENU3--------------------------------------------------------------------------------------------------------------------------------
    def func2(self):
        
        self.menu3 = Tk()
        self.menu3.title("seleccionar archivo")
        self.menu3.geometry("400x400")
        self.menu3.configure(bg='aquamarine2')

        Button(self.menu3, text="listar Cursos",bg= "bisque3",fg="DeepSkyBlue4").place(x=135, y=90, width=120, height=30)
        Button(self.menu3, text="Agregar Cursos", bg= "bisque3",fg="DeepSkyBlue4").place(x=120, y=130, width=150, height=30)
        Button(self.menu3, text="Editar cursos", bg= "bisque3",fg="DeepSkyBlue4").place(x=120, y=175, width=150, height=30)
        Button(self.menu3, text="Eliminar Cursos", bg= "bisque3",fg="DeepSkyBlue4", command=self.ELIMINI).place(x=125, y=215, width=150, height=30)
 
 #BOTON SALIR MENU3
        Button(self.menu3, text="regresar", bg= "bisque3",fg="DeepSkyBlue4",command=self.menu3.destroy).place(x=155, y=255, width=80, height=30)
       

        #self.menu3.mainloop()










#ELIMINAR CURSO------------------------------------------------------------
#INICIO MENU2--------------------------------------------------------------------------------------------------------------------------------
    def ELIMINI(self):
        
        self.elimi = Tk()
        self.elimi.title("seleccionar archivo")
        self.elimi.geometry("400x200")
        self.elimi.configure(bg='aquamarine2')
        self.menu3.destroy()


#BOTON SALIR MENU2
        Button(self.elimi, text="regresar",bg= "bisque3",fg="DeepSkyBlue4",command=self.ele).place(x=250, y=110, width=120, height=30)
        
       # self.menu2.mainloop()


       
#eliminar todo de menu3
    def ele(self):
        self.elimi.destroy()
        self.func2()






#FIN DE LA CLASE

menuU()