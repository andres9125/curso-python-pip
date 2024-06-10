# Versión Python del Docker
FROM python:3.9

# Nombre del Docker
WORKDIR /app

# Copiar el Archivo de Requerimientos de Local a Docker 
COPY requirements.txt /app/requirements.txt

# Instalar Archivos
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiar todos los Archivos, Local?
COPY . /app

# Comando para mantener encendido el contenedor
# Lanzar Servidor de Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "89"]