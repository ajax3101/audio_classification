# audio_classification
audio_classification
# Приклад Веб-сайту на Django5 присвячений "Бібліотеці"

[![Python Version](https://img.shields.io/badge/python-3.11-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-5.0-brightgreen.svg)](https://djangoproject.com)
Звичайний сайт, реалізований на веб-фреймворку Django 5

Як веб-інтерфейс використано фреймворк Bootstrap <https://getbootstrap.com/>

# Тестове завдання

## Розробка веб-застосунку для обліку книг у бібліотеці

# Мета завдання

## Оцінити навички кандидата в галузі веб-розробки на Python за допомогою фреймворку Django

# Завдання

## Ви маєте створити веб-додаток для обліку книг у бібліотеці. Застосунок повинен забезпечувати наступний функціонал

- Додавання нової книги із зазначенням назви, автора, жанру та року випуску.
- Перегляд списку всіх книг з можливістю їх редагування та видалення.
- Пошук книг за різними параметрами (назва, автор, жанр, рік випуску).
- Позначка книги як прочитана.
- Фільтрування книг за статусом прочитання (всі прочитані, непрочитані).

## Вимоги до технологій

- Використовуйте фреймворк Django для створення веб-застосунку.
- Використовуйте БД для зберігання інформації про книги.
- Використовуйте систему шаблонів Django для відображення даних.
- Реалізуйте механізм аутентифікації (реєстрація/вхід до системи).

![Library на Django](/library_img.png)

![Admin на Django](/library_img2.png)

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/ajax3101/library.git
```

```bash
    python3 -m venv venv
    . venv/bin/activate
 ```

Install the requirements:

```bash
 pip install -r requirements.txt
```

Run

```bash

 python manage.py makemigrations 
 python manage.py migrate
 python manage.py createsuperuser --email admin@example.com --username admin
 python manage.py runserver 
```
