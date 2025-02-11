# FAQ Telegram Bot (not full)

Этот проект представляет собой Telegram-бота, который отвечает на вопросы, используя базу данных FAQ. Бот создан на Python с использованием библиотеки `python-telegram-bot` и базы данных SQLite.

## Функционал
- Реагирует на команду `/start` и отправляет приветственное сообщение.
- Отвечает на вопросы, используя базу данных FAQ.
- Если вопрос отсутствует в базе, бот сообщает об этом.

## Установка и запуск
### 1. Клонирование репозитория
```sh
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

### 2. Установка зависимостей
```sh
pip install -r requirements.txt
```

### 3. Настройка бота
Открыть файл `config.py` и вставить токен Telegram-бота:
```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

### 4. Запуск бота
```sh
python main.py
```

## Структура проекта
```
.
├── config.py        # Конфигурация (TOKEN для Telegram-бота)
├── database.py      # Работа с SQLite (создание БД, добавление и поиск вопросов)
├── main.py         # Основная логика работы бота
├── data.db         # Файл базы данных SQLite (создается автоматически)
├── requirements.txt # Список зависимостей
└── README.md       # Документация проекта
```

## Используемые технологии
- Python
- `python-telegram-bot`
- SQLite

## Лицензия
Этот проект распространяется под лицензией MIT.

