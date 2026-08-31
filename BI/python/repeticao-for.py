for c in range(10):
    print('passo')
    print(c)

inicio = 1
fim = int(input('Digite o valor final:'))

#for c in range(valor_inicial, valor_fina + 1, valor_passo)?
for c in range(inicio, fim + 1, 2):
    print(f'Passo - {c}')