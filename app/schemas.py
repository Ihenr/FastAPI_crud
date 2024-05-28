from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#User Model 
class User(BaseModel): #Schema
    username : str
    password  : str
    nombre: str
    apellido: str 
    direccion: Optional[str]
    telefono:str
    correo:str
    creacion:datetime = datetime.now()

#Actualizar Model 
class UpdateUser(BaseModel): 
    username : Optional[str] = None
    password  : Optional[str] = None
    nombre : Optional[str] = None
    apellido : Optional[str] = None
    direccion : Optional[str] = None
    telefono : Optional[str] = None
    correo : Optional[str] = None
    

# Mostrar usuario
class ShowUser(BaseModel):
    username : str
    nombre: str
    apellido: str 
    direccion: Optional[str]
    telefono:str
    correo:str
    class Config():
        orm_mode = True

