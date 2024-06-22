# Importamos los frameworks pandas y matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Ubico y leo los datos desde el archivo en excel
especies_df = pd.read_excel('D:/BOOTCAMP/PAGINA_WEB_BIODIVERSIDAD_FUNZA_V3/db/Departamentales_especie_region.xlsx')

# Filtrar solo los datos de cundinamarca
cundi_df = especies_df[especies_df['slug_region'] == 'cundinamarca']

# Ordenar registros de mayor a menor
cundi_ordenado_df = cundi_df.sort_values(by='registros', ascending=False)

# Tomar los 10 primeros registros para graficar
diez_df = cundi_ordenado_df.head(5)

# Elimino la columna slug_region
final_df = diez_df.drop('slug_region', axis=1)

# Graficar los datos
plt.figure(figsize=(10, 6))
for column in final_df.columns[1:]:
    plt.plot(final_df[final_df.columns[0]], final_df[column], label=column)

plt.xlabel('Especie')
plt.ylabel('Registros')
plt.title('Gráfica de Especie vs Registros')
plt.legend()
plt.grid(True)

# Imprimir en una ventana el gráfico
plt.show()

# Guardar la gráfica como imagen
#plt.savefig('grafica.png')