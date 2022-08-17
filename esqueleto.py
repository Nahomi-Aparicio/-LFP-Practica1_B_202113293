from tkinter import END, messagebox

class Cuerpo :
    global lis
    lis=[]
    global litt
# ---------------------------------------------gestionar cursos _____________________________________________________________

# listar falta maso 1
    def prueba(self,mitad):
        try:
            if  lis== []:         
                 
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
#maso esta   3         
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
            conteo=0
            conteo1=len(lis)
            if lis==[]:
                messagebox.showinfo("agregar curso", "CURSO AGREGADO CORRECTAMENTE")
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

# yap 4       
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
                    if nu11== lis[i][0]:
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
               
#ya esta  mostrar     2
    def most(self,mo,muu,mee,maa,mii,paa,pee):
        mu=mo.get()
        mook=''
        me=''
        pe=''
        ma=''
        me=''
        micho=''
        mi=''
        cantid=len(lis)
        if mu == "":
            messagebox.showerror("ERROR", "escriba el codigo del curso ")
        
        else:
            for i in range(cantid-1):
                if mu==lis[i][0]:
                    print(lis[i])
                    mook= str(lis[i][1]) 
                    muu.configure(text=mook,font=("Helvetica",11))
                    ma= str(lis[i][2]) 
                    if ma=='':
                         maa.configure(text='ninguno',font=("Helvetica",11))
                      
                    else:
                         maa.configure(text='curso'+ma,font=("Helvetica",11))

                    mi= str(lis[i][4]) 
                    mii.configure(text=mi,font=("Helvetica",11))
                    
                    micho= str(lis[i][5])  
                    paa.configure(text=micho,font=("Helvetica",11))
                    me=lis[i][3]
                    if me=='1':
                        
                        mee.configure(text='obligatorio',font=("Helvetica",11))
                    else:
                        
                        mee.configure(text='opcional',font=("Helvetica",11))
                        
                    pe=lis[i][6]
                    
                    if pe=='1' or pe=='1\n':
                        pee.configure(text='Cursando ',font=("Helvetica",11))
                    elif pe=='-1'or pe=='-1\n':
                        pee.configure(text='Pendiente',font=("Helvetica",11))
                        
                    else:
                        pee.configure(text='Aprobado ',font=("Helvetica",11))
                    pass
                else:
                    pass
          
#LISTO   eliminar 5
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
                
#------------------------------cargar cursos-------------------------------------------------------------
#falta poquito
    def impresion(self,explorar):
       
        try:            
            archivo = open(explorar, "r", encoding ='utf-8')
            contenido = archivo.readline()

            while contenido != '':
                contenido = archivo.readline()
                tmp = contenido.split(",")
               
                lis.append(tmp)
                for p in lis:
                    O=1
                    for i in range(len(lis)):
                         if lis[i][0]==p[0]:
                            if O==2:
                                lis.remove(p)
                                
                            O+=1
            
            print(lis)
            messagebox.showinfo("cargar archivo", "ARCHIVO CARGADO CORRECTAMENTE")
            archivo.close()
           
        except UnicodeDecodeError:
            messagebox.showerror("Error", "el archivo no es compatible")
        except FileNotFoundError:
            messagebox.showerror("ERROR", "no se encontro el archivo")

#-------------------------------------CONTEO -------------------------------------
    def coint1(self,poo,po1,pou):
        
        lita=[]
        lito=[]
        liu=[]
        
        cantid=len(lis)
        if lis==[]:
             messagebox.showerror("ERROR", "NO EXISTEN CURSO AUN  ")
             pass
        else:
            for i in range(cantid-1):
                if "1" in lis[i][6] and '-1' not in lis[i][6]:
                    lita.append(lis[i][5])
                    l3 = sum(int(ele) for ele in lita)                    
                    poo.configure(text=l3,font=("Helvetica",11))
            for i in range(cantid-1):                            
                if "-1" in lis[i][6] :
                    lito.append(lis[i][5])
                    l2 = sum(int(ele) for ele in lito)
                    po1.configure(text=l2,font=("Helvetica",11))
                
            for i in range(cantid-1):           
                if "0" in lis[i][6] or "0\n" in lis[i][6]:                   
                    liu.append(lis[i][5])                    
                    sumu = sum(int(ele) for ele in liu)
                    pou.configure(text=sumu,font=("Helvetica",11))


    def boton1(self,sem11,poo1):
        se11=sem11.get()
        litaa=[]
        cantid=len(lis)

        for i in range(cantid-1):
            if se11 ==lis[i][4]:                    
                litaa.append(lis[i][5])
                l33 = sum(int(ele) for ele in litaa)                    
                poo1.configure(text=l33,font=("Helvetica",11))


    def boton2(self,sem12,poo2):
        se12=sem12.get()
        litoo=[]
        cantid=len(lis)
        cantid2=len(lis)
        for i in range(cantid-1):
            if lis[i][4] <=se12 and "1" in lis[i][3]:
        
                print('juan')
                             
                litoo.append(lis[i][5])
                l32 = sum(int(ele) for ele in litoo)
                print(l32) 
                print(litoo)                    
                poo2.configure(text=l32,font=("Helvetica",11))
                
                pass
   
 # CERRAR ARCHIVO
                    
Cuerpo()

