#Carregar bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn_extra.cluster import KMedoids

# Carregar o dataset Breast Cancer
breast_cancer = load_breast_cancer()

# Exibir características
breast_cancer.feature_names

#Exibir rótulos
breast_cancer.target_names

#Escolhe duas características do dataset, colunas 0 e 8 ('mean radius' e 'mean symmetry')
X = breast_cancer.data[:,[0,8]]

#Exibir os dados (primeiras 5 linhas)
X[:5]


# Gráfico dos dados antes da clusterização
plt.figure(figsize=(8,6))
plt.scatter(X[:,0],X[:,1],s=50)
plt.title("Dados Originais")
plt.xlabel(breast_cancer.feature_names[0])
plt.ylabel(breast_cancer.feature_names[8])
plt.show()

# Função para calcular WCSS
def calcular_wcss(X, k_max):
  wcss=[]
  for k in range (1, k_max + 1):
    kmedoids = KMedoids(n_clusters = k, random_state = 42)
    kmedoids.fit(X)
    wcss.append(kmedoids.inertia_)
  return wcss

# Definir o número máximo de clusters para testar
k_max = 10

# Calcular WCSS para diferentes valores de k
wcss = calcular_wcss(X, k_max)


# Plotar o gráfico de cotovelo
plt.figure(figsize=(8,6))
plt.plot(range(1, k_max+1), wcss, marker ='o', linestyle = '--')
plt.title("Método Elbow para determinar o número ideal de Clusters")
plt.xlabel("Número de clusters (k)")
plt.ylabel("Soma dos quadrados dentr do cluster (wcss)")
plt.grid(True)
plt.show()


# Identificar o número ideal de clusters pelo método Elbow
# Vamos assumir que o cotovelo está em k=3

optimal_k =3
# Aplicar K-Medoids com o número ideal de clusters

kmedoids = KMedoids(n_clusters = optimal_k, random_state=42)
kmedoids.fit(X)


#Obter os rótulos dos clusters e os medoids
labels = kmedoids.labels_
medoids= kmedoids.cluster_centers_


# Gráfico dos dados após a clusterização
plt.figure(figsize=(8,6))
plt.scatter(X[:,0],X[:,1], c=labels,s=50, cmap='viridis')
plt.scatter(medoids[:,0],medoids[:,1],c ="red", marker='X',s=200,alpha=0.75)
plt.title(f"Dados agrupados com K-medoids(k={optimal_k})")
plt.xlabel(breast_cancer.feature_names[0])
plt.ylabel(breast_cancer.feature_names[8])
plt.show()