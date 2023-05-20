# Utilizamos una imagen base de Python 3.9
FROM python:3.9

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos el archivo de requisitos al contenedor
COPY requirements.txt .

# Instalamos las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de archivos del proyecto al contenedor
COPY . .

# Exponemos el puerto en el que se ejecutará la aplicación
EXPOSE 8000

# Ejecutamos el comando para iniciar la aplicación FastAPI con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]