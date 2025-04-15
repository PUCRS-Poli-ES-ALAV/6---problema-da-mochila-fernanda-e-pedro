def ED(s: str, t: str) -> int:
    m = len(s)
    n = len(t)

    max_tab = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    iteracoes = 0  # contador

    for i in range(n + 1):
        max_tab[i][0] = i

    for j in range(m + 1):
        max_tab[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            iteracoes += 1

            if t[i - 1] == s[j - 1]:
                custo_extra = 0
            else:
                custo_extra = 1

            max_tab[i][j] = min(
                max_tab[i - 1][j] + 1,
                max_tab[i][j - 1] + 1,
                max_tab[i - 1][j - 1] + custo_extra
            )

    # Imprime a matriz
    # print("Matriz de Distância:")
    # for linha in max_tab:
    #     print(linha)

    print(f"\nNúmero de iterações: {iteracoes}")
    return max_tab[n][m]

ED("Casablanca", "Portentoso")

s1 = "".join(["Maven, a Yiddish word meaning accumulator of knowledge, began as an attempt to " ,
   			"simplify the build processes in the Jakarta Turbine project. There were several" , 
   			" projects, each with their own Ant build files, that were all slightly different." ,
   			"JARs were checked into CVS. We wanted a standard way to build the projects, a clear ", 
   			"definition of what the project consisted of, an easy way to publish project information" ,
   			"and a way to share JARs across several projects. The result is a tool that can now be" ,
   			"used for building and managing any Java-based project. We hope that we have created " ,
   			"something that will make the day-to-day work of Java developers easier and generally help " ,
   			"with the comprehension of any Java-based project."])
s2 = "".join(["This post is not about deep learning. But it could be might as well. This is the power of " ,
   			"kernels. They are universally applicable in any machine learning algorithm. Why you might" ,
   			"ask? I am going to try to answer this question in this article." , 
   		        "Go to the profile of Marin Vlastelica Pogančić" , 
   		        "Marin Vlastelica Pogančić Jun"])

ED(s1, s2)
