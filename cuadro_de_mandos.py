import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Cargar los datos de crecimiento del PIB
# Leer los datos del archivo Excel
file_path = 'datos_crecimiento.xlsx'
data_crecimiento = pd.read_excel(file_path, sheet_name='Data')

# Calcular la diferencia entre el crecimiento del mercado de noticias digitales y el crecimiento del PIB
data_crecimiento['Diferencia Crecimiento (%)'] = data_crecimiento['Crecimiento del mercado de suscripciones digitales (%)'] - data_crecimiento['Crecimiento del PIB de España (%)']

# Calcular la variación del crecimiento
crecimiento_actual = data_crecimiento['Diferencia Crecimiento (%)'].iloc[1]
crecimiento_anterior = data_crecimiento['Diferencia Crecimiento (%)'].iloc[0]
variacion_crecimiento = crecimiento_actual - crecimiento_anterior
flecha_crecimiento = '↑' if variacion_crecimiento > 0 else '↓' if variacion_crecimiento < 0 else '→'

### Paso 2: Cargar y Procesar los Datos de Seguimiento de los Medios

# Cargar los datos de seguimiento de medios
file_path_seguimiento_medios = 'datos_seguimiento_medios.xlsx'
data_seguimiento_medios = pd.read_excel(file_path_seguimiento_medios)

# Calcular los totales
total_trafico = data_seguimiento_medios['Tráfico orgánico para el medio'].sum()
total_coste = data_seguimiento_medios['Coste por sus fuentes'].sum()

### Paso 3: Cargar y Procesar los Datos de Acceso a Noticias

# Cargar los datos de acceso a noticias
file_path_acceso = 'data-ExyBd.csv'
data_acceso = pd.read_csv(file_path_acceso)

# Calcular la variación del acceso
acceso_actual_directo = data_acceso['Direct access to news websites/apps'].iloc[-1]
acceso_anterior_directo = data_acceso['Direct access to news websites/apps'].iloc[-2]
variacion_acceso_directo = acceso_actual_directo - acceso_anterior_directo
flecha_acceso_directo = '↑' if variacion_acceso_directo > 0 else '↓' if variacion_acceso_directo < 0 else '→'

acceso_actual_redes = data_acceso['Social media access'].iloc[-1]
acceso_anterior_redes = data_acceso['Social media access'].iloc[-2]
variacion_acceso_redes = acceso_actual_redes - acceso_anterior_redes
flecha_acceso_redes = '↑' if variacion_acceso_redes > 0 else '↓' if variacion_acceso_redes < 0 else '→'

### Paso 4: Cargar y Procesar los Datos del NPS

# Cargar los datos del NPS
file_path_encuesta = 'encuesta_realizada_online_Factify.xlsx'
df_encuesta = pd.read_excel(file_path_encuesta)

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
df_respuestas['Segmento'] = pd.cut(df_respuestas['Valor'], bins=[-1, 1, 2, 3, 4, 5], labels=['Detractores', 'Detractores', 'Pasivos', 'Pasivos', 'Promotores'], ordered=False)

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

### Paso 5: Visualizar todos los KPIs

def plot_kpis():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.axis('off')

    # Crecimiento
    ax.text(0.5, 0.9, f'Crecimiento del PIB: {crecimiento_actual:.2f}% {flecha_crecimiento}', ha='center', fontsize=12, fontweight='bold')

    # Seguimiento de medios
    ax.text(0.5, 0.75, f'Total Tráfico Generado: {total_trafico:.0f}', ha='center', fontsize=12)
    ax.text(0.5, 0.7, f'Total Coste: €{total_coste:.2f}', ha='center', fontsize=12)

    # Acceso a noticias
    ax.text(0.5, 0.55, f'Acceso directo: {acceso_actual_directo:.2f}% {flecha_acceso_directo}', ha='center', fontsize=12)
    ax.text(0.5, 0.5, f'Acceso a través de redes sociales: {acceso_actual_redes:.2f}% {flecha_acceso_redes}', ha='center', fontsize=12)

    # NPS
    ax.text(0.5, 0.35, f'NPS Actual: {nps_score:.2f} {flecha_nps}', ha='center', fontsize=12, fontweight='bold')

    plt.show()

if __name__ == "__main__":
    plot_kpis()
