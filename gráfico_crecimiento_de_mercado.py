import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos del archivo Excel
file_path = 'datos_crecimiento.xlsx'
df = pd.read_excel(file_path, sheet_name='Data')

# Calcular la diferencia entre el crecimiento del mercado de noticias digitales y el crecimiento del PIB
df['Diferencia Crecimiento (%)'] = df['Crecimiento del mercado de suscripciones digitales (%)'] - df['Crecimiento del PIB de España (%)']

# Configurar los colores
colors = []
for value in df['Diferencia Crecimiento (%)']:
    if value > 1:
        colors.append('green')
    elif 0 <= value <= 1:
        colors.append('yellow')
    else:
        colors.append('red')

# Crear la gráfica
plt.figure(figsize=(10, 6))
for i in range(len(df) - 1):
    plt.plot(df['Año'][i:i+2], df['Diferencia Crecimiento (%)'][i:i+2], marker='o', color=colors[i])
plt.xlabel('Año')
plt.ylabel('Diferencia de Crecimiento (%)')
plt.title('Diferencia entre Crecimiento del Mercado de Noticias Digitales y PIB de España')
plt.xticks(df['Año'].astype(int))  # Formatear los años como enteros
plt.grid(True)
plt.show()