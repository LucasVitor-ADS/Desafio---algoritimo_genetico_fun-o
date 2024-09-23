# Algoritmo Genético para Minimização de Função \( f(x) = x^3 - 6x + 14 \)

## Descrição Geral

Este projeto implementa um **algoritmo genético** para encontrar o valor de \( x \) que minimiza a função \( f(x) = x^3 - 6x + 14 \), considerando \( x \) dentro do intervalo \([-10, 10]\). O algoritmo utiliza várias técnicas como mutação, crossover e elitismo para simular a evolução natural e encontrar a solução mais próxima do mínimo global da função.

### Funcionamento do Algoritmo

O **algoritmo genético** simula o processo de evolução natural para resolver problemas de otimização. Ele começa com uma população inicial de possíveis soluções, que são representadas como cromossomos binários. A cada geração, novos indivíduos são criados por meio de crossover e mutação, e os indivíduos mais "aptos" são selecionados para sobreviver e gerar a próxima geração.

Os principais componentes do algoritmo são:

1. **Codificação**: Cada valor de \( x \) é representado por um vetor binário. A transformação de binário para real é feita para garantir que o valor de \( x \) permaneça dentro do intervalo definido.
   
2. **Fitness**: A função \( f(x) = x^3 - 6x + 14 \) é utilizada para avaliar a aptidão de cada cromossomo. Como estamos minimizando a função, o fitness é o valor negativo da função \( f(x) \), ou seja, valores menores de \( f(x) \) representam cromossomos melhores.

3. **Crossover**: Ocorre o cruzamento de dois cromossomos (pais) para gerar novos cromossomos (filhos). Neste caso, é usado um crossover de um ponto, onde um ponto de corte é escolhido aleatoriamente e a troca de material genético acontece a partir desse ponto.

4. **Mutação**: A mutação inverte aleatoriamente bits do cromossomo com uma determinada probabilidade (taxa de mutação), introduzindo variações na população.

5. **Seleção**: Utilizamos a técnica de seleção por torneio, onde um conjunto de indivíduos é selecionado aleatoriamente da população, e o indivíduo com o melhor fitness é escolhido para reprodução.

6. **Elitismo**: Uma porcentagem da melhor parte da população é mantida para garantir que as boas soluções não sejam perdidas a cada geração.

## Estrutura do Código

### Funções Principais

- **`funcao(x)`**: A função que queremos minimizar, \( f(x) = x^3 - 6x + 14 \).
- **`binario_para_real(binario, min_x, max_x)`**: Converte um cromossomo binário em um valor real na faixa \([-10, 10]\).
- **`criar_individuo(tamanho_cromossomo)`**: Cria um cromossomo binário aleatório.
- **`avaliar_individuo(individuo, min_x, max_x)`**: Avalia o fitness de um cromossomo, que é a função \( f(x) \) transformada para maximização.
- **`torneio(populacao, scores, k=3)`**: Realiza a seleção por torneio, escolhendo o melhor de um grupo aleatório.
- **`crossover(pai1, pai2, ponto_de_corte=None)`**: Realiza o crossover de um ponto entre dois pais.
- **`mutacao(individuo, taxa_mutacao)`**: Realiza a mutação nos cromossomos, invertendo bits com uma certa probabilidade.
- **`algoritmo_genetico(...)`**: Implementa o algoritmo genético, gerando novas populações ao longo de várias gerações.

## Como Executar

### Pré-requisitos

Para rodar este código, você precisará de **Python 3.8+** e a biblioteca **numpy**. Instale as dependências executando o seguinte comando no terminal:

```bash
pip install numpy

