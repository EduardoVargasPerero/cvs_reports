# 🧠 API de Análisis Inteligente de PDFs

**API para cargar CVs en PDF, extraer texto, validar contenido y detectar datos de contacto por archivo.**

Este proyecto es una API REST construida con **Django** y **Django REST Framework**. Su propósito es:

- 🧾 Gestionar características de texto mediante un CRUD.
- 📄 Recibir archivos PDF y analizar su contenido textual.
- 🧠 Validar si contienen características previamente registradas.
- 📬 Extraer información de contacto: correos, teléfonos, GitHub y LinkedIn.

---

## ⚙️ Requisitos

- Python 3.8+
- pip
- virtualenv (opcional pero recomendado)

---

## 📦 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/api-inteligente-pdf.git
cd api-inteligente-pdf

# Crear entorno virtual
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```
---

## 🚀 Ejecutar el servidor

python manage.py runserver
La API estará disponible en: http://localhost:8000/

---

## 📂 Estructura del proyecto

api_inteligente_pdf/

├── app/

│   ├── models.py

│   ├── serializers.py

│   ├── views.py

│   ├── urls.py

│   └── ...

├── manage.py

├── README.md

└── requirements.txt


---


## 📌 Endpoints disponibles

🔁 CRUD de Características
Método	URL	Descripción
| Método | URL                      | Descripción                     |
| ------ | ------------------------ | ------------------------------- |
| GET    | `/caracteristicas/`      | Lista todas las características |
| POST   | `/caracteristicas/`      | Crea una nueva característica   |
| GET    | `/caracteristicas/{id}/` | Obtiene una característica      |
| PUT    | `/caracteristicas/{id}/` | Actualiza una característica    |
| DELETE | `/caracteristicas/{id}/` | Elimina una característica      |


📄 Análisis de PDFs
| Método | URL           | Descripción                                                  |
| ------ | ------------- | ------------------------------------------------------------ |
| POST   | `/subir-pdf/` | Sube uno o más archivos PDF y devuelve el análisis detallado |


---

##  ✅ Validaciones y características
✅ Los archivos deben ser PDFs.

✅ El texto se normaliza (mayúsculas + sin acentos).

✅ Se compara contra características registradas en la base de datos.

✅ Extrae correos, teléfonos, GitHub y LinkedIn automáticamente si el archivo es válido.


---


##  🧑‍💻 Autor
Eduardo Vargas Perero

📧 eduardoevargasp@hotmail.com