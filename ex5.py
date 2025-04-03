def solve(num_produtos: int, capacidade_mochila: int, items: list[tuple[int, int]]):
    max_tab = [[0 for _ in range(capacidade_mochila + 1)] for _ in range(num_produtos + 1)]
    iteracoes = 0
    instrucoes = 0

    for i in range(1, num_produtos + 1):
        for j in range(1, capacidade_mochila + 1):
            iteracoes += 1
            instrucoes += 1  # Incrementa para a comparação do if
            if items[i - 1][0] <= j:
                instrucoes += 3  # Incrementa para acesso a items, max e soma
                max_tab[i][j] = max(max_tab[i - 1][j], items[i - 1][1] + max_tab[i - 1][j - items[i - 1][0]])
            else:
                instrucoes += 1  # Incrementa para atribuição
                max_tab[i][j] = max_tab[i - 1][j]

    return max_tab[num_produtos][capacidade_mochila], iteracoes, instrucoes


testes = [
    (3, 5, [(2, 3), (3, 4), (4, 5)]),
    (4, 10, [(2, 1), (3, 2), (4, 5), (5, 6)]),
    (5, 8, [(1, 1), (2, 2), (3, 4), (2, 3), (4, 5)])
]

print("Resultado | Iterações | Instruções")
print("-" * 35)

for num_produtos, capacidade_mochila, items in testes:
    resultado, iteracoes, instrucoes = solve(num_produtos, capacidade_mochila, items)
    print(f"{resultado:^9} | {iteracoes:^9} | {instrucoes:^10}")
