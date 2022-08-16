
from tkinter import END, messagebox

class Cuerpo :
    global lis
    lis=[]
    global litt
# ---------------------------------------------gestionar cursos _____________________________________________________________
    def prueba(self,mitad):
        try:
            if  lis== []:         
                 print('---------------------')
                 lis.append(self.litt)
                 cantid=len(lis)
                 for i in range(cantid):
                      mitad.insert("",END, text=lis[i][0], values=(lis[i][1],lis[i][2],lis[i][3],lis[i][4],lis[i][5],lis[i][6]))
            else:
                cantisd=len(lis)
                for i in range(cantisd-1):
                   mitad.insert("",END, text=lis[i][0], values=(lis[i][1],lis[i][2],lis[i][3],lis[i][4],lis[i][5],lis[i][6]))
        except AttributeError:
          messagebox.showerror("ERROR", "no se ningun curso")
#maso esta            
    def optener(self,n1,n2,n3,n4,n5,n6):
        litt=[]
        self.litt=litt
        nu1=n1.get()
        nu2=n2.get()
        nu3=n3.get()
        nu4=n4.get()
        nu5=n5.get()
        nu6=n6.get()
        litt.append(nu1)
        litt.append(nu2)
        litt.append(nu3)        
        litt.append(nu4)
        litt.append(',')
        litt.append(nu5)
        litt.append(nu6)
        print('_____________________________')

        if nu1 == "":
            messagebox.showerror("ERROR", "escriba el codigo del curso ") #shi
        elif nu1!="" and nu2=="":
            messagebox.showerror("ERROR", "llene los demas espacios")#shi
        elif  nu4!='1' and nu4!='0':
            messagebox.showerror("ERROR", "opcionalidad incorrecta")
        elif  nu6!='1' and nu6!='0' and nu6!='-1':
            messagebox.showerror("ERROR", "Estado incorrecto")
        elif nu3=="" and nu4=="" and nu5=="" and nu6=="":
             messagebox.showerror("ERROR", "escriba el codigo del curso ") 
        #__________________________________________
        else:
            contar =0 
            print('vaca')
            conteo1=len(lis)
            if lis==[]:
                pass
            else:
                for i in range (conteo1-1):
                    if nu1 == lis[i][0]:
                        conteo=len(lis) 
                        lis.remove(lis[i])     
                        lis.insert(conteo-2,self.litt)
                        print(lis)
                        messagebox.showinfo('curso cargado',"su curso se a cargado")
                        break
                
                    else :
                        contar+=1
                        if contar ==(conteo1-1):
                            lis.insert(conteo-1,self.litt)
                            print(lis)
                            messagebox.showinfo('CURSO CARGADO',"su curso se aagregado correctamente")
                            break
            
                    


                
    def okis(self):
        if lis==[]:           
            pass
        else :
            conteo=len(lis)      
            lis.insert(conteo-1,self.litt)
            print(lis)
            
                
    def edi(self,n11,n22,n33,n44,n55,n66):
        litto=[]
        
        nu11=n11.get()
        nu22=n22.get()
        nu33=n33.get()
        nu44=n44.get()
        nu55=n55.get()
        nu66=n66.get()
        litto.append(nu11)
        litto.append(nu22)
        litto.append(nu33)        
        litto.append(nu44)
        litto.append(',')
        litto.append(nu55)
        litto.append(nu66)
        print('_____________________________')

        if nu11 == "":
            messagebox.showerror("ERROR", "escriba el codigo del curso ") #shi
        elif nu11!="" and nu22=="":
            messagebox.showerror("ERROR", "llene los demas espacios")#shi
        elif  nu44!='1' and nu44!='0':
            messagebox.showerror("ERROR", "opcionalidad incorrecta\n"+"solo se acepta 1 o 0")
        elif  nu66!='1' and nu66!='0' and nu66!='-1':
            messagebox.showerror("ERROR", "Estado incorrecto\n"+"solo se acepta 1 , 0 o -1")
        elif nu11!="" and nu33=="" and nu44=="" and nu55=="" and nu66=="":
             messagebox.showerror("ERROR", "escriba el codigo del curso ") 
        #__________________________________________
        else:
            contar=0
            conteo1=len(lis)
            if lis==[]:
                messagebox.showerror('editar',"no existen cursos para editar")
                pass
            else:
                for i in range (conteo1-1):
                    if litto[i] == lis[i][0]:
                        conteo1=len(lis) 
                        lis.remove(lis[i])     
                        lis.insert(conteo1-2,litto)
                        print(lis)
                        messagebox.showinfo('editar',"su curso a sido editado")
                        break
                    else :

                        contar+=1
                        if contar ==(conteo1-1):
                            messagebox.showerror('editar',"su curso no existe")
                            break
               
