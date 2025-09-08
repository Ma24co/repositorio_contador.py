
import time

def cuenta_regresiva(numero):
    """
    Realiza una cuenta regresiva desde el número dado hasta 0.
    """
    while numero >= 0:
        print(numero)
        time.sleep(1)  # Pausa de 1 segundo entre números
        numero -= 1

if __name__ == "__main__": 
    numero_inicial = int(input("Ingrese un número para iniciar la cuenta regresiva: "))
    cuenta_regresiva(numero_inicial)