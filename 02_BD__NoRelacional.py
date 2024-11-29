
from pymongo import MongoClient

# Conectar a la base de datos no relacional

client = MongoClient("mongodb://localhost:27017/")

db = client["baseDatos_noRelac"]

# Tablas

clinicas_particulares = db["ClinicasParticulares"]
parques_recreativos = db["ParquesRecreativos"]

# Insertar datos

lista = [
    {"id": 1,
     "nombre": "Clínica Internacional",
     "ubicacion": "Quito",
     "especialidades": ["Cardiología", "Pediatría"],
     "numero_de_empleados": 40},
    {"id": 2,
     "nombre": "Clínica De la Mujerl",
     "ubicacion": "Guayaquilo",
     "especialidades": ["Ginecologia, Pediatría"],
     "numero_de_empleados": 60}
]
clinicas_particulares.insert_many(lista)

lista2 = [
    {"id": 1,
     "nombre": "Parque Acuático",
     "ubicacion": "Atacames",
     "tamaño": 11.3,
     "atracciones_principales": ["Dinosaurios, Piscina"]},
    {"id": 2,
     "nombre": "Parque Oasis",
     "ubicacion": "Chota",
     "tamaño": 10,
     "atracciones_principales": ["Toboganes, Piscina"]
     }
]
parques_recreativos.insert_many(lista2)

# Consultar datos
clinicas = list(clinicas_particulares.find())
print("Clínicas Particulares:", clinicas)

parques = list(parques_recreativos.find())
print("Parques Recreativos:", parques)

# Cerrar conexión
client.close()
