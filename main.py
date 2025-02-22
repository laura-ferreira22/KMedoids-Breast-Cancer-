#Carregar bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn_extra.cluster import KMedoids

# Carregar o dataset Breast Cancer
breast_cancer = load_breast_cancer()