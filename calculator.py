def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2



operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}



def calculartor():

    num1=float(input("What is the first number?:"))
    for symbol in operations:
        print(symbol)
    should_continue=True

    while should_continue:
        operation_symbol=input("Pick an opeartion:")
        num2=float(input("What is the next number?:"))
        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1,num2)
        print(answer)
        if input("y to cont n to start new")=='y':
            num1=answer
        else:
            should_continue=False
            
            calculartor()



calculartor()
