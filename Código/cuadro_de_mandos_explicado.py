import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Cargar los datos de crecimiento del PIB
# Leer los datos del archivo Excel
file_path = 'Data\datos_crecimiento.xlsx'
data_crecimiento = pd.read_excel(file_path, sheet_name='Data')

# Calcular la diferencia entre el crecimiento del mercado de noticias digitales y el crecimiento del PIB
data_crecimiento['Diferencia Crecimiento (%)'] = data_crecimiento['Crecimiento del mercado de suscripciones digitales (%)'] - data_crecimiento['Crecimiento del PIB de España (%)']

# Calcular la variación del crecimiento
crecimiento_actual = data_crecimiento['Diferencia Crecimiento (%)'].iloc[1]
crecimiento_anterior = data_crecimiento['Diferencia Crecimiento (%)'].iloc[0]
variacion_crecimiento = crecimiento_actual - crecimiento_anterior
flecha_crecimiento = '↑' if variacion_crecimiento > 0 else '↓' if variacion_crecimiento < 0 else '→'
color_flecha_crecimiento = 'darkgreen' if variacion_crecimiento > 0 else 'darkred' if variacion_crecimiento < 0 else 'black'

### Paso 2: Cargar y Procesar los Datos de Seguimiento de los Medios

# Cargar los datos de seguimiento de medios
file_path_seguimiento_medios = 'Data\datos_seguimiento_medios.xlsx'
data_seguimiento_medios = pd.read_excel(file_path_seguimiento_medios)

# Calcular los totales
total_trafico = data_seguimiento_medios['Tráfico orgánico para el medio'].sum()
total_coste = data_seguimiento_medios['Coste por sus fuentes'].sum()

# Formatear los valores con comas
total_trafico_formatted = f"{total_trafico:,.2f}"
total_coste_formatted = f"{total_coste:,.2f}"

### Paso 3: Cargar y Procesar los Datos de Acceso a Noticias

# Cargar los datos de acceso a noticias
file_path_acceso = 'Data\data-ExyBd.csv'
data_acceso = pd.read_csv(file_path_acceso)

# Calcular la variación del acceso
acceso_actual_directo = data_acceso['Direct access to news websites/apps'].iloc[-1]
acceso_anterior_directo = data_acceso['Direct access to news websites/apps'].iloc[-2]
variacion_acceso_directo = acceso_actual_directo - acceso_anterior_directo
flecha_acceso_directo = '↑' if variacion_acceso_directo > 0 else '↓' if variacion_acceso_directo < 0 else '→'
color_flecha_acceso_directo = 'darkgreen' if variacion_acceso_directo > 0 else 'darkred' if variacion_acceso_directo < 0 else 'black'

acceso_actual_redes = data_acceso['Social media access'].iloc[-1]
acceso_anterior_redes = data_acceso['Social media access'].iloc[-2]
variacion_acceso_redes = acceso_actual_redes - acceso_anterior_redes
flecha_acceso_redes = '↑' if variacion_acceso_redes > 0 else '↓' if variacion_acceso_redes < 0 else '→'
color_flecha_acceso_redes = 'darkgreen' if variacion_acceso_redes > 0 else 'darkred' if variacion_acceso_redes < 0 else 'black'

### Paso 4: Cargar y Procesar los Datos del NPS

# Cargar los datos
file_path = 'Data\encuesta_realizada_online_Factify.xlsx'
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

# Supongamos que tenemos el NPS anterior
nps_anterior = 30
variacion_nps = nps_score - nps_anterior
flecha_nps = '↑' if variacion_nps > 0 else '↓' if variacion_nps < 0 else '→'
color_flecha_nps = 'darkgreen' if variacion_nps > 0 else 'darkred' if variacion_nps < 0 else 'black'

# Paso 5: Cargar los resultados del clustering
file_path_clustering = 'Data/resultados_clustering.xlsx'
data_clustering = pd.read_excel(file_path_clustering)

# Calcular el número de grupos y la puntuación de silhouette
num_grupos = data_clustering['Cluster'].nunique()
X = data_clustering[['Número de suscriptores 2024', 'Precio de la suscripción 2024']]

# Normalizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

puntuacion_silhouette = silhouette_score(X_scaled, data_clustering['Cluster'])

