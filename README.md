# Boss_of_Apps

<picture>
 <img alt="Application and process manager" src="https://avatars.mds.yandex.net/get-images-cbir/936676/d21QxMSuHsOb73qt82VOVw8712/ocr">
</picture>

------Application and process manager------

(In progress)

Основной стек: Python, FastAPI, Postgresql, Nuitka

Данное веб-приложение должно иметь следующий функционал:
<ul>
 <li>Открытие и закрытие программ, установленных на компьютере;</li>
 <li>Отображение программ и процессов в специальном окне, чтобы пользователь мог ознакомиться с ними</li>
 <li>Данные о запусках хранить в базе данных (PostgreSQL)</li>

</ul>

  
Что на данные момент сделано:
<ul>
 <li>Открытие веб-приложения в браузере на локальном хосте;</li>
 <li>Отрисовка HTML шаблонов, чтобы пользователю было на что
посмотреть (main.py >> home()) а так же роутеры (templates >>
routers.py);</li>
 <li>Вывод в таблице всех запущенных процессов Windows с их
наименование, статусом, времени запуска и с их PID (app_script.py
>> get_app_dict());</li>
 <li>Вывод в другой таблице всех открытых окон (в панели задач):
app_script.py >> get_win_dict();</li>
 <li>Закрытие всех открытых окон кроме тех, которые требуют сохранить
документ перед закрытием. Выбор очевиден почему закрыть окна, а не
процессы, чтобы не случилось коллапса с оттенками синего на экране
(P.S. в коде у меня есть небольшой костыль, чтобы при проверке он не
закрывал PyCharm и собственно браузер с самой программой):
app_script.py >> close_all();</li>
 <li>Закрытие конкретного открытого окна из представленного списка.
Реализовано за счёт формы ввода в HTML с action, которое
перенаправляет по другому адресу и вызывает функцию закрытия
конкретного окна: main.py >> do_something();</li>
 <li>Создание базы данных PostgreSQL.
Соответственно установка, настройка и связь через ORM SQLALchemy, драйвер asyncpg;</li>
 <li>Регистрация, авторизация и выход пользователя через готовую
библиотеку FastAPI-Users. Выбрал стратегию хранения токена
JWTStrategy, потому что злоумышленники вряд ли даже узнают о
данном веб-приложении, да и в любом случае это более
распространённый метод и простой, чем через Database или Redis;</li>
 <li>Открытие окна проводника для открытия программы на компьютере.
Тут пришлось написать собственный протокол в файле .reg (его я тоже
прикреплю на всякий случай в папочке) и создание батовского файла
для работы протокола. (Небольшая инструкция, чтобы протокол
запустился: файл .reg надо запустить, а батовский файл поместить в
корень диска С:. Ну или запустить файл .cmd и без выше описанных
манипуляций всё заработает);</li>
 <li>Всё скомпилировано через Nuitka</li>
</ul>
