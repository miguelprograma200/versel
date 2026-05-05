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
    {"id": 1, "nombre": "EL PONCHO", "edad": 25, "pais": "GUACOCHE", "img": "https://pixabay.com/get/g46c910fdfda8b43f7787ba106a1943b492b43654c8a53c46945e0818f2c230bf44691088a45497c320c042a48a52b72a_1920.jpg"},
    {"id": 2, "nombre": "EL PEPO", "edad": 30, "pais": "EL TOTUMO", "img": "https://pixabay.com/get/gd9f38aeaf7d3846b0b7711c46b67d2f65f01336f1ed635ca98f9ae1fcbc3198040e2a5e3e4a57d583e72d9acc8da91ca_1920.jpg"},
    {"id": 3, "nombre": "EL MENBER", "edad": 22, "pais": "TOCAINA", "img": "https://pixabay.com/get/g1ba90f8375a00f1550b89e9a25bfb13003dc90be79344fb165febdabb5b321fcfa642d98c0e7a72f43c78a222c1281cc_1920.jpg"},
    {"id": 4, "nombre": "LA MARIA", "edad": 28, "pais": "MOROCHOA", "img": "https://pixabay.com/get/g7d9032916593a749e9d7c1592cef9ba8874c4886fb0eaf55c89417e2343234829f76f59f28c76c65aa4341bb8d095546_1920.jpg"},
    {"id": 5, "nombre": "LUCHO", "edad": 35, "pais": "LA PAZ", "img": "https://pixabay.com/get/g37194847cc92dd0b0b2554392be0f3ed2e8e6f0e2f7e8609144f97906402ab4f12ed2882e3a1027f79d1102bcd2cccf5_1920.jpg"},
    {"id": 6, "nombre": "Sofía", "edad": 27, "pais": "LA NEVADA", "img": "https://pixabay.com/get/g6e088ffc2b9b10e3d93d2689fa3219f1ae90f0b04e605bc040560b35d9c35622f7385f3a63e5c46f17adf9782e4ae9ce_1920.jpg"},
    {"id": 7, "nombre": "Pedro", "edad": 40, "pais": "LOS HATICOS", "img": "https://pixabay.com/get/g19314f4aa0020a5b3494c019dd9281fcdbaf24caa4ea14e4b8cb9873c48abc44a1c386d8e244cddac2c97be055f73ec2_1920.jpg"},
    {"id": 8, "nombre": "Lucía", "edad": 19, "pais": "SOLONDRIA", "img": "https://pixabay.com/get/g2eade9423d6bfc4fe54575d1ddca1e5b450e9b7e4283292ff19b84a17d61df73a4bf3fdade305d76024c55ee789f0e6a_1920.jpg"},
    {"id": 9, "nombre": "Carlos", "edad": 33, "pais": "VALLEDUPAR", "img": "https://cdn.pixabay.com/user/2016/03/24/17-38-25-443_96x96.jpg"},
    {"id": 10, "nombre": "Ana", "edad": 24, "pais": "BARRANQUILLA", "img": "https://pixabay.com/get/gd3591868e7f14d6c50ff699f62decd1aa65e049f1177aac44908f6e85d92d5b3777d7df6ce76f17c0113ac3cab59b60e_1920.jpg"},
    {"id": 11, "nombre": "Manuel", "edad": 29, "pais": "CARTAGENA", "img": "https://cdn.pixabay.com/user/2024/09/15/13-16-42-26_96x96.png"},
    {"id": 12, "nombre": "Marta", "edad": 31, "pais": "SANTA MARTA", "img": "https://cdn.pixabay.com/user/2025/05/10/06-52-54-224_96x96.jpg"},
    {"id": 13, "nombre": "Luis", "edad": 45, "pais": "RIOHACHA", "img": "https://cdn.pixabay.com/user/2024/11/08/11-39-05-526_96x96.jpg"},
    {"id": 14, "nombre": "Camila", "edad": 26, "pais": "MAICAO", "img": "https://cdn.pixabay.com/user/2022/08/21/08-09-34-590_96x96.jpg"},
    {"id": 15, "nombre": "Andrés", "edad": 38, "pais": "FONSECA", "img": "https://cdn.pixabay.com/user/2016/03/24/17-38-25-443_96x96.jpg"},
    {"id": 16, "nombre": "Paula", "edad": 21, "pais": "SAN JUAN", "img": "https://cdn.pixabay.com/user/2026/01/22/06-56-53-605_96x96.jpg"},
    {"id": 17, "nombre": "Diego", "edad": 34, "pais": "VILLANUEVA", "img": "https://cdn.pixabay.com/user/2021/06/08/08-54-50-264_96x96.jpg"},
    {"id": 18, "nombre": "Valentina", "edad": 23, "pais": "URUMITA", "img": "https://cdn.pixabay.com/user/2023/07/31/12-33-51-351_96x96.jpg"},
    {"id": 19, "nombre": "Fernando", "edad": 41, "pais": "DIBULLA", "img": "https://cdn.pixabay.com/user/2024/02/21/10-05-57-663_96x96.jpg"},
    {"id": 20, "nombre": "Daniela", "edad": 28, "pais": "ALBANIA", "img": "https://cdn.pixabay.com/user/2026/01/06/13-04-12-797_96x96.jpeg"},
    {"id": 21, "nombre": "Ricardo", "edad": 36, "pais": "HATONUEVO", "img": "https://pixabay.com/get/g1ba90f8375a00f1550b89e9a25bfb13003dc90be79344fb165febdabb5b321fcfa642d98c0e7a72f43c78a222c1281cc_1920.jpg"},
    {"id": 22, "nombre": "Natalia", "edad": 27, "pais": "BOSCONIA", "img": "https://pixabay.com/get/g7d9032916593a749e9d7c1592cef9ba8874c4886fb0eaf55c89417e2343234829f76f59f28c76c65aa4341bb8d095546_1920.jpg"},
    {"id": 23, "nombre": "Héctor", "edad": 39, "pais": "AGUACHICA", "img": "https://pixabay.com/get/g37194847cc92dd0b0b2554392be0f3ed2e8e6f0e2f7e8609144f97906402ab4f12ed2882e3a1027f79d1102bcd2cccf5_1920.jpg"},
    {"id": 24, "nombre": "Laura", "edad": 22, "pais": "CODAZZI", "img": "https://pixabay.com/get/g2eade9423d6bfc4fe54575d1ddca1e5b450e9b7e4283292ff19b84a17d61df73a4bf3fdade305d76024c55ee789f0e6a_1920.jpg"},
    {"id": 25, "nombre": "Oscar", "edad": 44, "pais": "CHIRIGUANA", "img": "https://cdn.pixabay.com/user/2016/03/24/17-38-25-443_96x96.jpg"}
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