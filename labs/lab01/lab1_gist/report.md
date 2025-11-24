<div align="center">
<h1><a id="intro">Лабораторная работа №1</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Сергеев_Н._М.-8b9aff" alt="Contributor Badge"></a></div>

***

## Задание

- [X] 1. Зарегистрироваться на почтовом сервисе **Gmail**. В случае наличия аккаунта - не требуется
- [X] 2. Зарегистрироваться на сервисе совместной разработки **GitHub**. В случае наличия аккаунта требуется произвести дополнительные настройки и обновить данные персонификации
- [X] 3. Отправить зарегистрированный адрес почтового ящика личным сообщением

n.m.sergeev@bk.ru

- [X] 4. Отправить зарегистрированный логин личным сообщением

KOLGOTKA

- [X] 5. Ознакомиться со ссылками учебного материала и формализованными требованиями из основного описания


- [X] 6. Сгенирировать **SSH** ключ и добавть его в список ключей для сервиса **GitHub**

![](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image.png)

- [X] 7. Сгенирировать **Personal Token** с правами **gist** и сохранить его в файл

![](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/pt_site.png)

- [X] 8. Сгенерировать GnuGP для подтверждения подписания коммитов и возможности использования Х.509

_smimesign - инструмент для подписи git commit с помощью S\MIME-сертификатов_

![](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-4.png)

![](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-5.png)

![](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-6.png)

- [X] 9. Подготовить глобальные переменные окружения для **GitHub**

![](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-2.png)

- [X] 10. Ознакомиться с материалами `gh` сервиса и использовать их для авторизации, `commit`, `pull requeste` и тд.

- Создайте локальный репозиторий на машине
- Проинициализируйте репозиторий
- Авторизуйтесь и спользуйте GitHub CLI для создания удаленного репозитория
- Создайте пустой README.md
- Используйте указание URL своего созданного репозитория для присвоения ветки master статуса origin

![gh auth](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-10.png)

422 ошибка говорит, что ключ уже добавлен, но это никак не влият на аутентификацию. Если ключ рабочий, то аутентификация пройдет успешно.

![init commit](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-12.png)

- В локальном репозитории и сделайте commit

![git add](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-14.png)
![init commit](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-13.png)

- Сделайте публикацию своего commit с флагом -S в удаленный репозиторий

Меняем ссылку на удалённый репозиторий с https на ssh и пушим. Флаг -S не нужен, так как в глобальных настройках git уже указан gpgsign.

![push](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-15.png)

- Создайте файл hello.py в локальном репозитории. Реализуйте Hello appsec world на языке python используя несколько интерпретаторов с "грязным" кодом

![hello](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-16.png)
- Сделайте commit с флагом -S
- Измените исходный код, что бы скрипт запрашивал имя пользователя и выводил Hello appsec world from @name

![hell2](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-17.png)

- Сделайте commit с флагом -S и сделайте публикацию в удаленный репозиторий. Проверьте вывод истории изменений

![commit log](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-20.png)

- В локальном репозитории создайте ветку patch1 и внесите изменения исправлению кода и модернизации до вида, чтобы код был рабочим. Сделайте публикацию своего commit с флагом -S в удаленный репозиторий

![typer](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-21.png)

![push](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-22.png)

- Проверьте, что ветка patch1 в удалённом репозитории
- Создайте pull-request в виде patch1 -> master

![pull req](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-24.png)

- В ветке patch1 добавьте в исходный код комментарии и убедитесь, что есть указанные изменения в pull-request

![alt text](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-25.png)

![push](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-26.png)

![diff](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-27.png)

- В удалённый репозитории выполните слияние pull-request для patch1 -> master и удалите ветку patch1

![merge](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-29.png)

- Стяните последние актуальные изменения и просмотрите историю изменений для master

![pull](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-28.png)

- Удалите локальную ветку patch1

![del branch](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-30.png)
- Создайте новую локальную ветку patch2

![branch2](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-31.png)

- Измените code style по своему усмотрению

![](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-32.png)

- Сделайте публикацию своего commit с флагом -S в удаленный репозиторий и создайте pull-request patch2 -> master

![alt text](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-34.png)

- В ветке master удаленного репозитория явно измените комментарий

![remote commit](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-33.png)

- Увидите, что в pull-request появились расхождения

![conflict](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-35.png)

- Локально сделайте rebase и исправьте расхождения (это называется конфликт)

![conflict](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-36.png)
![hello.py](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-37.png)


- Сделайте commit и опубликуйте изменения в ветке patch2

--force-with-lease - безопасный вариант --force, который не перезапишет изменения, если кто-то еще запушил в эту ветку.

![rebase](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-38.png)

- Убедитель, что пропали конфликтны.

![no conflict](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-39.png)

- Сделайте merge для pull-request patch2 -> master.

![merge](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-40.png)

- Подготовьте отчет gist.
- Продемонстрируйте в материалах отчета историю коммитов на локальном и удаленном репозитории.

__Дополнительные доработки кода в связи с комментариями от 24.11__

![colour code](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-43.png)

![colour print](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-44.png)

![git log](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-45.png)

![tree](https://raw.githubusercontent.com/KOLGOTKA/lab1/refs/heads/master/lab1_gist/imgs/image-46.png)

- [X] 11. Выполнить инструкцию учебного материала
- [X] 12. Оформить `README.md` по аналогии и использовать `shield`, etc.
- [X] 13. Составить `gist` отчет и отправить ссылку личным сообщением

Copyright (c) 2025 Sergeev Nikita
