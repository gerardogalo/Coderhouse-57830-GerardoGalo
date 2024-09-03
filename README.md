# Club Deportivo Messi

## Autor
Gerardo Octavio Galo
Comisión 57830
Curso Python - CODERHOUSE

## Descripción
Este proyecto Django es un prototipo para gestionar un club deportivo, permitiendo administrar socios, deportes e instalaciones de dicho club.

## Pasos seguidos para Configuración Inicial
1. Clonar el repositorio:
    ```
    git clone https://github.com/gerardogalo/TerceraPre-entrega-Galo.git
    cd .\TerceraPre-entrega-Galo\
    code .
    ```
2. Crear y activar un entorno virtual (opcional):
    ```
    python -m venv venv
    .\.venv\Scripts\activate 
    ```
3. Instalar Django, crear el proyecto y app:
    ```
    pip install django
    django-admin startproject config .
    python .\manage.py startapp club  
    ```
4. Realizar migraciones y crear un superusuario:
    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```
5. Iniciar el servidor:
    ```
    python manage.py runserver
    ```

## Orden Recomendado para Probar el Proyecto
Para probar el proyecto, se recomienda seguir este orden:
1. **Instalaciones**: Accede a la administración y carga primeramente las instalaciones. La base de datos ya contiene ejemplos precargados.
2. **Deportes**: Crea deportes asociándolos a las instalaciones existentes.
3. **Socios**: Finalmente, registra socios y asócialos a uno o más deportes.

## Cómo Probar
1. Accede a `http://127.0.0.1:8000/`
2. Utiliza los botones de la barra de navegación para acceder a las diferentes secciones: Socios, Deportes e Instalaciones.
2. Explora las funcionalidades de añadir y listar Socios, Deportes e Instalaciones.
3. Realiza busqueda por socios según apellido o según estado.
4. Accede a `http://127.0.0.1:8000/admin/` usando el usuario `admin` y la clave `123` para revisa los registros cargados

## Nota
La base de datos incluye varios socios, deportes e instalaciones precargados para facilitar la prueba.
