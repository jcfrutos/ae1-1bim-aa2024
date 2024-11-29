"""Creacion de Base de datos"""

import sqlite3

# Conectar o crear la base de datos relacional
with sqlite3.connect("database_relacional.db") as con:
    cursor = con.cursor()

# Crear tablas
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ClinicasParticulares (
        id INTEGER PRIMARY KEY,
        nombre VARCHARD(50),
        ubicacion VARCHARD(50),
        especialidades TVARCHARD(50),
        numero_de_empleados INTEGER)
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS ParquesRecreativos (
        id INTEGER PRIMARY KEY,
        nombre VARCHARD(50),
        ubicacion VARCHARD(50),
        tamaño DOUBLE,
        atracciones_principales VARCHARD(50))
        """
    )

    # Insertar datos

    ClinicasParticulares = [
        (1, "Internacional", "Quito", "Cardiologia, Pediatría", 40),
        (2, "De la Mujer", "Guayaquil", "Ginecologia, Pediatría", 60),
    ]

    ParquesRecreativos = [
        (1, "Parque Acuatico", "Atacames", 11.3, "Dinosaurios, Piscina"),
        (2, "Parque Oasis", "Chota", 10, "Toboganes, Piscina")
    ]

    cursor.executemany(
        "insert into ClinicasParticulares values(?,?,?,?,?)",
        ClinicasParticulares,
    )

    cursor.executemany(
        "insert into  ParquesRecreativos values(?,?,?,?,?)",
        ParquesRecreativos,
    )

con.commit()

# Consultar datos
cursor.execute("SELECT * FROM ClinicasParticulares")
clinicas = cursor.fetchall()
print("Clínicas Particulares:", clinicas)

cursor.execute("SELECT * FROM ParquesRecreativos")
parques = cursor.fetchall()
print("Parques Recreativos:", parques)
