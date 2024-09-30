from streamlit import text_input, number_input, write, button, title

def informacion_personal(**kwargs):
    for clave, valor in kwargs.items():
        write(f"{clave}: {valor}")

def leer_datos():
    title("Información Personal")


    nombre = text_input("Nombre")
    edad = number_input("Edad", min_value=0, max_value=120)
    direccion = text_input("Dirección")
    telefono = text_input("Teléfono")


    if button("Enviar"):
        informacion_personal(nombre=nombre, edad=edad, direccion=direccion, telefono=telefono)