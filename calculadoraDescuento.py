from streamlit import number_input,write,checkbox,title

def leer_datos():
    title("Calculadora de descuento")
    descuento_check=False
    impuesto_check=False
     
    if checkbox("Descuento personalizado"):
        descuento = number_input("Ingrese descuento",max_value=100,min_value=0)/100
        descuento_check = True
        
    
    if checkbox("Impuesto personalizado"):
        impuesto = number_input("Ingrese impuesto",max_value=100,min_value=0)/100
        impuesto_check=True
        
        
    precio = number_input("Ingrese el precio del producto")
   
    
    check = (descuento_check,impuesto_check)
    match check:
        case check if check == (True,True):
            calcular_precio_final(precio,descuento,impuesto)
        case check if check == (True,False):
            calcular_precio_final(precio,descuento=descuento)
        case check if check == (False,True):
            calcular_precio_final(precio,impuesto=impuesto)
        case check if check == (False,False):
            calcular_precio_final(precio)
        


def calcular_precio_final(precio, descuento = 0.1, impuesto = 0.16):
    
    precio_descuento = precio * (1- descuento)
    precio_final = precio_descuento + (precio_descuento*impuesto)
    if precio_final:
        write(f"Precio final {precio_final:.2f}$")
    
    
    
