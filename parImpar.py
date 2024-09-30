from streamlit import text_input,write,title
def leer_datos():
    title("Números pares e impares")
    datos=text_input("Ingrese los datos separados por espacios").split()
    correctos = True
    for i in datos:
        if not(i.isnumeric()):
            write("Ingrese los datos correctos")
            correctos = False
        
            
    if correctos : numeros_pares_e_impares([int(i) for i in datos])
    
    
def numeros_pares_e_impares(lista):
    pares = []
    impares = []
    for elemento in lista:
        pares.append(elemento) if elemento%2==0 else impares.append(elemento)
        
        if elemento == lista[-1]:
        
            write(f"Pares: {pares}")
            write(f"Impares: {impares}")