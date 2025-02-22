# K-Medoids Clustering no Dataset Breast Cancer

## Descrição
Este projeto aplica o algoritmo de clusterização **K-Medoids** ao dataset **Breast Cancer** da biblioteca `sklearn`. O objetivo é agrupar os dados utilizando duas características: `mean radius` e `mean symmetry`. Além disso, o método Elbow é utilizado para determinar o número ideal de clusters.

Esta atividade foi realizada como parte de um curso de **Machine Learning (ML)**.

## Instalação
Antes de executar o código, é necessário instalar a biblioteca `scikit-learn-extra`:
```bash
!pip install scikit-learn-extra
```

## Bibliotecas Utilizadas
- `numpy`
- `matplotlib`
- `sklearn.datasets`
- `sklearn_extra.cluster`

## Etapas do Código
1. **Carregar o dataset Breast Cancer**
2. **Selecionar características** (`mean radius` e `mean symmetry`)
3. **Visualizar os dados originais**
4. **Calcular WCSS para diferentes valores de clusters**
5. **Determinar o número ideal de clusters pelo método Elbow**
6. **Aplicar o algoritmo K-Medoids**
7. **Visualizar os clusters e os medoids**

## Resultados Esperados
- Um gráfico mostrando os dados originais antes da clusterização.
- O gráfico do método Elbow para ajudar a definir o número ideal de clusters.
- Um gráfico final exibindo os clusters formados pelo algoritmo K-Medoids.

## Como Executar
1. Instale as dependências.
2. Copie e cole o código em um ambiente Python compatível (Jupyter Notebook, Google Colab, etc.).
3. Execute as células sequencialmente.

## Exemplo de Saída
A saída incluirá três gráficos:
1. **Dados Originais**
2. **Método Elbow** para escolher o número ideal de clusters.
3. **Dados Agrupados com K-Medoids** indicando os clusters e os medoids.

## Observação
Este projeto é uma atividade educacional e pode ser aprimorado com outras técnicas de clusterização e análise dos resultados.
