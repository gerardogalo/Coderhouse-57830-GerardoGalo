# Club Deportivo Messi

## Autor
Gerardo Octavio Galo  
[LinkedIn](https://www.linkedin.com/in/gerardogalo/)  
Comisión 57830  
Curso Python - CODERHOUSE

## Descripción
Este proyecto Django es un prototipo para gestionar un club deportivo, permitiendo administrar socios, deportes e instalaciones de dicho club. El objetivo es facilitar la gestión de actividades y recursos del club de manera eficiente.

## Video Demostrativo
Puedes ver un video demostrativo de la aplicación web funcionando en el siguiente enlace: [Ver Video](URL_DEL_VIDEO)

## Tecnologías Utilizadas
- Django
- Python
- SQLite
- HTML
- CSS

## Pasos seguidos para Configuración Inicial
1. Clonar el repositorio:
    ```
    git clone https://github.com/gerardogalo/Coderhouse-57830-GerardoGalo.git
    cd Coderhouse-57830-GerardoGalo
    ```
2. Crear y activar un entorno virtual (opcional):
    ```
    python -m venv venv
    .\venv\Scripts\activate
    ```
3. Instalar dependencias necesarias:
    ```
    pip install django
    pip install pillow
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

## Funcionalidades
- **Gestión de Socios:** Crear, ver, editar y eliminar socios.
- **Gestión de Deportes:** Administrar deportes ofrecidos por el club.
- **Gestión de Instalaciones:** Control sobre las instalaciones del club.
- **Autenticación de Usuarios:** Sistema de login y registro.
- **Perfil de Usuario:** Usuarios pueden editar sus perfiles y subir imágenes de perfil desde el ADMIN.

## Orden Recomendado para Probar el Proyecto
1. **Registro de Usuario**: Accede a la opción de registro desde la página de inicio de sesión para crear un usuario.
2. **Actualizar Perfil de Usuario**: Una vez registrado, actualiza los detalles del perfil del usuario.
3. **Instalaciones**: Accede a la administración y carga primeramente las instalaciones. La base de datos ya contiene ejemplos precargados.
4. **Deportes**: Crea deportes asociándolos a las instalaciones existentes.
5. **Socios**: Registra socios y asócialos a uno o más deportes.

## Cómo Probar
1. Accede a `http://127.0.0.1:8000/`.
2. Regístrate como nuevo usuario y actualiza tu perfil.
3. Inicia y cierra sesión para probar las funcionalidades de autenticación.
4. Utiliza los botones de la barra de navegación para acceder a las diferentes secciones: Socios, Deportes e Instalaciones.
5. Explora las funcionalidades de añadir y listar Socios, Deportes e Instalaciones.
6. Realiza búsqueda por socios según apellido o según estado.
7. Accede a `http://127.0.0.1:8000/admin/` usando el usuario `admin` y la clave `123` para revisar los registros cargados.

## Nota
La base de datos incluye varios socios, deportes e instalaciones precargados para facilitar la prueba. Además de `admin`, hay otros dos usuarios cargados: `mocho` con clave `gerardogalo` y `grecia` con clave `coderhouse`.

## Mejoras Futuras
- **Mejora en la Seguridad**: Reforzar las medidas de seguridad, especialmente en la gestión de datos sensibles y transacciones.
- **Integración con Calendario**: Integrar un sistema de calendario para gestionar turnos, eventos y actividades del club, permitiendo a los socios inscribirse a turnos directamente desde la plataforma.
- **Módulo de Pagos**: Implementar un sistema de pagos para permitir a los socios pagar cuotas y servicios directamente a través del sitio.
- **Notificaciones y Alertas**: Desarrollar un sistema de notificaciones para informar a los usuarios sobre eventos próximos, cambios en el calendario, o avisos importantes.
- **Reportes Dinámicos**: Generar reportes dinámicos sobre la actividad del club, como la asistencia a turnos, ingresos por cuotas, y uso de instalaciones.

