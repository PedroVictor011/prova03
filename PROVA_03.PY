

numero_seceto = 7

tentativas_maximas = 3
tentaivas = 0

print('Bem vindo ao jogo da adivinhação.')
print('Tente adivinhar o numero de 1 a 10 voce tem 3 tentativas.')

while tentaivas < tentativas_maximas:

    tentativa = int(input('Digite sua tentativa:'))
    tentaivas += 1
    if tentativa == numero_seceto:
        print('Parabens voce acertou.')
        break
    elif tentaivas == tentativas_maximas :
        print('Suas tentativas acabaram.')
    elif tentativa != numero_seceto:
        print('Tente novamente.')
    elif tentaivas == tentativas_maximas :
        print('Suas tentativas acabaram.')
    else:
        print('O jogo acabou voce perdeu.')