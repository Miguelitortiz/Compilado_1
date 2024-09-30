from streamlit import text_input,write,title

def leer_datos():
    title("Suma de una lista de números")
    datos=text_input("Ingrese los datos separados por espacios").split()
    correctos = True
    for i in datos:
        if not(i.isnumeric()):
            write("Ingrese los datos correctos")
            correctos = False
        
            
    if correctos : sumar_lista([int(i) for i in datos])
            
    
    
def sumar_lista(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    if suma != 0:
        write(f"La suma es {suma}")
            