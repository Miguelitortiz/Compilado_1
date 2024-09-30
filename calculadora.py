from streamlit import number_input,write,button,title

def leer_datos():
  title
  num1 = number_input("Ingrese el primer numero")
  num2 = number_input("Ingrese el segundo numero")
  operación = False   
  if button("Suma"):
      operación = "+"
  if button("Resta"):
      operación = "-"
  if button("Multiplicación"):
      operación = "*"
  if button("Division"):
      operación = "/"
      
  
  if operación:
      calculadora_flexible(num1,num2,operación)

    
def calculadora_flexible(num1,num2,operador):
    match operador:
        case "+":
          result = num1 + num2
        case "-":
          result = num1 - num2
        case "*":
          result = num1 * num2
              
        case "/":
          result = num1 / num2
          
    write(f"El resultado es: {result}")