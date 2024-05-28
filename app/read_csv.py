import csv


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # Primera fila es el nombre de las columnas
    header = next(reader)
    data = []
    for row in reader:

      # Uniendo Array de Tuplas
      iterable = zip(header, row)
      contry_dict = {key: value for key, value in iterable}
      data.append(contry_dict)
    return data


if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data)
