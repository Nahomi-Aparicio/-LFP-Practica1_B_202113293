from tkinter import END, messagebox
from tkinter import ttk
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
from esqueleto import Cuerpo
class MenuU:
    global scaner
    scaner=Cuerpo()
    
    def __init__(self):       
        self.menu1 = Tk()
        self.menu1.title("PRACTICA 1")
        self.menu1.geometry("400x400")      
        frame = Frame(self.menu1)
        frame.configure(bg='aquamarine')
        frame.place(x=0, y=0, width=500, height=500)
#TEXTO DEL MENUu
        texto1 = Label(frame, text="Lab. Lenguajes Formales y de Programacion",bg='aquamarine',fg = "violetRed4")
        texto1.place(x=5, y=20, width=300, height=20)
        texto1.configure(font=("Helvetica",10))
        texto2 = Label(frame, text="Nombre: Genesis Nahomi Aparicio Acan",bg='aquamarine',fg = "violetRed4")
        texto2.place(x=5, y=50, width=280, height=20)
        texto2.configure(font=("Helvetica",10))
        texto3 = Label(frame, text="Carne del Estudiante: 202113293",bg='aquamarine',fg = "violetRed4")
        texto3.configure(font=("Helvetica",10))
        texto3.place(x=5, y=80, width=230, height=20)
        #BOTONES
        Button(frame, text="Cargar archivo",bg= "bisque3",fg="DeepSkyBlue4", command=self.func1).place(x=145, y=180, width=120, height=30)
        Button(frame, text="Gestionar Cursos", bg= "bisque3",fg="DeepSkyBlue4",command=self.func2).place(x=130, y=230, width=150, height=30)
        Button(frame, text="conteo de creditos", bg= "bisque3",fg="DeepSkyBlue4",command=self.Conte).place(x=130, y=280, width=150, height=30)
        Button(frame, text="salir", bg= "bisque3",fg="DeepSkyBlue4",command=self.menu1.quit).place(x=165, y=325, width=80, height=30)

#FIN MENUU
        
        self.menu1.mainloop()
#*******************************INICIO MENU2   SELECCIONAR ARCHIVO**************************************************************************
    def func1(self):        
        self.menu2 = Tk()
        self.menu2.title("seleccionar archivo")        
        self.menu2.geometry("400x200")
        self.menu2.configure(bg='aquamarine2')        
        self.menu1.destroy()        
        ruta = Label(self.menu2, text="Ruta",bg='aquamarine2',fg = "violetRed4")
        ruta.place(x=20, y=40, width=50, height=20)
        ruta.configure(font=("Helvetica",11))
        self.rut =Entry(self.menu2)
        self.rut.place(x=80, y=40, width=250, height=20)
        #BOTON SALIR MENU2
        Button(self.menu2, text="regresar",bg= "bisque3",fg="DeepSkyBlue4",command=self.coca).place(x=280, y=150, width=100, height=30)
        Button(self.menu2, text="Seleccionar",bg= "bisque3",fg="DeepSkyBlue4",command=self.browseFiles).place(x=160, y=80, width=100, height=30)
        
    def browseFiles(self):
        global scaner
        self.explor = filedialog.askopenfilename(initialdir = "/",title = "seleccione el archivo", filetypes = (("Text files", "*.csv*"), ("all files","*.*")))            
        self.rut.insert(0,self.explor ) 
        
        scaner.impresion(explorar=self.explor)
       
    def coca(self):
        self.menu2.destroy()
        #exporto mi clase y mi metodo parametrizado 
        #scaner=Cuerpo()
        #hace la funcion del metodo de esa clase con los valores del metodo de arriba 
        #scaner.impresion(explorar=self.explor)
        self.__init__()
       
#********************************INICIO MENU3 Gestionar cursos ARCHIVO *************************************************************************
    def func2(self):
        
        self.menu3 = Tk()
        self.menu3.title("Gestionar curso")
        self.menu3.geometry("350x400")
        self.menu3.configure(bg='aquamarine2')
      

        Button(self.menu3, text="listar Cursos",bg= "bisque3",fg="DeepSkyBlue4",command=self.LISTAR).place(x=120, y=80, width=130, height=30)
        Button(self.menu3, text="mostrar cursos",bg= "bisque3",fg="DeepSkyBlue4",command=self.mostrar).place(x=120, y=130, width=130, height=30)
        Button(self.menu3, text="Agregar Cursos", bg= "bisque3",fg="DeepSkyBlue4",command=self.agrgr).place(x=120, y=175, width=130, height=30)
        Button(self.menu3, text="Editar cursos", bg= "bisque3",fg="DeepSkyBlue4",command=self.EDIT).place(x=120, y=225, width=130, height=30)
        Button(self.menu3, text=" Eliminar Cursos ", bg= "bisque3",fg="DeepSkyBlue4", command=self.ELIMINI).place(x=120, y=275, width=130, height=30)
 
        #BOTON SALIR MENU3
        Button(self.menu3, text="regresar", bg= "bisque3",fg="DeepSkyBlue4",command=self.menu3.destroy).place(x=120, y=330, width=130, height=30)

    def mostrar(self):        
        self.most= Tk()
        self.most.title("Agregar Cursos")
        self.most .geometry("450x450")
        self.most.configure(bg='aquamarine2')
        self.menu3.destroy()



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
#eliminar todo de menu3
    def ele(self):
        self.elimi.destroy()
        self.func2()
