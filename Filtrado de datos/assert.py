def divisors(num):
    
    divisors = []
    for i in range(1, num + 1 ):
        if num % i == 0:
            divisors.append(i)
    
    return divisors


def run():
    
    num = input("ingrese un numero: ")
    assert num.isnumeric() and num > 0, "Debes ingresar un número valido y positivo"
    print(divisors(int(num)))
    print("Terminó mi programa")
    
if __name__ == "__main__":
    run()