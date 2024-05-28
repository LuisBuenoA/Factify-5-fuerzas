import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo Excel
file_path = 'datos_cuota_de_mercado.xlsx'
data_suscripciones = pd.read_excel(file_path, sheet_name='Datos suscripciones')

# Eliminar filas con valores nulos en la columna 'Número de suscriptores 2024' y 'Precio de la suscripción 2024'
data_suscripciones_clean = data_suscripciones.dropna(subset=['Número de suscriptores 2024', 'Precio de la suscripción 2024'])

# Filtrar datos relevantes
perio_clean = data_suscripciones_clean['Periódico']
num_suscriptores_clean = data_suscripciones_clean['Número de suscriptores 2024'].astype(int)
precio_suscripcion = data_suscripciones_clean['Precio de la suscripción 2024']

# Calcular el valor total de las suscripciones (número de suscriptores * precio de la suscripción)
valor_suscripciones = num_suscriptores_clean * precio_suscripcion

# Calcular el valor total de todas las suscripciones
total_valor_suscripciones = valor_suscripciones.sum()

# Crear la gráfica de cuota de mercado
plt.figure(figsize=(10, 6))
plt.pie(valor_suscripciones, labels=perio_clean, autopct='%1.1f%%', startangle=140)
plt.title('Cuota de Mercado de Suscripciones en 2024 (en euros)')

# Añadir el valor total de suscriptores en euros
plt.annotate(f'Total valor suscripciones: €{total_valor_suscripciones:,.2f}', 
             xy=(0.5, 0.5), xytext=(0, 0.8),
             textcoords='axes fraction', ha='center', fontsize=12)

plt.axis('equal')  # Asegurar que el gráfico sea un círculo

# Mostrar la gráfica
plt.show()
