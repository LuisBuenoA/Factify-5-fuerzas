import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Cargar los datos del archivo Excel
file_path = 'datos_cuota_de_mercado.xlsx'
data_suscripciones = pd.read_excel(file_path, sheet_name='Datos suscripciones')

# Eliminar filas con valores nulos en las columnas relevantes
data_suscripciones_clean = data_suscripciones.dropna(subset=['Número de suscriptores 2024', 'Precio de la suscripción 2024'])

# Calcular los ingresos totales por suscripciones
data_suscripciones_clean['Ingresos totales'] = data_suscripciones_clean['Número de suscriptores 2024'] * data_suscripciones_clean['Precio de la suscripción 2024']

# Crear la gráfica de sensibilidad de precios (scatter plot)
fig, ax = plt.subplots(figsize=(12, 8))

scatter = ax.scatter(data_suscripciones_clean['Precio de la suscripción 2024'], 
                     data_suscripciones_clean['Número de suscriptores 2024'], 
                     s=data_suscripciones_clean['Ingresos totales']*0.0002,  # Tamaño del punto basado en los ingresos
                     c='blue', alpha=0.6, edgecolors="w", linewidth=0.5, label='Tamaño basado en los ingresos')

# Añadir etiquetas y título
ax.set_xlabel('Precio de la suscripción (€)')
ax.set_ylabel('Número de suscriptores')
ax.set_title('Sensibilidad a los precios de suscripciones de medios')

# Añadir anotaciones para cada punto
for i, row in data_suscripciones_clean.iterrows():
    ax.annotate(row['Periódico'], (row['Precio de la suscripción 2024'], row['Número de suscriptores 2024']),
                textcoords="offset points", xytext=(0,15), ha='center')

# Ajustar una línea de regresión
slope, intercept, r_value, p_value, std_err = stats.linregress(data_suscripciones_clean['Precio de la suscripción 2024'], 
                                                               data_suscripciones_clean['Número de suscriptores 2024'])
regression_line = slope * data_suscripciones_clean['Precio de la suscripción 2024'] + intercept

# Añadir la línea de regresión a la gráfica
ax.plot(data_suscripciones_clean['Precio de la suscripción 2024'], regression_line, color='red', linestyle='--', label='Línea de regresión')

# Añadir la leyenda
ax.legend()

plt.tight_layout()
plt.show()