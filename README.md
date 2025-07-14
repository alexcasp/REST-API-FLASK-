# Python REST API — Сериализация

## 📦 Установка

Убедитесь, что установлен Python 3.10+ и виртуальное окружение.

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

Запуск сервера

python main.py
Сервер запустится по адресу: http://127.0.0.1:5000


Примеры использования API
✅ 1. Создать продукт
POST /api/v1/product

{
  "name": "Ноутбук",
  "price": 999.99
}

📃 2. Получить все продукты
GET /api/v1/product?page=1&page_size=10
[
  {
    "id": 1,
    "name": "Ноутбук",
    "price": 999.99
  },
  ...
]

🔍 3. Получить продукт по ID
GET /api/v1/product/1
{
  "id": 1,
  "name": "Ноутбук",
  "price": 999.99
}