# Paso 6: Visualizar todos los KPIs
def plot_kpis():
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.axis('off')
    
    # Configuración de las posiciones de los recuadros
    x_positions = [0.05, 0.35, 0.65]
    y_positions = [0.85, 0.65, 0.75, 0.45]
    heights = 0.15

    # Crecimiento del mercado
    ax.add_patch(patches.Rectangle((x_positions[0], y_positions[2]), 0.3, heights, fill=False, edgecolor='black', lw=1))
    ax.text(x_positions[0] + 0.15, y_positions[2] + heights - 0.03, 'Crecimiento del mercado*', ha='center', va='center', fontsize=16, fontweight='bold')
    ax.text(x_positions[0] + 0.15, y_positions[2] + heights / 3, f'{crecimiento_actual:.2f}% {flecha_crecimiento}', ha='center', va='center', fontsize=14, fontweight='bold', color=color_flecha_crecimiento)

    # Medios proveedores
    ax.add_patch(patches.Rectangle((x_positions[1], y_positions[0]), 0.3, heights, fill=False, edgecolor='black', lw=1))
    ax.text(x_positions[1] + 0.15, y_positions[0] + heights - 0.03, 'Medios proveedores**', ha='center', va='center', fontsize=16, fontweight='bold')
    ax.text(x_positions[1] + 0.15, y_positions[0] + heights / 3, f'Total Tráfico Generado: €{total_trafico_formatted}', ha='center', fontsize=14)
    ax.text(x_positions[1] + 0.15, y_positions[0] + heights / 3 - 0.03, f'Total Coste: €{total_coste_formatted}', ha='center', fontsize=14)

    # Acceso a noticias
    ax.add_patch(patches.Rectangle((x_positions[1], y_positions[1]), 0.3, heights, fill=False, edgecolor='black', lw=1))
    ax.text(x_positions[1] + 0.15, y_positions[1] + heights - 0.03, 'Acceso a noticias***', ha='center', va='center', fontsize=16, fontweight='bold')
    ax.text(x_positions[1] + 0.15, y_positions[1] + heights / 3, f'Directo: {acceso_actual_directo:.2f}% {flecha_acceso_directo}', ha='center', fontsize=14, color=color_flecha_acceso_directo)
    ax.text(x_positions[1] + 0.15, y_positions[1] + heights / 3 - 0.03, f'Redes sociales: {acceso_actual_redes:.2f}% {flecha_acceso_redes}', ha='center', fontsize=14, color=color_flecha_acceso_redes)

    # NPS
    ax.add_patch(patches.Rectangle((x_positions[2], y_positions[0]), 0.3, heights, fill=False, edgecolor='black', lw=1))
    ax.text(x_positions[2] + 0.15, y_positions[0] + heights - 0.03, 'Lealtad de los clientes****', ha='center', va='center', fontsize=16, fontweight='bold')
    ax.text(x_positions[2] + 0.15, y_positions[0] + heights / 3, f'NPS Actual: {nps_score:.2f} {flecha_nps}', ha='center', fontsize=14, fontweight='bold', color=color_flecha_nps)

    # Número de Grupos y Puntuación de Silhouette
    ax.add_patch(patches.Rectangle((x_positions[2], y_positions[1]), 0.3, heights, fill=False, edgecolor='black', lw=1))
    ax.text(x_positions[2] + 0.15, y_positions[1] + heights - 0.03, 'Agrupación del mercado*****', ha='center', va='center', fontsize=16, fontweight='bold')
    ax.text(x_positions[2] + 0.15, y_positions[1] + heights / 3, f'Número de Grupos: {num_grupos}', ha='center', fontsize=14, fontweight='bold')
    ax.text(x_positions[2] + 0.15, y_positions[1] + heights / 3 - 0.03, f'Silhouette: {puntuacion_silhouette:.2f}', ha='center', fontsize=14, fontweight='bold')

    # Leyendas
    leyendas = [
        "* Diferencia del mercado de noticias digital y el PIB español",
        "** Suma del coste de proveernos de noticias con medios, teniendo en cuenta el beneficio que generamos a los periódicos con el tráfico orgánico que reciben",
        "*** No tenemos en cuenta la utilización de buscadores, agregadores de noticias u otros accesos, por eso no suma un 100%",
        "**** Encuesta interna de los clientes que recomendarían el producto",
        "***** Número de agrupaciones de competidores hecha con K-means"
    ]
    
    leyendas_y = y_positions[-1] - 0.1  # Posición inicial de las leyendas
    for leyenda in leyendas:
        ax.text(0.05, leyendas_y, leyenda, fontsize=12, va='center')
        leyendas_y -= 0.05

    plt.show()

if __name__ == "__main__":
    plot_kpis()
