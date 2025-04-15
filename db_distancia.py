iters = 0

def ED(s: str, t: str) -> int:
    m = len(s)
    n = len(t)

    # Criar a matriz (n+1 x m+1)
    max_tab = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Inicializar bordas
    for i in range(n + 1):
        max_tab[i][0] = i  # deletar todos os caracteres de t até string vazia

    for j in range(m + 1):
        max_tab[0][j] = j  # inserir todos os caracteres de s na string vazia

    # Preencher o resto da matriz
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if t[i - 1] == s[j - 1]:  # cuidado com a ordem
                custo_extra = 0
            else:
                custo_extra = 1

            max_tab[i][j] = min(
                max_tab[i - 1][j] + 1,        # remoção
                max_tab[i][j - 1] + 1,        # inserção
                max_tab[i - 1][j - 1] + custo_extra  # substituição ou match
            )

    return max_tab[n][m]


s1 = "Casablanca"
s2 = "Portentoso"



res = ED(s1, s2) 
print(res)
print(iters)
