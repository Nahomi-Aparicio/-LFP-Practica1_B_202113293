class Cuerpo :
    
   
    def impresion(self,explorar):
        global list
        archivo = open(explorar, "r")
        contenido = archivo.readline()
        
        list=[]
        #print('se imprime')
        while contenido != '':
              contenido = archivo.readline()
              tmp = contenido.split(",")
                           
              list.append(tmp)
             
        archivo.close()
        self.prueba()

    def prueba(self):
        print(list[1][1])
        print(list[1][4])
        print(list)
    







"""
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