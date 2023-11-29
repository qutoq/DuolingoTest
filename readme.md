### Страницы
1. **""** - главная
2. **"/register"** - регистрация
3. **"/post"** - список постов

### Модели
1. **Post:** author, title, text, created_date, published_date
2. **Пользователи** 
3. **Course:** title, image, description, link, city, address, schedule, cost

### Локальный запуск 
Dockerfile пока не работает

`python manage.py runserver 0:4000` можно и 0:8000

### Планы
1. Переехать на MySQL
2. Добавить восстановление пароля
3. Подобрать api для отправки писем
