# Testes de Sanidade Iniciais (SAT Solver)

Nesta etapa, validamos a corretude da modelagem e do gerador DIMACS utilizando o solver **MiniSat**. Foram escolhidas três instâncias clássicas com soluções conhecidas.

## Metodologia
Para cada `N`, o arquivo `.cnf` foi gerado via `python3 gerador.py <N>`. Em seguida, executou-se `minisat rainhas_<N>.cnf saida_<N>.txt`. A solução foi validada visualmente através do script `visualizador.py`.

#### 4 rainhas (minisat)
============================[ Problem Statistics ]=============================
|                                                                             |
|  Number of variables:            16                                         |
|  Number of clauses:              80                                         |
|  Parse time:                   0.00 s                                       |
|  Eliminated clauses:           0.00 Mb                                      |
|  Simplification time:          0.00 s                                       |
|                                                                             |
============================[ Search Statistics ]==============================
| Conflicts |          ORIGINAL         |          LEARNT          | Progress |
|           |    Vars  Clauses Literals |    Limit  Clauses Lit/Cl |          |
===============================================================================
===============================================================================
restarts              : 1
conflicts             : 0              (0 /sec)
decisions             : 5              (0.00 % random) (2253 /sec)
propagations          : 12             (5408 /sec)
conflict literals     : 0              (-nan % deleted)
Memory used           : 11.00 MB
CPU time              : 0.002219 s

SATISFIABLE

´´
==== Solução Encontrada para N=4 ====

  . Q . .
  . . . Q
  Q . . .
  . . Q .

=====================================
´´

#### 6 rainhas (minisat)
============================[ Problem Statistics ]=============================
|                                                                             |
|  Number of variables:            36                                         |
|  Number of clauses:             296                                         |
|  Parse time:                   0.00 s                                       |
|  Eliminated clauses:           0.00 Mb                                      |
|  Simplification time:          0.00 s                                       |
|                                                                             |
============================[ Search Statistics ]==============================
| Conflicts |          ORIGINAL         |          LEARNT          | Progress |
|           |    Vars  Clauses Literals |    Limit  Clauses Lit/Cl |          |
===============================================================================
===============================================================================
restarts              : 1
conflicts             : 4              (inf /sec)
decisions             : 13             (0.00 % random) (inf /sec)
propagations          : 70             (inf /sec)
conflict literals     : 27             (0.00 % deleted)
Memory used           : 11.00 MB
CPU time              : 0 s

SATISFIABLE

´´
==== Solução Encontrada para N=6 ====

  . Q . . . .
  . . . Q . .
  . . . . . Q
  Q . . . . .
  . . Q . . .
  . . . . Q .

=====================================
´´

#### 8 rainhas (minisat)
============================[ Problem Statistics ]=============================
|                                                                             |
|  Number of variables:            64                                         |
|  Number of clauses:             736                                         |
|  Parse time:                   0.00 s                                       |
|  Eliminated clauses:           0.00 Mb                                      |
|  Simplification time:          0.00 s                                       |
|                                                                             |
============================[ Search Statistics ]==============================
| Conflicts |          ORIGINAL         |          LEARNT          | Progress |
|           |    Vars  Clauses Literals |    Limit  Clauses Lit/Cl |          |
===============================================================================
===============================================================================
restarts              : 1
conflicts             : 2              (2646 /sec)
decisions             : 18             (0.00 % random) (23810 /sec)
propagations          : 73             (96561 /sec)
conflict literals     : 19             (26.92 % deleted)
Memory used           : 11.00 MB
CPU time              : 0.000756 s

SATISFIABLE

´´
==== Solução Encontrada para N=8 ====

  . . . . Q . . .
  . Q . . . . . .
  . . . Q . . . .
  . . . . . Q . .
  . . . . . . . Q
  . . Q . . . . .
  Q . . . . . . .
  . . . . . . Q .

=====================================
´´