def knapsack_forca_bruta(capacidade, pesos, valores):
    n = len(pesos)
    max_valor = 0
    melhor_combinacao = []
    iteracoes = 0

    for i in range(2**n):
        combinacao = []
        peso_total = 0
        valor_total = 0

        for j in range(n):
            if (i >> j) & 1:
                combinacao.append(j)
                peso_total += pesos[j]
                valor_total += valores[j]

        iteracoes += 1

        if peso_total <= capacidade and valor_total > max_valor:
            max_valor = valor_total
            melhor_combinacao = combinacao

    return max_valor, melhor_combinacao, iteracoes

# Exemplo de uso
capacidade = 50
pesos = [10, 20, 30]
valores = [60, 100, 120]

max_valor, melhor_combinacao, iteracoes = knapsack_forca_bruta(capacidade, pesos, valores)

print("Valor máximo:", max_valor)
print("Melhor combinação (índices dos itens):", melhor_combinacao)
print("Número de iterações:", iteracoes)
