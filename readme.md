## Фронтенд
templates/ - html файлы

templates/registration/ - страницы для входа/выхода + личный кабинет

templates/base.html - шаблон для всех страниц 

статичные файлы по папкам в static/

media/ - для картинок загруженных через сайт

fonts/ - шрифты

### Загрузка статичных файлов в html:

В начале файла должно быть `{% load static %}`

Для css/img: `href="{% static 'css/duolingo.css' %}"`

Для `background-image: url('{% static "/img/background4.png" %}');`

В css static не прогружается, поэтому вынес из login.css в
`<style> .side-image {background-image: url('{% static "/img/cat.jpeg" %}');} </style>`S

Для шрифтов немного подругому


### Примечания

logged_out.html - отображается после выхода из аккаунта. Но сейчас идёт редирект на главную. Если будет желание, то можно будет включить эту страницу

Для login.html, registration.html, password_change.html общий шаблон registration.base, который использует шаблон base. Получается двойное вложение шаблонов


## Страницы
app/urls.py
1. **""** - главная
2. **"/register"** - регистрация
3. **"/login"** - вход
4. **"/logout"** - выход
5. **"/password_change"** - смена пароля
6. **"/profile"** - личный кабинет
7. **"/post"** - список постов (скоро удалю)

## Локальный запуск 
`git clone`
`pip install -r requirements.txt`
`python manage.py runserver 8000`

## Планы
1. Адаптировать сайт для мобильных устройств
2. Подобрать api для отправки писем
