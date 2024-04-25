# Проект "Сайт рецептов" на Django  
## Описание:
Этот веб-сайт представляет собой приложение для хранения и обмена кулинарными рецептами, созданное с помощью Django.  
Пользователи могут:
* Регистрироваться и создавать учетные записи.
* Создавать новые рецепты, добавляя название, описание, ингредиенты, инструкции и изображения.
* Редактировать свои рецепты, изменяя информацию и изображения.
* Просматривать рецепты других пользователей, искать рецепты по названию, ингредиентам или категории.
* Сохранять рецепты в избранное.
## Функционал:
### Регистрация/авторизация:
* Регистрация с помощью  логина и пароль.
* Авторизация с помощью логина и пароля.
### Рецепты:
* Создание рецептов с подробным описанием.
* Добавление изображений к рецептам.
* Категоризация рецептов.
* Поиск рецептов по названию, ингредиентам или категории.
* Сохранение рецептов в избранное.
* Оставление комментариев к рецептам.
### Профили пользователей:
* Просмотр профилей других пользователей.
* Подписка на пользователей.
* Просмотр рецептов, созданных другими пользователями.
## Установка:
### Клонируйте репозиторий.
* Создайте виртуальное окружение: python3 -m venv .venv
* Активируйте виртуальное окружение: source .venv/bin/activate
* Установите зависимости: pip install -r requirements.txt
* Запустите приложение: python manage.py runserver
* Доступ к приложению: Приложение будет доступно по адресу: http://localhost:8000
## Использование:
* Для регистрации перейдите на страницу /register.
* Для авторизации перейдите на страницу /accounts/login.
* Для создания рецепта перейдите на страницу /create_recipe.
* Для выбора и изменений рецепта нажмите на картинку с ревептом.
## Примечания:
Приложение находится в стадии разработки, и его функционал может быть расширен в будущем.
