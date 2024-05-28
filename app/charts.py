import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values) 
  
  ''' 
    EXIMUS|AMS|20240528|Comentarea Show
    plt.show() 
  '''
  plt.savefig(f'./imgs/{name}_bar.png')
  plt.close()


def generate_pie_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')  # Ordenamiento
    
  ''' 
    EXIMUS|AMS|20240528|Comentarea Show
    plt.show() 
  '''
  plt.savefig(f'./imgs/{name}_pie.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 200, 80]
  generate_pie_chart(labels, values)
