import sys

def visualizar(arquivo_saida, n):
    try:
        with open(arquivo_saida, 'r') as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print(f"Erro: Arquivo {arquivo_saida} não encontrado.")
        return

    is_sat = False
    variaveis = []

    for linha in linhas:
        linha = linha.strip()
        
        # ignora linhas de comentários ou estatísticas dos solvers
        if linha.startswith('c '):
            continue
            
        # verifica se é SAT (suporta formato MiniSat e Formato Competição)
        if linha == "SAT" or linha == "s SATISFIABLE":
            is_sat = True
        elif linha == "UNSAT" or linha == "s UNSATISFIABLE":
            print("O resultado é UNSAT (Insatisfatível).")
            return
            
        # se SAT, começa a coletar as variáveis
        elif is_sat:
            # remove o prefixo 'v ' usado no kissat/cadical
            if linha.startswith('v '):
                linha = linha[2:]
            
            # pega os pedaços da linha e converte pra inteiro
            partes = linha.split()
            for p in partes:
                try:
                    val = int(p)
                    if val == 0:
                        break # o número 0 indica o fim do modelo
                    variaveis.append(val)
                except ValueError:
                    continue

    if not is_sat or not variaveis:
        print("Erro: Não foi possível encontrar a solução SAT no arquivo.")
        return

    positivas = [v for v in variaveis if v > 0]
    
    tabuleiro = [["." for _ in range(n)] for _ in range(n)]
    
    for v in positivas:
        # reverte v = N * (i - 1) + j
        linha = (v - 1) // n
        coluna = (v - 1) % n
        tabuleiro[linha][coluna] = "Q"
        
    print(f"\n==== Solução encontrada para N = {n} ====\n")
    for linha in tabuleiro:
        print("  " + " ".join(linha))
    print("\n" + "=" * 39 + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso correto: python3 visualizador.py <arquivo_saida_solver.txt> <N>")
    else:
        visualizar(sys.argv[1], int(sys.argv[2]))