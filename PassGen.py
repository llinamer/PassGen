import os
import time
import random
import string
import secrets

def limpiar():
    os.system("clear" if os.name == "posix" else "cls")

def efecto_hacker(texto):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.03)
    print()

def animacion_carga():
    chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(20):
        linea = "".join(random.choice(chars) for _ in range(60))
        print("\033[32m" + linea + "\033[0m")
        time.sleep(0.05)

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(caracteres) for _ in range(longitud))

def main():
    limpiar()
    print("\033[32m")
    efecto_hacker(">>> INITIALIZE SYSTEM...")
    time.sleep(0.5)
    efecto_hacker(">>> ACCESSING A SECURE DATABASE...")
    time.sleep(0.5)

    animacion_carga()

    efecto_hacker(">>> PASSWORD GENERATOR ENABLE")
    longitud = int(input("\nDesired length: "))

    efecto_hacker("\n>>> Generating a password...")
    time.sleep(1)

    contraseña = generar_contraseña(longitud)

    print("\n\033[32m>>> PASSWORD CREATED:\033[0m")
    print("\033[32m" + contraseña + "\033[0m")

    efecto_hacker("\n>>> PROCESS COMPLETED")

if __name__ == "__main__":
    main()
