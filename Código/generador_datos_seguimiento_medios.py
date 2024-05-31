import pandas as pd

# Crear un DataFrame con los datos inventados
data_proveedores = {
    'Medios proveedores de noticias': ['El País', 'El Mundo', 'Expansión', 'ElDiario.es', 'El Español', 
                                       '20 Minutos', 'Europa Press', 'ABC', 'El Confidencial', 'La Vanguardia'],
    'Coste por sus fuentes': [20000, 18000, 15000, 12000, 10000, 8000, 7000, 6000, 8500, 11000],
    'CTR': [0.12, 0.10, 0.08, 0.11, 0.09, 0.15, 0.13, 0.14, 0.11, 0.10],
    'Tráfico orgánico para el medio': [5000, 4500, 4000, 3500, 3000, 5000, 2000, 4000, 2100, 3300]
}

# Convertir a DataFrame
df_proveedores = pd.DataFrame(data_proveedores)

# Calcular el "Coste total real" como la suma de "Coste por sus fuentes" y "Tráfico orgánico para el medio"
df_proveedores['Coste total real'] = df_proveedores['Coste por sus fuentes'] + df_proveedores['Tráfico orgánico para el medio']

# Exportar el DataFrame a un archivo Excel
# output_file_path = 'Data\datos_seguimiento_medios.xlsx'
# df_proveedores.to_excel(output_file_path, index=False)