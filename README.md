<strong>Task manager</strong><br>
Персонализированный сервиc, позволяющий пользователю ставить себе задачи, отражать в системе изменение их статуса и просматривать историю задач.

Сервис написан на python3 с использованием веб-фреймворка Django и Django REST Framework (DRF)
Сервис хранит данные в реляционной базе данных postgresql
Сервис предоставляtn интерфейс в виде JSON API.
Авторизация в API происходит с помощью токена. 
Cервис содержит Dockerfile для сборки сервиса.

Пользователь может зарегистрироваться в сервисе задав пару логин-пароль (/api/v1/accounts/register/). Реализовано при помощи плагина 
django-rest-registration - REST API для DRF.

Пользователь может авторизоваться в сервисе предоставив пару логин-пароль и получив в ответе два токена(/api/token/)
acess токен действует 5 минут (параметры могут быть изменены), затем пользователь должен обновить токен (api/token/refresh/) при помощи refresh токена, который действует еще 24 часа. После этого потребуется получить новый access токен. Реализовано при помощи плагинаdjangorestframework-simplejwt.

Пользователь видит только свои задачи (/mytasks/). Персонализированный список задач для конкретного пользователя получается путём фильтрации общего списка всех задач по конкретному пользователю (переопределение метода get_queryset()). Доступ ограничен параметрами аутентификации (необходимо предоставить токен).

Пользователь может создать себе задачу (Класс Task). Задача содержит следующие данные:
1.	 Название
2.	 Описание
3.	 Время создания
4.	 Статус - один из Новая, Запланированная, в Работе, Завершённая
5.	 Планируемое дата завершения

Пользователь может получить список своих задач, с возможностью фильтрации по статусу и планируемому времени завершения(/mytasks/?status=&estimated_date=). Реализовано при помощи плагина django-filter. Создается специальный отдельный класс TaskFilter. Во внутреннем классе Meta задаются поля, по которым необходио настроить фильтрацию. Поля для применения фильтрации можно изменить.

Пользователь может просмотреть историю изменений каждой своей задачи. Реализовано при помощи плагина django-simple-history. Плагин создает дополнительные таблицы в базе данных, которые хранят информацию о каждом изменении соответствующей модели.
