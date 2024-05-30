import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Cargar los datos del archivo Excel
file_path = 'datos_cuota_de_mercado.xlsx'
data_suscripciones = pd.read_excel(file_path, sheet_name='Datos suscripciones')

# Seleccionar las columnas relevantes y eliminar filas con valores faltantes
data_clean = data_suscripciones[['Periódico', 'Número de suscriptores 2024', 'Precio de la suscripción 2024']].dropna()

# Seleccionar las columnas para el clustering
X = data_clean[['Número de suscriptores 2024', 'Precio de la suscripción 2024']]

# Aplicar el método de Ward para el análisis de clustering jerárquico
Z = linkage(X, method='ward')

# Crear el dendrograma
plt.figure(figsize=(10, 7))
dendrogram(Z, labels=data_clean['Periódico'].values, leaf_rotation=90, leaf_font_size=10)
plt.title('Dendrograma de Clustering Jerárquico (Método de Ward)')
plt.xlabel('Periódico')
plt.ylabel('Distancia Euclidiana')
plt.tight_layout()
plt.show()