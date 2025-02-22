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