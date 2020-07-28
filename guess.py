import random


def run():
    numero_a_caso = random.randint(1, 100)
    numero_scelto = int(input('Scegli un numero da 1 a 100: '))
    while numero_scelto != numero_a_caso:
        if numero_scelto < numero_a_caso:
            print('Cerca un numero più grande')
        else:
            print('Cerca un numero più piccolo')
        numero_scelto = int(input('Scegli un altro numero: '))
    print('¡Hai Vinto!')


if __name__ == '__main__':
    run()
