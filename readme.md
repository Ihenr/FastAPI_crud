# Dos formas de ejecutar FastAPI

  1. uvicorn main:app 
  2. Agregar las lineas de codigo.
     ```sh
        import uvicorn
           if __name__ == "__main__":
            uvicorn.run("main:app", port=8000, reload=True)
     ```
     y luego  corremos python .\main.py
    

