import sys

def var(i, j, n):
    """Codificação linear: linha i, coluna j -> variável 1..n^2"""
    return n * (i - 1) + j

def gerar_clausulas(n):
    clausulas = []

    # ao menos uma por linha
    for i in range(1, n + 1):
        clausulas.append([var(i, j, n) for j in range(1, n + 1)])

    # no máximo uma por linha
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(j + 1, n + 1):
                clausulas.append([-var(i, j, n), -var(i, k, n)])

    # no máximo uma por coluna
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            for k in range(i + 1, n + 1):
                clausulas.append([-var(i, j, n), -var(k, j, n)])

    # no máximo uma por diagonal principal (i - j = constante d)
    # d varia de (1 - n) até (n - 1)
    for d in range(1 - n, n):
        diagonal = []
        for i in range(1, n + 1):
            j = i - d
            if 1 <= j <= n:
                diagonal.append(var(i, j, n))
        
        # combina dois a dois dentro da diagonal
        for p in range(len(diagonal)):
            for q in range(p + 1, len(diagonal)):
                clausulas.append([-diagonal[p], -diagonal[q]])

    # no máximo uma por diagonal secundária (i + j = constante d)
    # d varia de 2 até 2n
    for d in range(2, 2 * n + 1):
        diagonal = []
        for i in range(1, n + 1):
            j = d - i
            if 1 <= j <= n:
                diagonal.append(var(i, j, n))
        
        # combina dois a dois dentro da diagonal
        for p in range(len(diagonal)):
            for q in range(p + 1, len(diagonal)):
                clausulas.append([-diagonal[p], -diagonal[q]])

    return clausulas

def checar_sanidade(n, clausulas):
    """Verifica se o número de variáveis/cláusulas bate com o esperado analiticamente."""
    # fórmulas deduzidas na formalização (aquivo md)
    clausulas_linhas_min = n
    clausulas_linhas_max = n * (n * (n - 1)) // 2
    clausulas_colunas_max = n * (n * (n - 1)) // 2
    
    # somatório de C(L, 2) - contagem das diagonais
    clausulas_diag_princ = 0
    clausulas_diag_sec = 0
    
    # as diagonais crescem de 1 até n e depois decrescem até 1
    for L in range(1, n):
        pares = (L * (L - 1)) // 2
        # multiplica por 2 porque existem nos dois "triângulos" do tabuleiro
        clausulas_diag_princ += 2 * pares
        clausulas_diag_sec += 2 * pares
        
    # soma a diagonal central (que tem tamanho n)
    pares_centro = (n * (n - 1)) // 2
    clausulas_diag_princ += pares_centro
    clausulas_diag_sec += pares_centro

    total_esperado = (clausulas_linhas_min + clausulas_linhas_max + 
                      clausulas_colunas_max + clausulas_diag_princ + clausulas_diag_sec)

    if len(clausulas) != total_esperado:
        # usa stderr para não quebrar o arquivo gerado pelo stdout (>)
        sys.stderr.write(f"ERRO DE SANIDADE: Esperava {total_esperado} cláusulas, mas gerou {len(clausulas)}.\n")
        sys.exit(1)

def escrever_dimacs(n, clausulas):
    # o nº de variáveis é n*n
    print(f"p cnf {n*n} {len(clausulas)}")
    for c in clausulas:
        print(" ".join(map(str, c)) + " 0")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Uso correto: python gerador.py <tamanho_N>\n")
        sys.exit(1)
        
    n = int(sys.argv[1])
    clausulas = gerar_clausulas(n)
    checar_sanidade(n, clausulas)
    escrever_dimacs(n, clausulas)