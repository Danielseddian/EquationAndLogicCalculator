# Equation and logic calculator
## Этот сервис позволяет делать некоторые расчеты, проверять свои или воспользоваться генераторами.
### Сейчас реализовано две функции: расчет квадратного корня уравнения и генератор, определяющий цвет предмета по его номеру


## Предустановки:
### В консоли сервера:
> sudo apt install postgresql postgresql-contrib -y # Установит postgresql

> sudo -u postgres psql -c 'select now()' # Проверит, что postgresql запущен и работает

> sudo service postgresql restart # Перезапустит, если установлен, но не работает

> sudo -u postgres psql # Запустит командную строку сервера postgresql

### В консоли PostgreSQL:
> CREATE DATABASE db_name; # Создаст БД. (db_name). - название бд

> CREATE USER username WITH ENCRYPTED PASSWORD 'password'; # Создаст нового пользователя. (username). - имя пользователя. ('password'). - пароль пользователя

> ALTER USER username WITH PASSWORD 'postgres'; # Поменяет пароль пользователя, если требуется. (username). - имя пользователя. ('password'). - новый пароль.

> GRANT ALL PRIVILEGES ON DATABASE db_name TO username; # Даст пользователю все права доступа к БД (db_name). - название БД. (username). - пользователь.

> \q # выйдет из консоли управления PostgreSQL
### В консоли сервера (контейнера) в директории проекта, где находится manage.py:
#### DB_ENGINE=django.db.backends.postgresql_psycopg2 - драйвер БД

#### DB_NAME=db_name - название базы данных

#### DB_USER=username - имя пользователя базы данных

#### DB_PASS=password - пароль пользователя базы данных

#### DB_HOST=localhost - хост, на который будут отправляться запросы, если на том же сервере: localhost

#### DB_PORT=5432 - порт, в который будет отправляться запрос
> sudo echo VAR=value >> .env # Добавит значениня переменных в .env файл. (VAR). - имя переменной. (value). - значение
### В консоли сервера (контейнера)
> sudo systemctl restart gunicorn # Перезагрузит Gunicorn для того, чтобы изменения вступили в силу
### в консоли сервера (контейнера) в директории с проектом (где находится manage.py):# Запуск:

# Запуск сервиса:
### БД в консоли сервера (контейнера):
> docker run --rm -e POSTGRES_USERNAME=postgres -e POSTGRES_PASSWORD=postgres --name postgres -p 5432:5432 postgres
### Перед первым запуском или после изменения БД, в консоли сервера (контейнера) в директории с проектом (где manage.py):
> python3 manage.py makemigrations application # (application). - опционально, директория с приложением

> python3 manage.py migrate --run-syncdb  # (--run-syncdb). - опционально, создаст новую таблицу
### Django в консоли сервера (контейнера) в директории с проектом (где manage.py):
> python3 manage.py runserver