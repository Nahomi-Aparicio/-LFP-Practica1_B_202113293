
from tkinter import messagebox
class Cuerpo :
    
   
    def impresion(self,explorar):
        global list
        list=[]
        try:            
            archivo = open(explorar, "r")
            contenido = archivo.readline()
        
            
        #print('se imprime')
            while contenido != '':
                  contenido = archivo.readline()
                  tmp = contenido.split(",")
                  list.append(tmp)             
            archivo.close()
            print('archivo cargado')
            
            
        except UnicodeDecodeError:
            messagebox.showerror("showerror", "Error")
        except FileNotFoundError:
            messagebox.showerror("showerror", "Error")

        

    def prueba(self,mitad):
        print('---------------------')
        cantid=len(list)
        for i in range(cantid-1):
              mitad.insert("",index='end', text=list[i][0], values=(list[i][1],list[i][2],list[i][3],list[i][4],list[i][5],list[i][6]))
        # Increment counter
        print('archivo en la lista')

   








""" def insert_data(self):
        
        self.treeview.insert('', 'end', text="Item_"+str(self.i),
                             values=(self.dose_entry.get() + " mg",
                                     self.modified_entry.get()))
        # Increment counter
        self.i = self.i + 1


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