### Comandos para la base de datos

    $ pipenv shell

    #### Ejecutar la primera vez
    $ python app.py db init

    ### Ejecutar para crear las migraciones 
    $ pyhon app.py db migrate

    ### Ejecutar para enviar las migraciones hacia la base de datos
    $ python app.py db upgrade