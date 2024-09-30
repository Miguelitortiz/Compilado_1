from streamlit import text_input,write,title

def multiplicar_todos(*nums):
    prod = 1
    for numero in nums:
        prod *= numero
  
    if prod != 1:
	    write(f"El producto es : {prod}")


def leer_datos():
    title("Multiplicación con *args")
    datos=text_input("Ingrese los datos separados por espacios")
    correcto = True
    numeros_lista=[]
    for num in datos.split():
        if num.strip().isdigit():
             numeros_lista.append(float(num))
             
        else:
            write("Ingrese los datos correctos")
            correcto = False
            
    if correcto:

        multiplicar_todos(*numeros_lista)

