from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",  
    "http://localhost:3000",
    "https://testapimanu.pages.dev"  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datos
datos = [
    {"id": 1, "nombre": "EL PONCHO", "edad": 25, "pais": "GUACOCHE"},
    {"id": 2, "nombre": "EL PEPO", "edad": 30, "pais": "EL TOTUMO"},
    {"id": 3, "nombre": "EL MENBER", "edad": 22, "pais": "TOCAINA"},
    {"id": 4, "nombre": "LA MARIA", "edad": 28, "pais": "MOROCHOA"},
    {"id": 5, "nombre": "LUCHO", "edad": 35, "pais": "LA PAZ"},
    {"id": 6, "nombre": "Sofía", "edad": 27, "pais": "LA NEVADA"},
    {"id": 7, "nombre": "Pedro", "edad": 40, "pais": "LOS HATICOS"},
    {"id": 8, "nombre": "Lucía", "edad": 19, "pais": "SOLONDRIA"},
    {"id": 9, "nombre": "Carlos", "edad": 33, "pais": "VALLEDUPAR"},
    {"id": 10, "nombre": "Ana", "edad": 24, "pais": "BARRANQUILLA"},
    {"id": 11, "nombre": "Manuel", "edad": 29, "pais": "CARTAGENA"},
    {"id": 12, "nombre": "Marta", "edad": 31, "pais": "SANTA MARTA"},
    {"id": 13, "nombre": "Luis", "edad": 45, "pais": "RIOHACHA"},
    {"id": 14, "nombre": "Camila", "edad": 26, "pais": "MAICAO"},
    {"id": 15, "nombre": "Andrés", "edad": 38, "pais": "FONSECA"},
    {"id": 16, "nombre": "Paula", "edad": 21, "pais": "SAN JUAN"},
    {"id": 17, "nombre": "Diego", "edad": 34, "pais": "VILLANUEVA"},
    {"id": 18, "nombre": "Valentina", "edad": 23, "pais": "URUMITA"},
    {"id": 19, "nombre": "Fernando", "edad": 41, "pais": "DIBULLA"},
    {"id": 20, "nombre": "Daniela", "edad": 28, "pais": "ALBANIA"},
    {"id": 21, "nombre": "Ricardo", "edad": 36, "pais": "HATONUEVO"},
    {"id": 22, "nombre": "Natalia", "edad": 27, "pais": "BOSCONIA"},
    {"id": 23, "nombre": "Héctor", "edad": 39, "pais": "AGUACHICA"},
    {"id": 24, "nombre": "Laura", "edad": 22, "pais": "CODAZZI"},
    {"id": 25, "nombre": "Oscar", "edad": 44, "pais": "CHIRIGUANA"}
]

@app.get("/")
def get_datos():
    return {
        "fecha": datetime.now().strftime("%Y-%m-%d"),
        "total": len(datos),
        "datos": datos
    }

# handler para serverless
handler = Mangum(app)