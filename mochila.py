def solve(num_produtos: int, capacidade_mochila: int, items: list[tuple[int, int]]):
    max_tab = [[0 for _ in range(capacidade_mochila + 1)] for _ in range(num_produtos + 1)]

    for i in range(1, num_produtos + 1):
        for j in range(1, capacidade_mochila + 1):
            if items[i-1][0] <= j:
                max_tab[i][j] = max(max_tab[i-1][j], items[i-1][1] + max_tab[i-1][j - items[i-1][0]])
            else:
                max_tab[i][j] = max_tab[i-1][j]

    return max_tab[num_produtos][capacidade_mochila]


res = solve(3, 5, [(2, 3), (3, 4), (4, 5)])
print(res)
