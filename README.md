--Gestor de Contraseñas Seguro (Python + MVC) Descripción--



Este proyecto es una aplicación de escritorio desarrollada en Python que permite gestionar contraseñas de diferentes servicios de manera segura.

La aplicación implementa el patrón de arquitectura MVC (Modelo - Vista - Controlador) y utiliza programación orientada a objetos (POO), lo que permite una organización modular, escalable y mantenible del código.

Los datos se almacenan en archivos JSON y las contraseñas se protegen mediante cifrado, evitando que queden visibles en texto plano.

Funcionalidades

La aplicación permite realizar operaciones CRUD sobre los registros:

 -Registrar credenciales (servicio, usuario, contraseña, categoría)
 -Consultar credenciales almacenadas
 -Eliminar registros específicos
 -Cifrar toda la información almacenada
 -Descifrar información cuando se requiera
 -Generar clave de cifrado
 -Seguridad y Cifrado

El sistema utiliza la librería cryptography específicamente el módulo Fernet, que proporciona cifrado simétrico seguro.

¿Cómo funciona?
Se genera una clave única (clave.key)
Esta clave se utiliza para cifrar y descifrar los datos
Los datos se convierten en formato binario cifrado antes de almacenarse en datos.key
El archivo JSON (passwords.json) solo existe en texto plano cuando los datos están descifrados
Flujo de seguridad:
Se registran los datos
Se guardan en JSON
Se cifran usando Fernet
Se elimina el JSON en texto plano
Se almacena el archivo cifrado (datos.key)
Para visualizar datos, se descifra usando la clave

 Esto garantiza que las contraseñas no sean visibles en almacenamiento.

 Arquitectura (MVC)

El proyecto está dividido en tres capas:

 Modelo (Model)
Maneja la lógica de negocio
Gestiona archivos JSON
Implementa cifrado y descifrado
 Vista (View)
Interfaz gráfica desarrollada con Tkinter
Permite la interacción del usuario
Muestra formularios y resultados
 Controlador (Controller)
Actúa como intermediario entre vista y modelo
Procesa eventos de la interfaz
Ejecuta las operaciones del modelo
 Librerías utilizadas
Librerías estándar:
json → Manejo de datos en formato JSON
os → Manejo de archivos y rutas
tkinter → Creación de interfaz gráfica
Librerías externas:
cryptography
Se utiliza para cifrar y descifrar contraseñas con Fernet

Instalación:

pip install cryptography
Interfaz Gráfica

La aplicación utiliza Tkinter, una biblioteca estándar de Python que permite crear aplicaciones de escritorio multiplataforma.

Opcionalmente, se pueden usar otras alternativas:

CustomTkinter → Interfaz moderna con temas oscuros/claro
Flet → Interfaces modernas tipo web/desktop con Python
 Estructura del Proyecto
python/
│
├── main.py
├── model/
│   └── gestor_model.py
├── view/
│   └── gui_view.py
├── controller/
│   └── gestor_controller.py
│
├── passwords.json
├── datos.key
├── clave.key
 Instalación y ejecución
1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd nombre-del-proyecto
2. Crear entorno virtual (opcional)
python -m venv venv
venv\Scripts\activate  # Windows
3. Instalar dependencias
pip install cryptography
4. Ejecutar la aplicación
python main.py
 Uso de la aplicación
Ejecutar la aplicación
Crear clave de cifrado
Registrar credenciales:
Servicio
Usuario
Contraseña
Categoría
Cifrar datos para protegerlos
Recuperar datos cuando sea necesario
Eliminar registros si se desea
 -Buenas prácticas aplicadas
Separación de responsabilidades (MVC)
Programación orientada a objetos (POO)
Validación de datos de entrada
Manejo básico de errores
Uso de cifrado para seguridad
Persistencia en archivos JSON
  -Posibles mejoras futuras
Autenticación de usuario
Encriptación con múltiples claves
Interfaz más moderna (CustomTkinter o Flet)
Base de datos en lugar de JSON
Búsqueda y filtrado de credenciales
Exportación de datos
 Autor

Proyecto desarrollado como parte de un parcial académico utilizando Python, MVC y técnicas de seguridad básicas.
