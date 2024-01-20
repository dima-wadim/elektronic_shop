В данном задании вам предлагается разработать онлайн платформу торговой сети электроники.
Технические требования:
    Python 3.8+
    Django 3+
    DRF 3.10+
    PostgreSQL 10+

При выполнении тестового задания вы можете дополнительно использовать любые сторонние Python библиотеки, без всяких ограничений.

Задание

    Создайте веб-приложение, с API интерфейсом и админ-панелью.
    Создайте базу данных используя миграции Django.

Требования к реализации:

    Необходимо реализовать модель сети по продаже электроники.

    Сеть должна представлять собой иерархическую структуру из 3 уровней:
        Завод;
        Розничная сеть;
        Индивидуальный предприниматель.

    Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т.е. завод всегда находится на 0 уровне, а если розничная сеть относится напрямую к заводу, минуя остальные звенья - её уровень - 1.
    Каждое звено сети должно обладать следующими элементами:
        Название;
        Контакты:
            Email;
            Страна;
            Город;
            Улица;
            Номер дома;
        Продукты:
            Название;
            Модель;
            Дата выхода продукта на рынок;
        Поставщик (предыдущий по иерархии объект сети);
        Задолженность перед поставщиком в денежном выражении с точностью до копеек;
        Время создания (заполняется автоматически при создании).
    Сделать вывод в админ-панели созданных объектов

    На странице объекта сети добавить:
        ссылку на «Поставщика»;
        фильтр по названию города;
        «admin action», очищающий задолженность перед поставщиком у выбранных объектов.
    Используя DRF, создать набор представлений:

    CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед поставщиком»);

    Добавить возможность фильтрации объектов по определенной стране.
    Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.


Для запуска проекта необходимо создать в корневой директории проекта файл .env и записать в него следующие переменные 
для использования базы данных PostgreSQL:

    POSTGRES_DB=
    POSTGRES_PASSWORD=
    POSTGRES_USER=
    POSTGRES_HOST=
    POSTGRES_PORT=

На сервере PostgreSQL необходимо создать базу данных.

Установить необходимые библиотеки с помощью команды в терминале
    $ pip install -r requirements.txt

Необходимо применить миграции к базе данных с помощью команды в терминале
    $ python3 manage.py migrate

Для запуска приложения необходимо ввести команду в терминале
    $ python3 manage.py runserver