#falta mostrar       
    def most(self,mo,s1):
        mu=mo.get()
        
        cantid=len(lis)
        if mu == "":
            messagebox.showerror("ERROR", "escriba el codigo del curso ")
        else:
            for i in range(cantid-1):
                if mu==lis[i][0]:
                     print(lis[i])
                     

                     mook= str(lis[i][1]) 
                     print(mook)
                else:
                    pass
          #LISTO    
    def eliC (self,elw):
        mu=elw.get()
        cantid=len(lis)
        if mu == "":
            messagebox.showerror("ERROR", "escriba el codigo del curso ")
         
        else:
            for i in range(cantid-1):
                if mu==lis[i][0]:
                    lis.remove(lis[i])
                    messagebox.showerror("eliminar curso", "SU CURSO SE ELIMINO CORRECTAMENTE")
                    print(lis)
                    break
                elif mu != lis:
                    messagebox.showerror("eliminar curso", "SU CURSO NO EXISTE")
                    break
                
#------------------------------cargar cursos-------------------------------------------------------------
    def impresion(self,explorar):
        li=[]
        try:            
            archivo = open(explorar, "r", encoding ='utf-8')
            contenido = archivo.readline()

            while contenido != '':
                  contenido = archivo.readline()
                  tmp = contenido.split(",")
                  li.append(tmp) 
            archivo.close()
            print('archivo cargado')
            
            for e in li:
                  if e not in lis:
                    if e not in lis:
                        lis.append(e)
            print(lis)

        except UnicodeDecodeError:
            messagebox.showerror("Error", "el archivo no es compatible")
        except FileNotFoundError:
            messagebox.showerror("ERROR", "no se encontro el archivo")


#-------------------------------------CONTEO -------------------------------------
    def coint1(self):
        print('holi')
        cantid=len(lis)
        for i in range(cantid-1):
                if "1" in lis[i][6] and '-1' not in lis[i][6]:
                    print(lis[i])
                    myNewList = [int(string) for string in lis[i][5]]
                    #listSum = sum(myNewList)
                    sum2 = sum(number for number in myNewList)
                    print(f'{sum2}')
                    
                else:
                    pass
 # CERRAR ARCHIVO
                     
Cuerpo()

""" edi1=n11.get()
        cantid=len(lis)
        if edi1 == "":
            messagebox.showerror("ERROR", "escriba el codigo del curso ")
        else:
            for i in range(cantid-1):
                if edi1==lis[i][0]:
                     print(lis[i])
                """


"""     
          
     
   def F(self,mitad):
        #cantid=len(litt)
        for i in range(1):
              mitad.insert("",END, text=litt[i][0], values=(litt[i][1],litt[i][2],litt[i][3],litt[i][4],litt[i][5],litt[i][6]))
    

            litt[i].append(num1)
            litt[i].append(num2)
            litt[i].append(num3)
            litt[i].append(num4)
            litt[i].append(',')
            litt[i].append(num5)
            litt[i].append(num6)

litt[i].append(n2.get())
                
        global list
        list=[]


        while contenido != '':
              contenido = archivo.readline()
              tmp = contenido.split('\n')              
              list.append(tmp)
        print(list)
        """
        

""""archivo = open(explorar, "r")
        #linea = archivo.readline()
        #lis = archivo.readline()        
        print('archivo abierto')
        global contenido
        contenido = archivo.read()
        archivo.close
        print (contenido)
        #print (contenido2)
        #archivo.close
        self.texto = contenido
        print('archivo abierto')
        print (contenido)"""



      
