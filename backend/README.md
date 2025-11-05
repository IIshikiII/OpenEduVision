# Backend (FastAPI) — OpenEduVision

## Описание

Это модуль Backend для проекта OpenEduVision — API на FastAPI для обработки запросов, анализа данных, работы с курсами и студентами.

## Структура

- main.py — точка входа FastAPI
- requirements.txt — список зависимостей
- app/api/ — эндпойнты (courses.py, analytics.py, students.py)
- app/models/ — модели данных
- app/services/ — сервисы для логики и ML
- app/db/ — конфиг для БД

## Быстрый старт

1. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Запустите сервер:
   ```bash
   python main.py
   ```
Сервер будет доступен на http://localhost:8000, документация API на /docs.

## Технологии
- FastAPI
- Starlette
- Python-dotenv
- AsyncIO
- JWT-авторизация
- PostgreSQL / SQLite

## Структура папки backend
```
backend/
├── main.py
├── requirements.txt
└── app/
    ├── api/
    ├── models/
    ├── services/
    └── db/
```
