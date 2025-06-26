# 🧪 API Testing Framework en Python

Este proyecto contiene una suite de pruebas automatizadas para testear endpoints REST de una API, usando `pytest`, `requests` y el patrón **Page Object Model (POM)**.

## 📦 Estructura del proyecto

├── tests/ # Casos de prueba organizados
├── pages/ # Clases POM para las APIs
├── conftest.py # Fixtures comunes y configuración
├── requirements.txt # Dependencias
├── .gitignore # Archivos a ignorar por Git
└── README.md # Documentación del proyecto

## 🚀 Tecnologías utilizadas

- Python 3.13.5
- Pytest
- Requests
- Logging estándar de Python
- Page Object Model

## 🧪 Ejecicion de pruebas

- Para ejecutar todos los tests desde el terminal:

pytest

- Para ejecutar un solo archivo de pruebas:

pytest tests/test_post_pet.py

## 🔧 Configuración

Las variables comunes como base_url y auth_headers se manejan desde los fixtures definidos en conftest.py
