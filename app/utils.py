def get_population(country_dict):

  population_dict = {
      '2022': int(country_dict['2022 Population']),
      '2020': int(country_dict['2020 Population']),
      '2015': int(country_dict['2015 Population']),
      '2010': int(country_dict['2010 Population']),
      '2000': int(country_dict['2000 Population']),
      '1990': int(country_dict['1990 Population']),
      '1980': int(country_dict['1980 Population']),
      '1970': int(country_dict['1970 Population'])
  }

  labels = population_dict.keys()
  values = population_dict.values()

  return labels, values


def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country,
                       data))
  return result


def get_world_percentages(data):

  labels = [x['Country/Territory'] for x in data]
  values = [x['World Population Percentage'] for x in data]

  return labels, values


# Esta función devuelve el país con mayor población
'''
def get_arg_population():
  import read_csv as funtion

  data = funtion.read_csv('./app/data.csv')
  data = list(
      filter(lambda item: item['Country/Territory'] == 'Argentina', data))

  #print("Resultado:", data)

  # Leer todas las propiedades del diccionario y filtrar solo aquellas propiedaddes que sean años

  for item in data:

    for propiedad in item:
      print(propiedad)

      # Evalua si una variable contiene números
      pattern = r'\b\d{4}\b'
      if (bool(re.search(pattern, propiedad))):

        # Extrae el año de la propiedad
        dict_prop_name = ''.join(re.findall(r'\d', propiedad))
        #print(dict_prop_name)

    #resultado = zip(desc,value)


if __name__ == '__main__':
  get_population()
'''
