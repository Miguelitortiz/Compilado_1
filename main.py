import streamlit as st
import saludoSimple,sumaDosNumeros,areaTriangulo,calculadoraDescuento,sumaLista
import valorPredeterminado,parImpar,multiplicacionArgs,calculadora,informacionPersona
def main():

    menu = {
        "Función de saludo simple":saludoSimple.saludar,
        "Suma de dos números": sumaDosNumeros.sumar,
        "Área de un triángulo":areaTriangulo.calcular_area_triangulo,
        "Calculadora de descuento":calculadoraDescuento.leer_datos,
        "Suma de una lista de números":sumaLista.leer_datos,
        "Funciones con valores predeterminados":valorPredeterminado.leer_datos,
        "Números pares e impares": parImpar.leer_datos,
        "Multiplicación con *args":multiplicacionArgs.leer_datos,
        "Información personal":informacionPersona.leer_datos,
        "Calculadora flexible" : calculadora.leer_datos
        
    }   
    
    keys = tuple(menu.keys())
    option = st.sidebar.selectbox("Menu",keys)
    
    menu[option]()
    
if __name__ == "__main__":
    main()
    
    
            
            
    
    
   
   
    
 