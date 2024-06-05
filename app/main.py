# llamar a los otros archivos! Por fin
import utils
import read_csv
import charts
import pandas as pd

'''
data = [{
    'Country': 'Colombia',
    'Population': 500
}, {
    'Country': 'Bolivia',
    'Population': 600
}]
'''
'''
def run():
  keys, values = utils.get_population()
  print(keys, values)

  print("Variable: ", utils.a)

  country = input('Type Country => ')

  result = utils.population_by_country(data, country)
  print("result:", result)
'''


def run():

  '''
  # Ejecuta la función read para leet el Archivo CSV pasandole la Ruta.
  data = read_csv.read_csv('./data.csv')

  # Digitar el nombre del Pais
  country = input('Type Country => ')
  name = country

  # Obtiene el  Diccionario del País
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)

    charts.generate_bar_chart(name, labels, values)

    # Ejecuta función generación grafico Pie
    charts.generate_pie_chart(name, labels, values)
  '''
  country = input('Type Continent => ')
  name = country

  df = pd.read_csv('./data.csv')
  df = df[df['Continent'] == name]

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(name, countries, percentages)
  charts.generate_bar_chart(name, countries, percentages)


    

'''
def run_2():

  # Ejecuta la función read para leet el Archivo CSV pasandole la Ruta.
  data = read_csv.read_csv('./data.csv')

  # Filtro por continente
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  # Obtiene el  Diccionario del País
  labels, values = utils.get_world_percentages(data)

  # Ejecuta función generación grafico Pie
  charts.generate_pie_chart(labels, values)
'''

# Ejecutar el archivo main.py
# Si el archivo es ejecutado desde la consola, entonces ejecuta run()
if __name__ == '__main__':
  run()
