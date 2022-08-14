import ast
from ctypes import LittleEndianStructure
from re import I
from tkinter import END, messagebox

class Cuerpo :
    global lis
    lis=[]
    


   

    def prueba(self,mitad):
        
        print('---------------------')
        cantid=len(lis)
        for i in range(cantid-1):
              mitad.insert("",END, text=lis[i][0], values=(lis[i][1],lis[i][2],lis[i][3],lis[i][4],lis[i][5],lis[i][6]))

        print('archivo en la lista')
        
    
        
    
    def optener(self,n1,n2,n3,n4,n5,n6):
        global Litt
        self.litt=[]
        self.litt.append(n1.get())
        self.litt.append(n2.get())
        self.litt.append(n3.get())        
        self.litt.append(n4.get())
        self.litt.append(',')
        self.litt.append(n5.get())
        self.litt.append(n6.get())
        print('_____________________________')
        print(self.litt)
        print('_____________________________')
        conteo=len(lis)        
        lis.insert(conteo-1,self.litt)
        print(lis)
    


    def impresion(self,explorar):
        
        li=[]
        try:            
            archivo = open(explorar, "r")
            contenido = archivo.readline()
#print('se imprime')
            while contenido != '':
                  contenido = archivo.readline()
                  tmp = contenido.split(",")
                  li.append(tmp) 
            archivo.close()
            print('archivo cargado')
            print(li)
            for e in li:
                  if e not in lis:
                    lis.append(e)

            
            
        except UnicodeDecodeError:
            messagebox.showerror("Error", "el archivo no es compatible")
        except FileNotFoundError:
            messagebox.showerror("ERROR", "no se encontro el archivo")
       
    

        

    
        
   



        

    
   








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



      
# CERRAR ARCHIVO
        #archivo.close()
              
Cuerpo()