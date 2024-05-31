import pandas as pd
import matplotlib.pyplot as plt

# Datos obtenidos de Reuters de el executive summary que hacen de su informe: 
# https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2023/dnr-executive-summary

# Cargar los datos del archivo CSV
file_path = 'Data\data-ExyBd.csv'
df_sustitutos = pd.read_csv(file_path)

# Crear la gráfica con dos líneas
fig, ax1 = plt.subplots(figsize=(12, 8))

color = 'tab:blue'
ax1.set_xlabel('Año')
ax1.set_ylabel('Acceso directo a sitios web/apps de noticias (%)', color=color)
ax1.plot(df_sustitutos['Year'], df_sustitutos['Direct access to news websites/apps'], color=color, marker='o', label='Acceso directo a sitios web/apps de noticias')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_ylim(0, 100)  # Fijar el eje Y de 0% a 100%

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Acceso a noticias vía redes sociales (%)', color=color)
ax2.plot(df_sustitutos['Year'], df_sustitutos['Social media access'], color=color, marker='o', label='Acceso a noticias vía redes sociales')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(0, 100)  # Fijar el eje Y de 0% a 100%

# Añadir la leyenda
fig.legend(loc="upper left", bbox_to_anchor=(0.1,0.9))

# Añadir título
plt.title('Acceso a las Noticias: Sitios Web Directos vs Redes Sociales')

plt.tight_layout()
plt.show()
