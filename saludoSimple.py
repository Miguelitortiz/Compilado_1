from streamlit import text_input,write,title

def saludar():
    title("Función de saludo simple: ")
    nombre = text_input("Ingrese su nombre")
    if nombre:  
      write(f"Hola, {nombre}")
    
if __name__ == "__main__":
    saludar()