#variavel      0      1        2        3              
pessoas = ['Diego','Jhenny','Romeu','Julieta' ]

print(pessoas[0])

for pessoa in pessoas:
    print(pessoa)


print(*pessoas)

turma = [   #    0     1         2
            ['Diego', 20, 'Desenvolvedor'], # 0
            ['Jhenny', 36, 'Programadora'], # 1
            ['Romeu', 27, 'Analista'] # 2
        ]

print(turma[1][0]) #lista[linha][coluna]
print(turma[1][1]) #lista[linha][coluna]

print(len(pessoas)) # retorna o tamanho da lista
print(pessoas[-2]) # retorna um indice de traz para frente
print(pessoas[1:]) # retorna a partir do indice
print(pessoas[:3]) # retorna a partir do indice
print(pessoas[1:3]) # retorna a partir do indice 1 até o indice 2

# pessoas = ['Diego', 'Jhenny', 'Romeu', 'Julieta', 'Maria']
print(pessoas)
pessoas[2] = "Celeste" #altera o indice
print(pessoas)

pessoas.append('Charlie') # inclui um registro no final da lista
print(pessoas)

pessoas.insert(3,'Lucy') # inclui um registro no indice indicado
# primeiro argumento = indice
# segundo argumento = registro(dados)
print(pessoas)

pessoas.pop() # exclui o ultimo registro
print(pessoas)

pessoas.pop(0) #exclui o registro com o indice passado
print(pessoas)

pessoas.remove('Celeste') # exclui o registro com valor passado
print(pessoas)

