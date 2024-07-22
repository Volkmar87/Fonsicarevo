from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import openai
import pymysql
app = FastAPI()

# Montar el directorio de archivos estáticos (fondo)
app.mount("/imagenes", StaticFiles(directory="imagenes"), name="imagenes")

# Configurar tu clave de API de OpenAI
api_key1 = ""  
openai.api_key = api_key1
DB_CONFIG = {
    'host': 'database-1.cpi0ouoem383.us-east-1.rds.amazonaws.com',
    'port': 3306,
    'user': 'admin',
    'password': '',
    'database': 'cochesitos',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}
def execute_insert_query(query, params):
    connection = pymysql.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
        connection.commit()
    finally:
        connection.close()
# Inicio (revisar)
@app.get("/")
async def hallo():
    return FileResponse("index.html")

# Endpoint para generar cinco coches que se parezcan
@app.post("/recomendaciones")
async def recommend_car(request: Request):
    data = await request.json()
    marca = data.get('marca')
    modelo = data.get('modelo')
    
    if not modelo or not marca:
            raise HTTPException(status_code=400, detail="Necesito que me digas una marca y un modelo para comparar")
    
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
        {
            "role": "user",
            "content": f"Recomiéndame  5 coches parecidos a {marca} de {modelo}, pero de otra marca. Dame las recomendaciones en una lista ordenada",
        }])
        recomendaciones = response.choices[0].message.content
        # Insertar datos en la base de datos
        insert_query = "INSERT INTO fonsicar_volumen2 (marca, modelo, sugerencias) VALUES (%s, %s, %s)"
        insert_params = (marca, modelo, recomendaciones)
        execute_insert_query(insert_query, insert_params)
        return {"recommendations": response.choices[0].message.content}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Fin
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)