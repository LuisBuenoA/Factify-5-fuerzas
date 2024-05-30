import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import seaborn as sns

# Cargar los datos del archivo Excel
file_path = 'datos_cuota_de_mercado.xlsx'
df_suscripciones = pd.read_excel(file_path, sheet_name='Datos suscripciones')

# Eliminar filas con valores nulos en la columna 'Número de suscriptores 2024' y 'Precio de la suscripción 2024'
df_suscripciones = df_suscripciones.dropna(subset=['Número de suscriptores 2024', 'Precio de la suscripción 2024'])

# Seleccionar las columnas relevantes para el análisis
X = df_suscripciones[['Número de suscriptores 2024', 'Precio de la suscripción 2024']]

# Normalizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determinar el número óptimo de clusters usando el método del codo y el coeficiente de silueta
inertia = []
silhouette_scores = []
kmeans_per_k = []

Ks = range(2, 7)

for k in Ks:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    kmeans_per_k.append(kmeans)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, kmeans.labels_))

# Método del codo
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(Ks, inertia, 'bo-')
plt.xlabel('Número de clusters (k)', fontsize=14)
plt.ylabel('Inercia', fontsize=14)
plt.title('Método del codo', fontsize=14)
plt.xticks(Ks)

# Método del coeficiente de silhouette
plt.subplot(1, 2, 2)
plt.plot(Ks, silhouette_scores, 'bo-')
plt.xlabel('Número de clusters (k)', fontsize=14)
plt.ylabel('Silhouette score', fontsize=14)
plt.title('Coeficiente de silhouette', fontsize=14)
plt.tight_layout()
plt.xticks(Ks)
plt.show()

# Basándonos en el gráfico del codo, seleccionamos el número de clusters
n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(X_scaled)

# Obtener las etiquetas de los clusters
labels = kmeans.labels_

# Añadir las etiquetas al dataframe original
df_suscripciones['Cluster'] = labels

# Calcular el coeficiente de silueta
silhouette_avg = silhouette_score(X_scaled, labels)
print(f'Coeficiente de silueta: {silhouette_avg}')

# Visualizar los clusters con nombres de los periódicos
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df_suscripciones, x='Precio de la suscripción 2024', y='Número de suscriptores 2024', hue='Cluster', palette='viridis', s=100)

for i in range(df_suscripciones.shape[0]):
    plt.text(x=df_suscripciones['Precio de la suscripción 2024'][i], y=df_suscripciones['Número de suscriptores 2024'][i], 
             s=df_suscripciones['Periódico'][i], 
             fontdict=dict(color='black', size=10),
             bbox=dict(facecolor='white', alpha=0.5))

plt.title('Clustering del mercado')
plt.xlabel('Precio de la suscripción 2024')
plt.ylabel('Número de suscriptores 2024')
plt.legend(title='Cluster')
plt.tight_layout()
plt.show()

# Guardar los resultados en un archivo Excel
df_suscripciones.to_excel('resultados_clustering.xlsx', index=False)
