# Análise Estrutural da Malha Viária de Jucurutu, RN

## Identificação da Região
**Região Analisada:** Jucurutu, Rio Grande do Norte, Brasil.
Jucurutu é um município no interior do Rio Grande do Norte, caracterizado por ser cortado pelo Rio Piranhas-Açu, o que cria gargalos naturais de mobilidade (como pontes e vias de acesso principais).

## Vídeo de Apresentação
[Link do Vídeo no Loom](#) *(Inserir link do vídeo aqui)*

## Objetivo do Trabalho
O objetivo deste trabalho é aplicar conceitos de teoria dos grafos em uma rede real, interpretando a malha viária da cidade de Jucurutu como um grafo. A proposta busca identificar nós centrais (hubs), regiões estruturalmente densas (k-core) e pontos críticos de conexão (betweenness), indo além da execução de código para obter uma interpretação crítica urbana.

## Metodologia
1. **Extração de Dados:** A rede viária foi extraída do OpenStreetMap utilizando a biblioteca Python **OSMnx**, configurada para capturar ruas que permitem o tráfego de veículos (`network_type="drive"`).
2. **Construção do Grafo:** O grafo resultante possui cruzamentos como nós e trechos de ruas como arestas. Para garantir a corretude algorítmica, o grafo foi convertido para uma versão simples e não direcionada.
3. **Cálculo de Métricas:** Através do **NetworkX**, calculamos métricas de centralidade, grau e decomposição estrutural.
4. **Exportação e Visualização:** O grafo com seus atributos foi exportado no formato `.graphml` para ser importado e visualizado de forma geográfica e estrutural com o **Gephi**.

## Métricas Calculadas
Foram extraídos 963 nós e 1.278 arestas (no grafo simples não-direcionado). As métricas analisadas incluem:
* **Grau e Distribuição de Grau:** Quantidade de ruas conectadas a cada cruzamento.
* **Betweenness Centrality (Centralidade de Intermediação):** Identificação de gargalos na rede viária.
* **Closeness Centrality (Centralidade de Proximidade):** O quão rápido é possível alcançar qualquer outro nó a partir de um cruzamento.
* **K-Core Decomposition:** Identificação das áreas mais densas da rede, com foco no núcleo principal (k=2).

## Principais Visualizações
* *Distribuição de Grau:* Gráfico de barras indicando que a grande maioria dos nós possui grau 1 (ruas sem saída) ou 3 (cruzamentos em T).
* *Gargalos da Rede:* Visualização geográfica destacando os nós com maior Betweenness, indicando as vias de acesso essenciais.
* *Decomposição K-Core:* Visualização da remoção das franjas da rede, mantendo apenas o núcleo viário.

## Respostas às Questões Obrigatórias

**1. Os nós com maior grau coincidem com os nós de maior betweenness?**
Não. Os nós com maior grau (hubs de grau 4 ou 5) são cruzamentos com muitas conexões locais, mas não necessariamente as vias mais vitais para cruzar a cidade. Já os nós com maior betweenness costumam ter graus menores (como 2 ou 3), mas atuam como pontes vitais entre regiões inteiras da cidade.

**2. O núcleo identificado pelo k-core coincide com os principais hubs?**
O *main core* (neste caso, k=2) engloba 676 dos 963 nós da rede. Os principais hubs estão contidos dentro desse núcleo, mas o k-core abrange uma área muito mais vasta que apenas os hubs, servindo essencialmente para filtrar as "franjas" da rede (ruas sem saída com k=1, que são 287 nós).

**3. O que a métrica de betweenness revela que o grau não revela?**
O grau revela apenas a conectividade **local** (quantas vias chegam àquele cruzamento específico). O betweenness revela a importância **global** do nó. Um nó de betweenness alto é um corredor de fluxo crítico; se ele for bloqueado, o tráfego da cidade inteira pode ser forçado a fazer longos desvios.

**4. O que muda quando a rede é analisada em sua posição geográfica real e quando é analisada por um layout estrutural?**
A análise geográfica mantém a fidelidade física: distâncias, rios e formatos de quadras limitam a visualização. O layout estrutural (como o ForceAtlas2 no Gephi) ignora o espaço físico e agrupa os nós puramente pela densidade de conexões. Vias que formam comunidades fortes se aproximam no centro visual, enquanto ruas isoladas são empurradas para a periferia da imagem, revelando o "esqueleto topológico" da malha.

**5. Existem regiões críticas para mobilidade urbana na área analisada?**
Sim. Os dados mostram nós com uma centralidade de intermediação (betweenness) excepcionalmente alta (entre 0.35 e 0.46), o que significa que até 46% dos caminhos mais curtos da cidade passam por um único ponto. Isso indica fortíssimos gargalos, muito provavelmente relacionados às pontes sobre o Rio Piranhas e à Rodovia BR-226 que corta a região.

**6. A rede parece homogênea ou apresenta concentração estrutural?**
A rede apresenta forte concentração estrutural e dependência de poucos caminhos. O fato do betweenness máximo chegar a ~0.46 revela que a rede está longe de ser homogênea em relação ao fluxo. Além disso, a presença de quase 30% da rede como nós de k=1 aponta muitas ramificações periféricas ou ruas sem saída ao redor do núcleo conectado.

**7. Os resultados obtidos fazem sentido considerando o conhecimento urbano da região escolhida?**
Sim, fazem todo o sentido. Cidades do interior cortadas por acidentes geográficos severos (como o Rio Piranhas em Jucurutu) tendem a apresentar poucos pontos de travessia. Esses cruzamentos ou rodovias de ligação absorvem quase todo o tráfego em viagens longas, o que se reflete matematicamente nos altos valores de Betweenness identificados pela análise.

## Principais Conclusões
O uso de métricas de grafos permitiu identificar matematicamente o que a intuição sobre a cidade sugere: Jucurutu possui uma malha viária fortemente dependente de um pequeno conjunto de vias de ligação. O planejamento urbano deve observar com atenção esses cruzamentos de alta centralidade de intermediação, pois acidentes ou interdições nestes nós causam um impacto muito maior à mobilidade do município do que em qualquer outro local da malha.
