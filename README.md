# 🌍 API Sensor Aire

¡Bienvenido al proyecto **API Sensor Aire**! 🚀 Este repositorio contiene una aplicación diseñada para monitorear la calidad del aire utilizando una arquitectura de microservicios. A continuación, encontrarás toda la información necesaria para comprender, instalar y contribuir a este proyecto. 🌱💨

## 📌 Tabla de Contenidos

- [📖 Descripción del Proyecto](#-descripción-del-proyecto)
- [📂 Estructura del Proyecto](#-estructura-del-proyecto)
- [⚙️ Requisitos Previos](#️-requisitos-previos)
- [🛠️ Configuración Inicial](#️-configuración-inicial)
- [🚀 Despliegue de la Aplicación](#-despliegue-de-la-aplicación)
- [📊 Uso de la Aplicación](#-uso-de-la-aplicación)
- [🤝 Contribuciones](#-contribuciones)
- [📜 Licencia](#-licencia)

---

## 📖 Descripción del Proyecto

**API Sensor Aire** es una aplicación que monitorea la calidad del aire en tiempo real. Utiliza sensores para recopilar datos ambientales y ofrece una interfaz interactiva para visualizar esta información. Además, incorpora análisis avanzados mediante técnicas de **machine learning** 🤖 para proporcionar **insights detallados** sobre la calidad del aire.

---

## 📂 Estructura del Proyecto
### api- sensor-aire/ 
- ├── backend/ # 📡 API RESTful │ ├── app/ │ ├── Dockerfile │ └── requirements.txt 
- ├── frontend/ # 🖥️ Interfaz de usuario │ ├── app/ │ ├── Dockerfile │ └── requirements.txt 
- ├── ml/  # 🧠 Modelos de Machine Learning │ ├── models/ │ └── scripts/ 
- ├── ollama/ # 🔥 Configuración de Ollama │ └── ollama/ 
- ├── docker-compose.yml 🛠️ Orquestación con Docker 
- └── README .md # 📜 Documentación


📌 **Componentes principales**:
- 🖥️ **Frontend**: Interfaz gráfica interactiva para visualizar los datos en tiempo real.
- 📡 **Backend**: API RESTful para la gestión y almacenamiento de datos.
- 🧠 **Machine Learning**: Algoritmos avanzados para el análisis de calidad del aire.
- 📦 **Docker Compose**: Orquestación de contenedores para un despliegue fácil y rápido.

---

## ⚙️ Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes en tu sistema:

- 🐳 [Docker](https://www.docker.com/get-started): Plataforma para desarrollar y ejecutar aplicaciones en contenedores.
- 🏗️ [Docker Compose](https://docs.docker.com/compose/install/): Herramienta para definir y gestionar aplicaciones multi-contenedor.

---

## 🛠️ Configuración Inicial

1️⃣ **Clonar el repositorio**:

```bash
git clone https://github.com/ccgg1997/api-sensor-aire.git
cd api-sensor-aire
```

2️⃣ Configurar variables de entorno:

Crea un archivo .env en la raíz del proyecto con los siguientes valores:
```bash
POSTGRES_USER=tu_usuario
POSTGRES_PASSWORD=tu_contraseña
POSTGRES_DB=nombre_base_datos
TELEGRAM_BOT_TOKEN=tu_token_de_telegram
```

# 🚀 Despliegue de la Aplicación
Para desplegar la aplicación completa utilizando Docker Compose:
1️⃣ Construir y levantar los servicios:
```bash
docker-compose up -d --build
```
2️⃣ Verificar que los contenedores estén corriendo:
```bash
docker-compose ps
```

#### ✅ Si todos los servicios están en estado Up, la aplicación está lista para usarse.

## 📊 Uso de la Aplicación
🔹 Frontend:
📍 Abre tu navegador y ve a http://localhost:8501 para visualizar los datos en tiempo real.

🔹 Backend:
📍 Accede a la API RESTful en http://localhost:5000.
📍 Puedes probar los endpoints con Postman o curl.

## 🤝 Contribuciones
🚀 ¡Las contribuciones son bienvenidas! Si deseas colaborar:

## Haz un fork de este repositorio.
Crea una nueva rama para tu funcionalidad (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -m 'Añadir nueva funcionalidad').
Sube los cambios a tu repositorio (git push origin feature/nueva-funcionalidad).
Abre un Pull Request en este repositorio.

💡 Si encuentras un problema o tienes una sugerencia, abre un issue para que podamos mejorar juntos.

📜 Licencia
📄 Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

📌 Autor: @ccgg1997
🌟 ¡No olvides dejar una ⭐ si te gusta este proyecto!

