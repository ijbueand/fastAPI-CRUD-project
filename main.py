'''PROYECTO CRUD

Este sistema CRUD debe permitir al usuario realizar operaciones básicas 
sobre los datos almacenados en la base de datos (database.db), como 
agregar nuevos registros, leer y visualizar registros existentes, actualizar 
información y eliminar registros. Para ello, se deben crear las rutas y métodos 
correspondientes utilizando FastAPI y SQLite.'''

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import sqlite3

# Creamos una instancia de la aplicación FastAPi
app = FastAPI()

# Definimos la estructura de los datos que se van a almacenar en 
# la base de datos utilizando la clase BaseModel de Pydantic
class Alumno(BaseModel):
    ID: str
    Name: str
    email: str
    Role: str
    Group_name: str

# Ahora creamos las rutas y los métodos correspondientes para realizar 
# las operaciones CRUD. Concretamente, establecemos cuatro rutas: una 
# para crear un nuevo registro (POST), una para leer todos los registros 
# (GET), una para actualizar un registro existente (PUT) y una para 
# eliminar un registro existente (DELETE). Cada ruta llamará a una función 
# que realizará la operación correspondiente en la base de datos utilizando SQLite.

# Ruta para crear un nuevo registro
@app.post("/alumnos/")
async def create_alumno(alumno: Alumno):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO my_table (ID, Name, email, Role, Group_name) VALUES (?, ?, ?, ?, ?)", (alumno.ID, alumno.Name, alumno.email, alumno.Role, alumno.Group_name))
    con.commit()
    con.close()
    return JSONResponse(content={"message": "Alumno creado correctamente"}, status_code=201)

# Ruta para leer todos los registros
@app.get("/alumnos/")
async def read_alumnos():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM my_table")
    rows = cur.fetchall()
    con.close()
    return JSONResponse(content={"alumnos": [dict(row) for row in rows]}, status_code=200)

# Ruta para actualizar un registro existente
@app.put("/alumnos/{id}")
async def update_alumno(id: str, alumno: Alumno):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM my_table WHERE ID=?", (id,))
    row = cur.fetchone()
    if row is None:
        con.close()
        return JSONResponse(content={"message": "Alumno no encontrado"}, status_code=404)

    cur.execute("UPDATE my_table SET ID=?, Name=?, email=?, Role=?, Group_name=? WHERE ID=?", (alumno.ID, alumno.Name, alumno.email, alumno.Role, alumno.Group_name, id))
    con.commit()
    con.close()
    return JSONResponse(content={"message": "Alumno actualizado correctamente"}, status_code=200)

# Ruta para eliminar un registro existente
@app.delete("/alumnos/{id}")
async def delete_alumno(id: str):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("DELETE FROM my_table WHERE ID=?", (id,))
    con.commit()
    con.close()
    return JSONResponse(content={"message": "Alumno eliminado correctamente"}, status_code=200)
