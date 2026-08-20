### Introdução, análise complementar e conclusão

- **Introdução:** descrição informal do problema e por que é interessante computacionalmente (N-Rainhas é NP-difícil em generalizações, mas a instância clássica é usada como benchmark clássico de busca combinatória e de solvers desde os anos 1960).

- **Análise complementar pedida pelo professor** comparar a abordagem via SAT com pelo menos duas outras formas clássicas de resolver N-Rainhas:
  - **Backtracking puro** (busca com poda) — complexidade de pior caso, como a poda reduz a árvore de busca.
  - **Programação por restrições / forward checking** (ex.: AC-3) — como a propagação de restrições se compara à unit propagation do SAT solver.
  - Opcional, se sobrar tempo: **busca local / min-conflicts** (Minton et al., famoso por resolver N-Rainhas para N muito grandes rapidamente, ao contrário do SAT/backtracking).
  - O ponto central da comparação: SAT converte o problema em uma busca genérica sobre fórmulas booleanas — vale a pena discutir o que se ganha (reuso de um solver genérico e altamente otimizado) e o que se perde (overhead de codificação, cláusulas redundantes) frente a um algoritmo especializado.

- **Análise e conclusão** (Seção 5 do relatório): usar os dados de teste para discutir se a formalização foi eficiente, se existe formalização alternativa com menos cláusulas (ex.: pensar se dá pra reduzir as cláusulas de "no máximo um" com uma codificação binária em vez de one-hot — não precisa implementar, mas vale discutir), e como a complexidade do problema se relaciona com o desempenho observado.
