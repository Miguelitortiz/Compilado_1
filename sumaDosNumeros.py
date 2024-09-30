from streamlit import number_input,write,title

def sumar():
    title("Suma de dos números:")
    num1 = number_input("Ingrese el primer número")
    num2 = number_input("Ingrese el segundo número")
    if num1 and num2:
        write(f"La suma es {num1+num2}")