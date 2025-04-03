def knapsack_divisao_conquista(capacidade, pesos, valores, n):
    if n == 0 or capacidade == 0:
        return 0

    if pesos[n - 1] > capacidade:
        return knapsack_divisao_conquista(capacidade, pesos, valores, n - 1)

    return max(
        valores[n - 1] + knapsack_divisao_conquista(capacidade - pesos[n - 1], pesos, valores, n - 1),
        knapsack_divisao_conquista(capacidade, pesos, valores, n - 1)
    )

capacidade = 50
pesos = [10, 20, 30]
valores = [60, 100, 120]
n = len(pesos)

max_valor = knapsack_divisao_conquista(capacidade, pesos, valores, n)

print("Valor máximo:", max_valor)
