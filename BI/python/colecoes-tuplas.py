# Tuplas em python é uma sequencia imutavel de valores de qualquer tipo

coordenadas = (-49,200,-20,80,200)

print(coordenadas)
print(type(coordenadas))

pessoas_lista = ['João', 'Maria', 'Romeu', 'Julieta']

print(pessoas_lista)
print(type(pessoas_lista))

pessoas_tupla = tuple(pessoas_lista)

print(pessoas_tupla)
print(type(pessoas_tupla))

pessoa = ('Maria',30, 'Desenvolvedora')

print(pessoa[0])

nome,idade,profissao = pessoa

print(nome)
print(idade)
print(profissao)

tupla_aninhada = (
    ('Maçã',1),
    ('Banana',2),
    ('Laranja',3)
)

print(tupla_aninhada[2][0]) #nome_tupla[linha][coluna]