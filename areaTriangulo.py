from streamlit import number_input,write,title

def calcular_area_triangulo():
    title("Area de un triángulo:")
    base = number_input("Ingrese la medida de la base")
    altura = number_input("Ingrese la medida de la altura")
    area = base * altura / 2
    if base and altura:
        
        write(f"El área es {area:.2f}")