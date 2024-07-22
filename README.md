# Fonsicarevo, tu recomendador de coches
🚗 Fonsicarevo - Recomendador de Coches 🚗

Fonsicarevo es una aplicación que utiliza inteligencia artificial para recomendar coches similares basados en la marca y el modelo que los usuarios proporcionan. Utilizando un modelo de lenguaje avanzado, la aplicación sugiere una lista de cinco coches que se parecen al coche indicado, pero de diferentes marcas.
Descripción del Proyecto

Este proyecto emplea un modelo de lenguaje avanzado (OpenAI) para generar recomendaciones de coches basadas en la marca y el modelo proporcionados por el usuario. Los datos ingresados se almacenan en una base de datos en AWS, y se utiliza FastAPI para manejar las solicitudes y la interacción con la base de datos.
Estructura del Proyecto

    prueba.py: Código para la aplicación FastAPI que maneja la generación de recomendaciones de coches y la interacción con la base de datos.
    index.html: Archivo HTML para la interfaz de usuario.
    Dockerfile: Archivo Docker para construir y ejecutar la aplicación en un contenedor Docker.
    requirements.txt: Archivo de requerimientos para las dependencias de la aplicación.
    imagenes/: Carpeta que contiene imágenes y otros recursos estáticos utilizados en el proyecto.
    db_config.ipynb: Jupyter Notebook para la configuración de la base de datos y la estructura de la tabla en AWS.

Instalación a través de Docker
Descargar la Imagen

Descarga la imagen desde Docker Hub:

bash

docker pull volkmar87/prueba:v1

Ejecutar el Contenedor

Ejecuta el contenedor con el siguiente comando:

bash

docker run -p 8000:8000 volkmar87/prueba:v1

Uso
Accede a la Interfaz Web

Abre tu navegador y accede a la aplicación en: http://localhost:8000/
Generar Recomendaciones

    Ingresa la marca y el modelo del coche en los campos proporcionados.
    Envía el formulario y espera la lista de cinco coches recomendados generada por el modelo de IA.

Herramientas

    Python: Lenguaje de programación utilizado.
    FastAPI: Framework para construir la API de la aplicación.
    MySQL: Sistema de gestión de bases de datos para almacenar datos de recomendaciones.
    Uvicorn: Servidor ASGI para ejecutar la aplicación FastAPI.
    OpenAI: API para generar recomendaciones basadas en el modelo GPT-3.5-turbo.
    Docker: Plataforma para construir y ejecutar contenedores.
    HTML: Lenguaje para crear la interfaz web.

Notas Adicionales

    Asegúrate de que la clave de API de OpenAI esté configurada correctamente en el archivo app.py.
    Verifica que la base de datos en AWS esté configurada y que la tabla fonsicar_volumen2 esté creada utilizando el Jupyter Notebook en db_config.ipynb.
    Para modificar la aplicación o agregar nuevas funcionalidades, edita el archivo app.py y actualiza los requisitos en requirements.txt.

¡Gracias por usar Fonsicarevo! Si tienes alguna pregunta, sugerencia o necesitas ayuda adicional, no dudes en contactar conmigo a través de aperezlizarriturri@gmail.com
    
