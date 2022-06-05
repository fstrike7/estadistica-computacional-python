import random

def tirar_dado(numero_tiros):
    secuencia_de_tiros = list()
    for _ in range(numero_tiros):
        tiro = random.choice([1,2,3,4,5,6])
        secuencia_de_tiros.append(tiro)
    return secuencia_de_tiros

def main(numero_tiros, numero_intentos):
    tiros = list() 
    for _ in range(numero_intentos):
        secuencia_de_tiros = tirar_dado(numero_tiros) # Guarda los resultados de los tiros de dado.
        tiros.append(secuencia_de_tiros)

    # Por cada secuencia, evalua si por lo menos contiene un 1, suma los True.
    tiros_con_1 = sum(1 not in secuencia for secuencia in tiros)
    prob_tiros_con_1 = tiros_con_1 / numero_intentos
    print(f'Cuál es la probabilidad de no obtener por lo menos un 1 en {numero_tiros} tiros = {prob_tiros_con_1}')
if __name__ == "__main__":
    tiros = int(input('Cuantos tiros del dado: '))
    intentos = int(input('Cantidad de veces que corre la simulación: '))

    main(tiros, intentos)