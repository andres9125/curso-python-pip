import store
from fastapi import FastAPI

#Para que el response sea en HTML
from fastapi.responses import HTMLResponse

# Instancia de la Aplicación
app = FastAPI()

# Creación de Primer Recurso
@app.get('/') # Ruta desde la web, se puede acceder
def get_list():
    return [1,2,3,4]

@app.get('/contact', response_class=HTMLResponse) # Ruta desde la web, se puede acceder
def get_list():
    return """

        <html>
            <head>
                <h1>Mi primera Web en Python</h1>
                <h2>Impresionante!</h2>
            </head>
            <body>
                <p>Este Python esta genial!</p>
            </body>
        <html>

    """

def run():    
    store.get_categories()

if __name__ == '__main__':
    run()