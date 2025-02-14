lista_pessoas = []

for i in range(15):
    altura = float(input(f'Digite a altura da pessoa nº{i + 1} em centimetros: '))
    genero = input(f'Digite o gênero da pessoa nº{i +1} (masculino ou feminino): ')

    lista_pessoas.append((altura, genero))

# print(lista_pessoas)

altura_homens = []
alturas = []
quantidade_de_mulheres = 0
quantidade_de_homens = 0

for altura, genero in lista_pessoas:
    alturas.append(altura)

    if genero == 'masculino':
        altura_homens.append(altura)
        quantidade_de_homens +=1
    elif genero == 'feminino':
        quantidade_de_mulheres += 1

# print(altura_homens)

media_homens = sum(altura_homens) / quantidade_de_homens

print(f'A maior altura do grupo é de{max(alturas):.1f} centimetros, a menor altura é de {min(alturas)} centimetros.')
print(f'A media de altura dos homens é {media_homens:.1f} centimetros.')
print(f'O número de pessoas do gênero feminino é {quantidade_de_mulheres}.')