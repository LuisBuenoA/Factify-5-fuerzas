import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo Excel
file_path = 'encuesta_realizada_online_Factify.xlsx'
df_encuesta = pd.read_excel(file_path)

# Asumir que la columna con las respuestas se llama 'Respuesta'
respuestas = df_encuesta['¿Cuánto valor le darías a una plataforma que recopila y compara noticias de distintas fuentes?'].tolist()

# Asignar valores numéricos a las respuestas
valores = {
    "Nada": 0,
    "Poco": 1,
    "Algo": 2,
    "Bastante": 3,
    "Mucho": 4
}

# Convertir respuestas a valores numéricos
valores_respuestas = [valores[respuesta] for respuesta in respuestas]

# Crear DataFrame
df_respuestas = pd.DataFrame(valores_respuestas, columns=["Valor"])

# Categorizar respuestas
df_respuestas['Segmento'] = pd.cut(df_respuestas['Valor'], bins=[-1, 1, 2, 3, 4, 5], labels=['Detractores', 'Detractores', 'Pasivos', 'Promotores', 'Promotores'], ordered=False)

# Contar respuestas por segmento y reordenar
segmentos = df_respuestas['Segmento'].value_counts().reindex(['Detractores', 'Pasivos', 'Promotores'])

# Calcular NPS
promotores = segmentos['Promotores']
detractores = segmentos['Detractores']
total_respuestas = len(respuestas)
nps_score = ((promotores - detractores) / total_respuestas) * 100

print(f'NPS Score: {nps_score}')

# Crear la gráfica del estudio NPS
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(segmentos.index, segmentos.values, color=['red', 'gray', 'green'])

# Añadir etiquetas y título
ax.set_xlabel('Segmento')
ax.set_ylabel('Número de Respuestas')
ax.set_title('Estudio NPS de Factify')
plt.tight_layout()

# Mostrar la gráfica
plt.show()
