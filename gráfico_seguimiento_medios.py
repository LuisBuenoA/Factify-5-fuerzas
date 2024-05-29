import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Cargar los datos del archivo Excel
file_path = 'datos_seguimiento_medios.xlsx'
df_proveedores = pd.read_excel(file_path)

# Normalizar el CTR para usarlo en la escala de colores
norm = plt.Normalize(df_proveedores['CTR'].min(), df_proveedores['CTR'].max())
sm = plt.cm.ScalarMappable(cmap='Blues', norm=norm)

# Crear la gráfica de barras apiladas
fig, ax = plt.subplots(figsize=(12, 8))

# Graficar el 'Coste por sus fuentes'
ax.bar(df_proveedores['Medios proveedores de noticias'], df_proveedores['Coste por sus fuentes'], label='Coste por sus fuentes')

# Graficar el 'Tráfico orgánico para el medio' con colores basados en el CTR
for idx, row in df_proveedores.iterrows():
    ax.bar(row['Medios proveedores de noticias'], row['Tráfico orgánico para el medio'], 
           bottom=row['Coste por sus fuentes'], 
           color=sm.to_rgba(row['CTR']), 
           edgecolor='black', label='Tráfico orgánico para el medio' if idx == 0 else "")

# Añadir la barra de colores para el CTR
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('CTR')

# Añadir etiquetas y título
ax.set_xlabel('Medios proveedores de noticias')
ax.set_ylabel('Coste en euros')
ax.set_title('Costes desglosados por proveedores de noticias')
ax.legend()

# Mostrar la gráfica
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
