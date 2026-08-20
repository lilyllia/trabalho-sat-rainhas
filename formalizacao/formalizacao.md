# 2. Formalização Matemática

O problema escolhido para a formalização foi o das N-Rainhas. Conforme as diretrizes do trabalho, esta seção define o conjunto de variáveis e sua codificação. Além disso, descreve cada família de cláusulas em FNC com suas justificativas e apresenta o número total de variáveis e cláusulas em função da instância. A modelagem foi analisada primeiramente em uma instância de tamanho N=4 para validar a estrutura antes de sua generalização.

## 2.1. Variáveis Proposicionais
Para representar as posições no tabuleiro $N \times N$, a definição das variáveis é feita da seguinte maneira:
* Definimos $x_{i,j}$ = "há uma rainha na linha $i$, coluna $j$", onde $i, j \in \{1, \dots, N\}$.
* **Codificação linear:** Como os SAT solvers operam com índices unidimensionais positivos, mapeamos a matriz bidimensional em um número inteiro único através da fórmula de codificação: `var(i,j) = N · (i - 1) + j`.

## 2.2. Famílias de Cláusulas em CNF
As restrições do problema das N-Rainhas foram divididas em famílias nomeadas. Para cada uma, detalhamos a cláusula genérica correspondente e a justificativa de necessidade e suficiência.

### "Ao menos uma por linha"
* **Cláusula genérica:** Para cada linha $i \in \{1, \dots, N\}$: `(x_{i,1} ∨ x_{i,2} ∨ ... ∨ x_{i,N})`
* **Justificativa:** Esta restrição é necessária para garantir que nenhuma linha do tabuleiro fique vazia. Sem ela, um tabuleiro sem nenhuma rainha seria considerado válido pelo solver.

### "No máximo uma por linha"
* **Cláusula genérica:** Para cada linha $i \in \{1, \dots, N\}$ e para todo par de colunas $j < k$: `(¬x_{i,j} ∨ ¬x_{i,k})`
* **Justificativa:** Previne que duas ou mais rainhas dividam a mesma linha. Quando combinada à regra de "ao menos uma por linha", torna-se suficiente para garantir que exista exatamente uma rainha ocupando cada linha, garantindo o total de $N$ rainhas no tabuleiro final.

### "No máximo uma por coluna"
* **Cláusula genérica:** Para cada coluna $j \in \{1, \dots, N\}$ e para todo par de linhas $i < k$: `(¬x_{i,j} ∨ ¬x_{k,j})`
* **Justificativa:** Captura a restrição vertical do xadrez, sendo necessária para assegurar que duas rainhas nunca se ataquem através de uma mesma coluna. 

### "No máximo uma por diagonal principal"
* **Cláusula genérica:** Agrupando as variáveis pela constante de diagonal descendente `d = i - j`. Para cada grupo $d$, consideram-se todos os pares de coordenadas distintas pertencentes a este grupo: `(¬x_{i,j} ∨ ¬x_{k,l})`
* **Justificativa:** Diagonais principais (↘) são caracterizadas pela mesma diferença entre o índice da linha e da coluna. Esta família de cláusulas impede que as rainhas ataquem umas às outras nesses eixos inclinados.

### "No máximo uma por diagonal secundária"
* **Cláusula genérica:** Agrupando as variáveis pela constante de diagonal ascendente `d = i + j`. Para cada grupo $d$, consideram-se todos os pares distintos pertencentes a este grupo: `(¬x_{i,j} ∨ ¬x_{k,l})`
* **Justificativa:** Diagonais secundárias (↗) possuem a mesma soma dos índices de linha e coluna. Esta cláusula é necessária para bloquear ataques diagonais ascendentes, complementando todas as direções de ataque válidas no xadrez.

## 2.3. Contagem
Abaixo expressamos os cálculos de dimensionamento do problema em função do parâmetro $N$.

* **Total de Variáveis:** O tabuleiro possui $N$ linhas e $N$ colunas, resultando em **$N^2$** variáveis.
* **Cláusulas "ao menos uma por linha":** Uma única cláusula restritiva para cada linha, resultando em **$N$** cláusulas.
* **Cláusulas "no máximo uma por linha":** Para cada uma das $N$ linhas, formamos pares entre as $N$ colunas disponíveis, totalizando: `N · C(N,2) = N · N · (N - 1) / 2` cláusulas.
* **Cláusulas "no máximo uma por coluna":** Utilizando a simetria com as linhas, para cada uma das $N$ colunas avaliamos os pares entre as linhas: `N · C(N,2) = N · N · (N - 1) / 2` cláusulas.
* **Cláusulas de diagonais:** Em um tabuleiro $N \times N$, existem $2N - 1$ diagonais em cada direção (principais e secundárias). Para uma diagonal específica de comprimento $L$ (onde $L$ varia de 1 até $N$ e retrocede a 1), existem `C(L,2)` pares de "no máximo um". A contagem total será a **soma de `C(L,2)` computada sobre todas as diagonais**.