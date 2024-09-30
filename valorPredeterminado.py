from streamlit import number_input,write,checkbox,text_input,title

def leer_datos():
    title("Funciones con valores predeterminados")
    cantidad_check = False
    precio_check = False
     
    if checkbox("Cantidad personalizada"):
        cantidad = number_input("Ingrese la cantidad")
        cantidad_check = True
        
    
    if checkbox("Precio por unidad personalizado"):
        precio = number_input("Ingrese el precio")
        precio_check = True
        
    nombre = text_input("Ingrese el nombre del producto")
   
    if nombre:
        
        check = (precio_check,cantidad_check)
        match check:
            case check if check == (True,True):
                producto(nombre,cantidad,precio)
            case check if check == (True,False):
                producto(nombre,precio=precio)
            case check if check == (False,True):
                producto(nombre,cantidad=cantidad)
            case check if check == (False,False):
                producto(nombre)
            


def producto(nombre, cantidad = 1, precio = 10):
    write(nombre)
    write(f"Cantidad: {cantidad}")
    write(f"Precio : {precio}")
    write(f"Total a pagar {precio*cantidad}")
  
    
    
    
