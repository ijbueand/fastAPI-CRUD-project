# Proyecto CRUD FastAPI

Este proyecto es una API utilizando FastAPI y SQLite para realizar operaciones CRUD (Create, Read, Update, Delete) en una base de datos de alumnos. 
La base de datos contiene información básica sobre alumnos, como ID, nombre, correo electrónico, rol y nombre de grupo.

## Estructura del proyecto

El proyecto se compone de los siguientes archivos:

- `main.py`: Contiene la lógica de la aplicación FastAPI, incluyendo la definición del modelo `Alumno`, las rutas para las operaciones CRUD y las funciones que interactúan con la base de datos.
- `database_creation.py`: Script para crear la base de datos SQLite (`database.db`) y poblarla con datos de un archivo CSV (`datos_alumnos.csv`).
- `datos_alumnos.csv`: Archivo CSV con datos de ejemplo de alumnos.
- `Dockerfile`: Contiene las instrucciones para construir la imagen Docker de la aplicación.
- `docker-compose.yml`: Define los servicios, redes y volúmenes necesarios para ejecutar la aplicación en un entorno Docker.
- `README.md`: Este archivo, que proporciona una descripción general del proyecto y explica cómo ejecutarlo y usarlo.

## Cómo ejecutar el proyecto

1. Asegúrate de tener instalado Docker y Docker Compose en tu sistema.
2. Abre un terminal y navega hasta la carpeta del proyecto.
3. Ejecuta el siguiente comando para construir y ejecutar la aplicación usando Docker Compose: docker-compose up --build
4. Una vez que la aplicación esté en ejecución, abre tu navegador y ve a http://localhost:8000/docs para acceder a la documentación interactiva de FastAPI. Aquí podrás probar las diferentes operaciones CRUD directamente desde tu navegador.

## Uso de la API

La API proporciona las siguientes rutas para interactuar con la base de datos de alumnos:

- `POST /alumnos/`: Crea un nuevo registro de alumno.
- `GET /alumnos/`: Obtiene una lista de todos los alumnos en la base de datos.
- `PUT /alumnos/{id}`: Actualiza la información de un alumno existente, identificado por su ID.
- `DELETE /alumnos/{id}`: Elimina un alumno existente de la base de datos, identificado por su ID.

Puedes probar estas rutas y ver ejemplos de cómo usarlas en la documentación interactiva de FastAPI en http://localhost:8000/docs.
