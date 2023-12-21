from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

#Modelo para crear y modificar usuarios
class User(BaseModel):
    dni: str
    name: str
    last_name: str
    age: int

#No existe bbdd real pero se simula
users_db = []

#endpoint para añadir usuario
@app.post("/users")
def create_user(user: User):
    # Check if DNI already exists
    if any(u.dni == user.dni for u in users_db):
        raise HTTPException(status_code=400, detail="DNI already exists")

    users_db.append(user)
    return {"message": "User added successfully"}

#endpoint para recibir informacion sobre el usuario segun DNI
@app.get("/users/{dni}")
def get_user(dni: str):
    user = next((u.dict() for u in users_db if u.dni == dni), None)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

#endpoint para modificar usuario segun DNI
@app.put("/users/{dni}")
def modify_user(dni: str, modified_data: User):
    existing_user = next((u for u in users_db if u.dni == dni), None)
    if existing_user:
        existing_user.name = modified_data.name
        existing_user.last_name = modified_data.last_name
        existing_user.age = modified_data.age
        return {"message": "User modified successfully"}
    raise HTTPException(status_code=404, detail="User not found")

#endpoint para listar los usuarios existentes
@app.get("/users", response_model=List[User])
def query_users(page: Optional[int] = 1, filter_dni: Optional[str] = None, filter_name: Optional[str] = None, filter_last_name: Optional[str] = None, filter_age: Optional[int] = None):
    filtered_users = users_db

    # aplicacion de filtros
    if filter_dni:
        filtered_users = [u for u in filtered_users if u.dni == filter_dni]
    if filter_name:
        filtered_users = [u for u in filtered_users if u.name == filter_name]
    if filter_last_name:
        filtered_users = [u for u in filtered_users if u.last_name == filter_last_name]
    if filter_age:
        filtered_users = [u for u in filtered_users if u.age == filter_age]

    #paginacion de resultados
    items_per_page = 10
    start = (page - 1) * items_per_page
    end = start + items_per_page

    return filtered_users[start:end]

#endpoint para borrar usuario segun DNI
@app.delete("/users/{dni}")
def delete_user(dni: str):
    global users_db
    users_db = [u for u in users_db if u.dni != dni]
    return {"message": "User deleted successfully"}

def start_fastapi_server():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)