#LISTAR CURSO--------------------------
    def LISTAR(self):
        
        
        self.listar = Tk()
        self.listar.title("listar Cursos")
        self.listar .geometry("560x300")
        self.listar.configure(bg='aquamarine2')
        self.menu3.destroy()
        
        Button(self.listar, text="regresar",bg= "bisque3",fg="DeepSkyBlue4",command=self.eles).place(x=420, y=260, width=120, height=30)
        columns =('#1','#2','#3','#4','#5','#6')
        #mi tablita  la cual esta enlazada a la ventana y luego a las columnas
        self.mita=ttk.Treeview(self.listar,columns=columns ,height=8)
        #self.mita.grid(row=0,column=10,padx=10,pady=10,ipady=30)
        self.mita.grid(sticky="W")
        
        self.mita.column('#0',width=70, anchor=CENTER)
        self.mita.column('#1',width=120, anchor=CENTER)
        self.mita.column('#2',width=80, anchor=CENTER)
        self.mita.column('#3',width=80, anchor=CENTER)
        self.mita.column('#4',width=70, anchor=CENTER)
        self.mita.column('#5',width=70, anchor=CENTER)
        self.mita.column('#6',width=70, anchor=CENTER)
      
        #definir columnas
        #self.mita['columns']=("juan","pablo","maria")
        #encabezados de mi tablita
        self.mita.heading('#0',text="Codigo", anchor=CENTER)
        self.mita.heading('#1',text="nombre", anchor=CENTER)
        self.mita.heading('#2',text="Pre requisitos", anchor=CENTER)
        self.mita.heading('#3',text="Opcionalidad", anchor=CENTER)
        self.mita.heading('#4',text="Semestre", anchor=CENTER)
        self.mita.heading('#5',text="Creditos", anchor=CENTER)
        self.mita.heading('#6',text="Estado", anchor=CENTER)
        scaner.prueba(mitad=self.mita)
       
        
       
        

        self.mita.pack(side='left') # supongo que sabes usar pack
        ejscrollbar= ttk.Scrollbar(self.listar,orient=VERTICAL,command=self.mita.yview)
        ejscrollbar.pack(side='right',fill='y')
        self.mita.configure(yscrollcommand=ejscrollbar.set)

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
        # -----------------------
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
        Button(self.agr, text="Agregar",bg= "bisque3",fg="DeepSkyBlue4",command=self.entradas).place(x=210, y=300, width=80, height=30)
        Button(self.agr, text="regresar",bg= "bisque3",fg="DeepSkyBlue4",command=self.elem).place(x=310, y=400, width=100, height=30)  
    def entradas(self):
        scaner.optener(n1=self.ent1,n2=self.ent2,n3=self.ent3,n4=self.ent4,n5=self.ent5,n6=self.ent6)
        
    
    def elem(self):
        self.agr.destroy()
        self.func2()
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
        #----------------------- 
        self.cre = Label(self.cont, text="Creditos Aprobados:",bg='aquamarine2',fg = "violetRed4")
        self.cre.place(x=10, y=40, width=150, height=20)
        self.cre.configure(font=("Helvetica",11))
        #----------------------- 
        self.crec = Label(self.cont, text="Creditos Cursados:",bg='aquamarine2',fg = "violetRed4")
        self.crec.place(x=10, y=70, width=150, height=20)
        self.crec.configure(font=("Helvetica",11))
        #----------------------- 
        self.crep = Label(self.cont, text="Creditos Pendientes:",bg='aquamarine2',fg = "violetRed4")
        self.crep.place(x=10, y=100, width=150, height=20)
        self.crep.configure(font=("Helvetica",11))
        #----------------------- 
        self.creo = Label(self.cont, text="Creditos obligatorios hasta semestre N :",bg='aquamarine2',fg = "violetRed4")
        self.creo.place(x=10, y=130, width=280, height=20)
        self.creo.configure(font=("Helvetica",11))  
                #  ----------------------- 
        self.entt = Text(self.cont)
        self.entt.place(x=290, y=130, width=80, height=20)
               #----------------------- 
        self.sem = Label(self.cont, text="semestre :",bg='aquamarine2',fg = "violetRed4")
        self.sem.place(x=100, y=180, width=150, height=20)
        self.sem.configure(font=("Helvetica",11))
        #----------------------- 
        self.se=Combobox(self.cont)
        self.se.place(x=210, y=180, width=50, height=20)
       #-----------------------      
        Button(self.cont, text="Contar",bg= "bisque3",fg="DeepSkyBlue4").place(x=280, y=180, width=80, height=20)
        #----------------------- 
        self.cres = Label(self.cont, text="Creditos del semestre :",bg='aquamarine2',fg = "violetRed4")
        self.cres.place(x=10, y=230, width=280, height=20)
        self.cres.configure(font=("Helvetica",11))
        #----------------------- 
        self.sem = Label(self.cont, text="semestre :",bg='aquamarine2',fg = "violetRed4")
        self.sem.place(x=100, y=260, width=150, height=20)
        self.sem.configure(font=("Helvetica",11))
        #----------------------- 
        self.se=Combobox(self.cont)
        self.se.place(x=210, y=260, width=50, height=20)
        #-----------------------         
        Button(self.cont, text="Contar",bg= "bisque3",fg="DeepSkyBlue4").place(x=280, y=260, width=80, height=20)
        #-----------------------         
        Button(self.cont, text="regresar",bg= "bisque3",fg="DeepSkyBlue4",command=self.cont.destroy).place(x=350, y=320, width=90, height=20)
#----------------------- 
#FIN DE LA CLASE
MenuU()

