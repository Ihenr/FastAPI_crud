# FastAPI
Un CRUD básico utilizada FastAPI, donde pueden implementar estas operaciones de manera eficiente utilizando SQLAlchemy para la gestión de la base de datos. 
## Requisitos

- Python 
- PostgreSQL

## Instalación

### 1. Clonar el repositorio

```sh
git clone https://github.com/Ihenr/FastAPI_crud.git
cd tu-proyecto
```
### 2. Crear la base de datos 

```sh
CREATE DATABASE fastapi_database;
```
### 3. Verificar la conexión a la base de datos  

```sh
- SQLALCHEMY_DATABASE_URL = "postgresql://usuario:contraseña@localhost:5432/nombre_db"
```

### 4. Iniciar el proyecto 
1. Verificar si tiene instalado virtualenv
   ```sh
   virtualenv --version
   ```
En caso de no tener instalar  virtualenv
   ```sh
   pip install virtualenv
      
   ```
2. Activa el entorno virtual
   ```sh
   python -m venv env
   o
   virtualenv venv
   ```
3. Activa el entorno virtual  
   ```sh
   --PowerShell
   .\venv\Scripts\activate.ps1
   ```
4. Instalar las dependencias 
   ```sh
   pip install -r requirements.txt
   ```
5. Ejecución.
   
** Dos formas de ejecutar FastAPI **
  - 1. uvicorn main:app 
  - 2. Agregar las líneas de Código.
     ```sh
     import uvicorn
     if __name__ == "__main__":
       uvicorn.run("main:app", port=8000, reload=True)
     ```
     y luego corremos
    ```sh
    python .\main.py
    ```
     
6. Abrir en el navegador
  ```sh
  http://127.0.0.1:8000/docs
   ```
    

