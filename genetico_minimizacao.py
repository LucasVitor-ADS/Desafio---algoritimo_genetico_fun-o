import random
import numpy as np

# Função que queremos minimizar
def funcao(x):
    return x**3 - 6*x + 14

# Converte binário para decimal na faixa [-10, 10]
def binario_para_real(binario, min_x, max_x):
    decimal = int(''.join(str(b) for b in binario), 2)
    max_decimal = 2**len(binario) - 1
    return min_x + (decimal / max_decimal) * (max_x - min_x)

# Criação de um indivíduo aleatório (cromossomo binário)
def criar_individuo(tamanho_cromossomo):
    return [random.randint(0, 1) for _ in range(tamanho_cromossomo)]

# Função de avaliação (fitness), inversa da função que queremos minimizar
def avaliar_individuo(individuo, min_x, max_x):
    x = binario_para_real(individuo, min_x, max_x)
    return -funcao(x)  # Queremos minimizar, então usamos negativo

# Seleção por torneio
def torneio(populacao, scores, k=3):
    participantes = random.sample(range(len(populacao)), k)
    melhor = participantes[0]
    for p in participantes[1:]:
        if scores[p] > scores[melhor]:
            melhor = p
    return populacao[melhor]

# Crossover de 1 ponto
def crossover(pai1, pai2, ponto_de_corte=None):
    if ponto_de_corte is None:
        ponto_de_corte = random.randint(1, len(pai1) - 1)
    filho1 = pai1[:ponto_de_corte] + pai2[ponto_de_corte:]
    filho2 = pai2[:ponto_de_corte] + pai1[ponto_de_corte:]
    return filho1, filho2

# Mutação
def mutacao(individuo, taxa_mutacao):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]  # Inverte o bit
    return individuo

# Algoritmo Genético
def algoritmo_genetico(
    tamanho_populacao=10, tamanho_cromossomo=10, taxa_mutacao=0.01,
    num_geracoes=100, min_x=-10, max_x=10, elitismo=True, taxa_elitismo=0.1
):
    # Inicializar população
    populacao = [criar_individuo(tamanho_cromossomo) for _ in range(tamanho_populacao)]
    
    # Executar algoritmo por várias gerações
    for geracao in range(num_geracoes):
        # Avaliar população
        scores = [avaliar_individuo(individuo, min_x, max_x) for individuo in populacao]
        
        # Aplicar elitismo, mantendo os melhores indivíduos
        nova_populacao = []
        if elitismo:
            num_elites = int(taxa_elitismo * tamanho_populacao)
            elites = sorted(zip(scores, populacao), reverse=True)[:num_elites]
            nova_populacao = [ind for _, ind in elites]
        
        # Criar nova geração com crossover e mutação
        while len(nova_populacao) < tamanho_populacao:
            pai1 = torneio(populacao, scores)
            pai2 = torneio(populacao, scores)
            filho1, filho2 = crossover(pai1, pai2)
            filho1 = mutacao(filho1, taxa_mutacao)
            filho2 = mutacao(filho2, taxa_mutacao)
            nova_populacao.append(filho1)
            if len(nova_populacao) < tamanho_populacao:
                nova_populacao.append(filho2)

        # Atualizar a população
        populacao = nova_populacao

    # Avaliar a população final
    scores_finais = [avaliar_individuo(individuo, min_x, max_x) for individuo in populacao]
    melhor_indice = np.argmax(scores_finais)
    melhor_individuo = populacao[melhor_indice]
    melhor_x = binario_para_real(melhor_individuo, min_x, max_x)
    melhor_valor = funcao(melhor_x)
    
    return melhor_x, melhor_valor

# Parâmetros do algoritmo
tamanho_populacao = 10
tamanho_cromossomo = 16  # Resolução do binário para [-10, 10]
taxa_mutacao = 0.01
num_geracoes = 100
min_x = -10
max_x = 10
elitismo = True
taxa_elitismo = 0.1

# Rodar o algoritmo genético
melhor_x, melhor_valor = algoritmo_genetico(
    tamanho_populacao, tamanho_cromossomo, taxa_mutacao, num_geracoes,
    min_x, max_x, elitismo, taxa_elitismo
)

print(f"Melhor x encontrado: {melhor_x}")
print(f"Valor mínimo de f(x): {melhor_valor}")
