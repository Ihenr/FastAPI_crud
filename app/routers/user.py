from fastapi import APIRouter, Depends
from app.schemas import User, ShowUser, UpdateUser
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List

router = APIRouter(
    prefix="/user",
    tags=["Users"],
    responses={404: {"description": "Not found"}},

)


@router.get("/", response_model=List[ShowUser])
def obtener_usuarios(db: Session = Depends(get_db)):
    data = db.query(models.User).all()
    return  data

# crear un usuario
@router.post("/")
def crear_usuario(user:User, db: Session = Depends(get_db)):
    usuario = user.dict()
    nuevo_usuario = models.User(
        username = usuario["username"],
        password = usuario["password"],
        nombre = usuario["nombre"],
        apellido = usuario["apellido"],
        direccion = usuario["direccion"],
        telefono = usuario["telefono"],
        correo = usuario["correo"]
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return {"respuesta": "Usuario creado exitosamente"}

#listar usuarios con Id 
@router.get("/{user_id}", response_model=ShowUser) # Buscar usuario por  ID
def obtener_usurio(user_id:int, db: Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id).first()
    if not usuario:
        return {"respuesta": "Usuario no encontrado!!"}
    return usuario

#Eliminar usuario
@router.delete("/{user_id}")
def eliminar_usuario(user_id:int, db: Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():
        return {"respuesta": "Usuario no encontrado!!"}
    usuario.delete(synchronize_session=False)
    db.commit()
    return {"respuesta": "Usuario eliminado exitosamente"}



#Editar usuario
@router.patch("/{user_id}")
def actualizar_usuario(user_id: int, update_user: UpdateUser, db: Session = Depends(get_db)):
    usuario = db.query(models.User).filter(models.User.id == user_id)
    if not usuario.first():
        return {"respuesta": "Usuario no encontrado!!"}
    usuario.update(update_user.dict( exclude_unset=True))
    db.commit()
    return {"respuesta": "Usuario Actualizado exitosamente"}
