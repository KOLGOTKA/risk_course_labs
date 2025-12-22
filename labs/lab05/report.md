<div align="center">
<h1><a id="intro">Лабораторная работа №5</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Сергеев_Н._М.-8b9aff" alt="Contributor Badge"></a></div>

## Задание

- [X] 1. Поставьте `Docker` и `buildkit`

```bash
uniqm@DESKTOP-OT4LBEF:~$ docker buildx version
github.com/docker/buildx v0.30.1 9e66234aa13328a5e75b75aa5574e1ca6d6d9c01
```

- [X] 2. Перейдите в `source` и выведите на терминале, далее проанализируйте следующие команды консоли

```bash
$ docker buildx build -t hellow-appsec-world .
$ docker run hello-appsec-world
$ docker run --rm -it hello-appsec-world

$ docker save -o hello.tar hello-appsec-world
$ docker load -i hello.tar
```

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker buildx build -t hello-appsec-world .
[+] Building 47.3s (13/13) FINISHED                                                    docker:default
 => [internal] load build definition from Dockerfile                                             0.0s
 => => transferring dockerfile: 443B                                                             0.0s
 => [internal] load .dockerignore                                                                0.0s
 => => transferring context: 2B                                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                              5.5s
 => [internal] load build context                                                                0.0s
 => => transferring context: 488B                                                                0.0s
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e  10.6s
 => => resolve docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee6  0.0s
 => => sha256:cb352e69d7b69f39dbc2cc35ecc34d01ca14439abc55911a5f7932f3dd6bd079 5.48kB / 5.48kB   0.0s
 => => sha256:1733a4cd59540b3470ff7a90963bcdea5b543279dd6bdaf022d7883fdad221e 29.78MB / 29.78MB  5.8s
 => => sha256:72cf4c3b83019e176aba979aba419d35f56576bbcfc4f7249a1ab1d4b536730b 1.29MB / 1.29MB   1.6s
 => => sha256:4d55cfecf3663813d03c369bcd532b89f41cf07b65d95887ef686538370a747 14.36MB / 14.36MB  4.5s
 => => sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6 10.37kB / 10.37kB  0.0s
 => => sha256:26fe52250f1b8012f5061c8f7228e6fca4f100aa3f99b41a8aa2608a42c5db43 1.75kB / 1.75kB   0.0s
 => => sha256:3f0cdbca744e7bd0ce0ff6da73b9148829b04309925992954a314ba203f56e99 249B / 249B       2.2s
 => => extracting sha256:1733a4cd59540b3470ff7a90963bcdea5b543279dd6bdaf022d7883fdad221e5        2.3s
 => => extracting sha256:72cf4c3b83019e176aba979aba419d35f56576bbcfc4f7249a1ab1d4b536730b        0.3s
 => => extracting sha256:4d55cfecf3663813d03c369bcd532b89f41cf07b65d95887ef686538370a747c        1.7s
 => => extracting sha256:3f0cdbca744e7bd0ce0ff6da73b9148829b04309925992954a314ba203f56e99        0.0s
 => [builder 2/4] WORKDIR /hello                                                                 0.3s
 => [builder 3/4] COPY requirements.txt .                                                        0.1s
 => [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requiremen  27.2s
 => [stage-1 3/6] COPY --from=builder /wheels /wheels                                            0.0s
 => [stage-1 4/6] COPY requirements.txt .                                                        0.1s
 => [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt            2.9s
 => [stage-1 6/6] COPY hello.py .                                                                0.0s
 => exporting to image                                                                           0.2s
 => => exporting layers                                                                          0.2s
 => => writing image sha256:bbb77c154ba90604a734b1b0c7274ac1102926fcbd66844d318cc57262303a1f     0.0s
 => => naming to docker.io/library/hello-appsec-world                                            0.0s
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker run hello-appsec-world
hello appsec world
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker run --rm -it hello-appsec-world
hello appsec world
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker save -o hello.tar hello-appsec-world
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker load -i hello.tar
Loaded image: hello-appsec-world:latest
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker run hello-appsec-world
hello appsec world
```

__Команда `docker buildx build -t hello-appsec-world .`__

- buildx build — сборка образа через BuildKit.
- -t hello-appsec-world — присваивает образу тег hello-appsec-world.
- . — контекст сборки (текущая директория).

__Команда `docker run hello-appsec-world`.__ Запускает контейнер из образа hello-appsec-world. Контейнер печатает hello appsec world.

__Команда `docker run --rm -it hello-appsec-world`__

- -i (interactive) — оставляет STDIN открытым.
- -t — выделяет псевдотерминал.
- --rm — автоматически удаляет контейнер после завершения.

Результат выполнения тот же.

__Команды `docker save` / `docker load`__

- docker save -o hello.tar hello-appsec-world сохраняет образ в файл hello.tar.
- docker load -i hello.tar загружает образ из архива.

Повторный docker run подтверждает, что образ успешно загружен и запускается.


- [X] 3. Откройте `Dockerfile` и сделайте его анализ. Сделайте `commit`

```dockerfile
# Этап 1: сборка зависимостей
FROM python:3.11-slim AS builder
WORKDIR /hello
# Копируем файл с зависимостями
COPY requirements.txt . 
# Устанавливаем зависимости в отдельную директорию wheelhouse для кеширования
RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt

# Этап 2: запускаемый образ
FROM python:3.11-slim
WORKDIR /hello
# Копируем файл с зависимостями
COPY --from=builder /wheels /wheels # Копируем собранные wheel-пакеты
COPY requirements.txt . 
# Устанавливаем зависимости из wheel-пакетов
RUN pip install --no-index --find-links=/wheels -r requirements.txt
# Копируем исходный код приложения
COPY hello.py .

# Переменные окружения для улучшенной работы Python
ENV PYTHONUNBUFFERED=1
# Запускаем приложение
CMD ["python", "hello.py"] 
```

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker run --rm hello-appsec-world Nikita
pygame 2.6.1 (SDL 2.28.4, Python 3.11.14)
Hello from the pygame community. https://www.pygame.org/contribute.html
Привет, Nikita!
```

- [X] 4. Замените в `Dockerfile`значение скрипта на `python` тем, который вы сделали ранее в прошлых лабораторных работах. Вложите свой файл `python` в директорию. Сделайте анализ своего измененного `Dockerfile` и внесите изменения. Сделайте `commit`. 

Обновляем `requirements.txt`
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ cat requirements.txt
typer
pygame
```

Обновленный `Dockerfile`
```dockerfile
# Этап 1: сборка зависимостей
FROM python:3.11-slim AS builder
WORKDIR /hello
# Копируем файл с зависимостями
COPY requirements.txt . 
# Устанавливаем зависимости в отдельную директорию wheelhouse для кеширования
RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt

# Этап 2: запускаемый образ
FROM python:3.11-slim
WORKDIR /hello
# Копируем файл с зависимостями
COPY --from=builder /wheels /wheels # Копируем собранные wheel-пакеты
COPY requirements.txt . 
# Устанавливаем зависимости из wheel-пакетов
RUN pip install --no-index --find-links=/wheels -r requirements.txt
# Копируем исходный код приложения
COPY my_hello.py .

# Переменные окружения для улучшенной работы Python
ENV PYTHONUNBUFFERED=1
# Заменили CMD на ENTRYPOINT, чтобы зафиксировать запуск python my_hello.py как основную, неизменяемую команду контейнера
ENTRYPOINT ["python", "my_hello.py"] 
```

- [X] 5. Выведите на терминале и проанализируйте следующие команды консоли. Сравните хеш сумму вашего архива с `image.tar` из репозитория, выведите на терминал.

```bash
$ docker buildx build -t hellow-appsec-world .
$ docker run hello-appsec-world
$ docker save -o hello_ypur_project.tar hello-appsec-world

$ docker load -i hello_ypur_project.tar
$ docker run hello-appsec-world

$ docker load -i image.tar
$ docker run hello-appsec-world
```

Сборка и запуск:
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker buildx build -t hello-app
sec-world .
[+] Building 1.1s (13/13) FINISHED                                                     docker:default
 => [internal] load build definition from Dockerfile                                             0.0s
 => => transferring dockerfile: 456B                                                             0.0s
 => [internal] load .dockerignore                                                                0.0s
 => => transferring context: 2B                                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                              1.0s
 => [internal] load build context                                                                0.0s
 => => transferring context: 68B                                                                 0.0s
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e6  0.0s
 => CACHED [builder 2/4] WORKDIR /hello                                                          0.0s
 => CACHED [builder 3/4] COPY requirements.txt .                                                 0.0s
 => CACHED [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requ  0.0s
 => CACHED [stage-1 3/6] COPY --from=builder /wheels /wheels                                     0.0s
 => CACHED [stage-1 4/6] COPY requirements.txt .                                                 0.0s
 => CACHED [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt     0.0s
 => CACHED [stage-1 6/6] COPY my_hello.py .                                                      0.0s
 => exporting to image                                                                           0.0s
 => => exporting layers                                                                          0.0s
 => => writing image sha256:0a21b73ace084e66187f05c3c6da95f3ab00ad8e60e3e3a2c0e1579206d6cedc     0.0s
 => => naming to docker.io/library/hello-appsec-world                                            0.0s
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker run hello-appsec-world Nikita
pygame 2.6.1 (SDL 2.28.4, Python 3.11.14)
Hello from the pygame community. https://www.pygame.org/contribute.html
Привет, Nikita!
```

Сохранение/загрузка архива:
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker save -o my_hello.tar hello-appsec-world
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker load -i my_hello.tar
Loaded image: hello-appsec-world:latest
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker run hello-appsec-world Nikita
pygame 2.6.1 (SDL 2.28.4, Python 3.11.14)
Hello from the pygame community. https://www.pygame.org/contribute.html
Привет, Nikita!
```

Загрузка `hello.tar`:
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker load -i hello.tar
The image hello-appsec-world:latest already exists, renaming the old one with ID sha256:0a21b73ace084e66187f05c3c6da95f3ab00ad8e60e3e3a2c0e1579206d6cedc to empty string
Loaded image: hello-appsec-world:latest
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker run hello-appsec-world
hello appsec world
```

Сравнение SHA-256:
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ sha256sum my_hello.tar hello.tar
dd556317831325e940a3d062a3063cf17708bb2c024dfaa6c9a36316a6e50bc3  my_hello.tar
4a486f7dbab8ed95419484df245dfaec4eda75f5c7c3fbc4e5b1a826612332fa  hello.tar
```
_Команда sha256sum my_hello.tar hello.tar вычисляет SHA-256 для двух файлов. Хеши различаются, следовательно файлы my_hello.tar и hello.tar не идентичны._

- [X] 6. Доработайте свой `python` скрипт подключаемыми библиотеками, далее их необходимо разместить в `requirements.txt`.

Так как у меня уже были добавлены подключаемые библиотеки, добавлем конкретные версии для библиотек
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ cat requirements.txt
typer==0.20.0
pygame==2.6.1
```

- [X] 7. Сделайте `commit`. Повторите сборку приложения по вашему `Dockerfile` для доработанного скрипта `python`. Сохраните `image` в виде .`tar` архива. Сделайте `commit`.

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ git commit -m "add tar archives and requirements"
[Sergeev_lab03 973b9c7] add tar archives and requirements
 2 files changed, 2 insertions(+), 2 deletions(-)
 create mode 100644 labs/lab05/source/my_hello_with_req.tar
```

- [X] 8. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ docker login
$ docker tag hello-appsec-world yourusername/hello-appsec-world
$ docker push yourusername/hello-appsec-world
$ docker inspect yourusername/hello-appsec-world
$ docker container create --name first hello-appsec-world # выпишите id контейнера

$ docker image pull geminishkv/hello-appsec-world
$ docker inspect geminishkvdev/hello-appsec-world
$ docker container create --name second hello-appsec-world

``` 

Вход в Docker Hub:
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker login

USING WEB-BASED LOGIN

i Info → To sign in with credentials on the command line, use 'docker login -u <username>'


Your one-time device confirmation code is: QDJN-PHSJ
Press ENTER to open your browser or submit your device code here: https://login.docker.com/activate

Waiting for authentication in the browser…
Login Succeeded
```
_`docker login` выполняет вход через web-based login_

Публикация образа:
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker push kolgotka/hello-appse
c-world
Using default tag: latest
The push refers to repository [docker.io/kolgotka/hello-appsec-world]
c36f3a196491: Pushed
00852b5e9db9: Pushed
89a451d4ae19: Pushed
02ce38082094: Pushed
209ea13f386e: Pushed
fa384bf02ac1: Mounted from library/python
600af8de593b: Mounted from library/python
424dc4972605: Mounted from library/python
77a2b55fbe8b: Mounted from library/python
latest: digest: sha256:3594fdff00a672d1098bb2cb7bf50753f11226eac39dbfc8bf7875e409dd4074 size: 2204
```
_`docker push kolgotka/hello-appsec-world` отправляет образ в Docker Hub_

Просмотр метаданных образа:
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker inspect kolgotka/hello-ap
psec-world
[
    {
        "Id": "sha256:fe3f20c51bd7952b621cacbb085376c82f7bb82d1acea68d8d95d10296bac188",
        "RepoTags": [
            "kolgotka/hello-appsec-world:latest",
            "hello-appsec-world:latest"
        ],
        "RepoDigests": [
            "kolgotka/hello-appsec-world@sha256:3594fdff00a672d1098bb2cb7bf50753f11226eac39dbfc8bf7875e409dd4074"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2025-12-14T12:40:50.302010802Z",
        "Container": "",
        "ContainerConfig": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": null,
            "Cmd": null,
            "Image": "",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "DockerVersion": "",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D",
                "PYTHON_VERSION=3.11.14",
                "PYTHON_SHA256=8d3ed8ec5c88c1c95f5e558612a725450d2452813ddad5e58fdb1a53b1209b78",
                "PYTHONUNBUFFERED=1"
            ],
            "Cmd": null,
            "Image": "",
            "Volumes": null,
            "WorkingDir": "/hello",
            "Entrypoint": [
                "python",
                "my_hello.py"
            ],
            "OnBuild": null,
            "Labels": null
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 199930824,
        "VirtualSize": 199930824,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/87ep3hhshqfyvog6jxerwxovo/diff:/var/lib/docker/overlay2/xolmtle5h0ifepdcpdjboj2lx/diff:/var/lib/docker/overlay2/vl4pwkuj3gz8etf4zl1vfbtt9/diff:/var/lib/docker/overlay2/f3g5ubel2hjjbptqlfi9as2xq/diff:/var/lib/docker/overlay2/032870bdd385f6fed5be0bd6449e437808bcdf6115302d855d1fdd4303c35442/diff:/var/lib/docker/overlay2/23058b7683c3ee945883ddb0faef962929f4c9267e5ee51d1fda7d77ebfbd727/diff:/var/lib/docker/overlay2/8590bc7a27eb93e5c814cfe22e688ee07f096980e4b70b04a7b35ce929e42813/diff:/var/lib/docker/overlay2/c1e2b987e8b33083d890184a997cb699180981084c08662821a7a23d6e7f05be/diff",
                "MergedDir": "/var/lib/docker/overlay2/qavw9fu87dhfr5k7myzetktpq/merged",
                "UpperDir": "/var/lib/docker/overlay2/qavw9fu87dhfr5k7myzetktpq/diff",
                "WorkDir": "/var/lib/docker/overlay2/qavw9fu87dhfr5k7myzetktpq/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:77a2b55fbe8b9984ce0af3ffc0b0ab62507668e63306ec161a585e587a3eb164",
                "sha256:424dc4972605239ec660864fe4cc7bcf6ebdadd752a7ee7ad065a83c34798378",
                "sha256:600af8de593b464a3642857b2dce39ad42474145771745962fb90ea9c276fa9d",
                "sha256:fa384bf02ac198a84ae5f0bbe085a6e4bd2de0be1b595833ba52e9780a936ba9",
                "sha256:209ea13f386e8fb0b465cd22c14604ace55274362bd5db9081a452b618bdc41c",
                "sha256:02ce380820946a4644c3f0a531b490efc21492b73a5c9f33a9b8c612d0a65227",
                "sha256:89a451d4ae19ae0564e6e317d61936f6edccf38c9190ebfce28bb92b29a23b8b",
                "sha256:00852b5e9db98276e0ef0b8398fc84d9148c09f8b906536016f31443093b4484",
                "sha256:c36f3a1964911b8822687fccf4c940747a31866d7b1fa04d9048567c8ac8cc76"
            ]
        },
        "Metadata": {
            "LastTagTime": "2025-12-14T12:50:15.55816234Z"
        }
    }
]
```
_`docker inspect kolgotka/hello-appsec-world` выводит JSON-метаданные образа_

В блоке Config видно, что:

- рабочая директория WorkingDir равна /hello;
- Entrypoint настроен как ["python","my_hello.py"];
- присутствует переменная окружения PYTHONUNBUFFERED=1;
- указана архитектура amd64, ОС linux и размер Size: 199930824.

Создание контейнера first:
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker container create --name first hello-appsec-world
fed54779178e4731f85d99deb035f9c154a5268cc1f7587773dc91c6fb314c48
```
_`docker container create --name first hello-appsec-world` создаёт контейнер first (без запуска) и выводит его ID_

С репозитория geminishkv мы не имеем доступа к образу, поэтому команда pull не сработала
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker image pull geminishkv/hello-appsec-world
Using default tag: latest
Error response from daemon: pull access denied for geminishkv/hello-appsec-world, repository does not exist or may require 'docker login': denied: requested access to the resource is denied
```

Устанавиливаем образ из своего репозитория и сравниваем результаты:
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker image pull kolgotka/hello
-appsec-world
Using default tag: latest
latest: Pulling from kolgotka/hello-appsec-world
Digest: sha256:3594fdff00a672d1098bb2cb7bf50753f11226eac39dbfc8bf7875e409dd4074
Status: Image is up to date for kolgotka/hello-appsec-world:latest
docker.io/kolgotka/hello-appsec-world:latest
```

_Команда inspect выводит практически такие же результаты, как и в предыдущем случае_.

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker container create --name second hello-appsec-world
54944686ef05ba2a449c64c428342d977d623c8b5e8edfa32a3ee70212351598
```

- [X] 9. Выведите на терминале и проанализируйте в консоли процессы, которые запущены, владельцев по пользователям

```bash 
 $ docker container run -it ubuntu /bin/bash
``` 

Скачиваем и устанавливаем образ ubuntu. Подключаеися к нему и смотрим запущенные процессы:
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker container run -it ubuntu /bin/bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
20043066d3d5: Pull complete
Digest: sha256:c35e29c9450151419d9448b0fd75374fec4fff364a27f176fb458d472dfc9e54
Status: Downloaded newer image for ubuntu:latest
root@8b2dff93f765:/# whoami
root
root@8b2dff93f765:/# id
uid=0(root) gid=0(root) groups=0(root)
root@8b2dff93f765:/# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   4588  3840 pts/0    Ss   13:02   0:00 /bin/bash
root        11  0.0  0.0   7888  4096 pts/0    R+   13:04   0:00 ps aux
```
- whoami показывает текущего пользователя внутри контейнера: root.
- id показывает идентификаторы пользователя/группы: uid=0(root) gid=0(root) groups=0(root).
- ps aux выводит процессы:
    - PID 1 — /bin/bash под пользователем root;
    - второй процесс — ps aux, также под root
 
- [X] 10. Выведите оба контейнера first и second на терминал

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker ps -a --filter "name=firs
t" --filter "name=second"
CONTAINER ID   IMAGE                COMMAND                CREATED          STATUS    PORTS     NAMES
54944686ef05   hello-appsec-world   "python my_hello.py"   12 minutes ago   Created             second
fed54779178e   hello-appsec-world   "python my_hello.py"   14 minutes ago   Created             first
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker inspect first --format 'Name={{.Name}} Id={{.Id}} Image={{.Config.Image}} Cmd={{json .Config.Cmd}}'
Name=/first Id=fed54779178e4731f85d99deb035f9c154a5268cc1f7587773dc91c6fb314c48 Image=hello-appsec-world Cmd=null
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05/source$ docker inspect second --format 'Name={{.Name}} Id={{.Id}} Image={{.Config.Image}} Cmd={{json .Config.Cmd}}'
Name=/second Id=54944686ef05ba2a449c64c428342d977d623c8b5e8edfa32a3ee70212351598 Image=hello-appsec-world Cmd=null
```
Выводим список всех контейнеров, ограничив поиск по имени `first` и `second`, в помощью команды `docker ps -a --filter "name=..."`

- [X] 11. Перейдите в основной корень `lab05` и выведите на терминале, и проанализируйте

```bash 
$ docker-compose up --build
``` 

Посмотрим, что находится в `docker-compose.yml`:
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05$ cat docker-compose.yml
version: "3.8"

networks:
  app_net:

services:
  server:
    build: ./server
    ports:
      - "8000:8000"
    networks:
      - app_net
    command: python app.py

  client:
    build: ./client
    depends_on:
      - server
    networks:
      - app_net
    command: python client.py
```

Собираем и запускаем:
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05$ docker-compose up --build
WARNING: The Docker Engine you're using is running in swarm mode.

Compose does not use swarm mode to deploy services to multiple nodes in a swarm. All containers will be scheduled on the current node.

To deploy your application across the swarm, use `docker stack deploy`.

Creating network "lab05_app_net" with the default driver
Building server
[+] Building 23.5s (14/14) FINISHED                                                    docker:default
 => [internal] load build definition from Dockerfile                                             0.0s
 => => transferring dockerfile: 431B                                                             0.0s
 => [internal] load .dockerignore                                                                0.0s
 => => transferring context: 2B                                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                              3.6s
 => [auth] library/python:pull token for registry-1.docker.io                                    0.0s
 => CACHED [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879  0.0s
 => [internal] load build context                                                                0.0s
 => => transferring context: 853B                                                                0.0s
 => [builder 2/4] WORKDIR /app                                                                   0.0s
 => [builder 3/4] COPY requirements.txt .                                                        0.0s
 => [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requiremen  16.2s
 => [stage-1 3/6] COPY --from=builder /wheels /wheels                                            0.0s
 => [stage-1 4/6] COPY requirements.txt .                                                        0.0s
 => [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt            2.6s
 => [stage-1 6/6] COPY app.py .                                                                  0.0s
 => exporting to image                                                                           0.2s
 => => exporting layers                                                                          0.2s
 => => writing image sha256:88f79fd8a889b59bc2c1ac34d8f1f6fac5dbac3e50fcc2cf5465598163a63721     0.0s
 => => naming to docker.io/library/lab05_server                                                  0.0s
Building client
[+] Building 20.4s (13/13) FINISHED                                                    docker:default
 => [internal] load .dockerignore                                                                0.0s
 => => transferring context: 2B                                                                  0.0s
 => [internal] load build definition from Dockerfile                                             0.0s
 => => transferring dockerfile: 437B                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                              0.4s
 => [internal] load build context                                                                0.0s
 => => transferring context: 577B                                                                0.0s
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e6  0.0s
 => CACHED [builder 2/4] WORKDIR /app                                                            0.0s
 => [builder 3/4] COPY requirements.txt .                                                        0.0s
 => [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requiremen  16.3s
 => [stage-1 3/6] COPY --from=builder /wheels /wheels                                            0.0s
 => [stage-1 4/6] COPY requirements.txt .                                                        0.0s
 => [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt            2.9s
 => [stage-1 6/6] COPY client.py .                                                               0.0s
 => exporting to image                                                                           0.2s
 => => exporting layers                                                                          0.2s
 => => writing image sha256:079dbf7390e7f29552017197428fd082fa375001c9ce70b9e60e30f4e744664f     0.0s
 => => naming to docker.io/library/lab05_client                                                  0.0s
Creating lab05_server_1 ... done
Creating lab05_client_1 ... done
Attaching to lab05_server_1, lab05_client_1
server_1  |  * Serving Flask app 'app'
server_1  |  * Debug mode: off
server_1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server_1  |  * Running on all addresses (0.0.0.0)
server_1  |  * Running on http://127.0.0.1:8000
server_1  |  * Running on http://172.21.0.2:8000
server_1  | Press CTRL+C to quit
server_1  | 172.21.0.3 - - [14/Dec/2025 13:18:09] "GET / HTTP/1.1" 200 -
client_1  |
client_1  |     <html>
client_1  |     <head><title>Colorful Output</title></head>
client_1  |     <body style="font-family: monospace; font-size: 24px;">
```
Команда `docker-compose up --build` запускает сервисы из compose-файла, принудительно собирая образы перед запуском.

В выводе видим, что:
- создана сеть lab05_app_net;
- выполнена сборка server и client с присвоением имён образам lab05_server и lab05_client;
- server_1 выводит, что приложение Flask запущено и слушает 0.0.0.0:8000 и доступно по http://127.0.0.1:8000 и http://172.21.0.2:8000.

Подключаемся к поднятому веб-сайту и видим логи подключения
```bash
server_1  | 172.21.0.1 - - [14/Dec/2025 13:19:47] "GET / HTTP/1.1" 200 -
server_1  | 172.21.0.1 - - [14/Dec/2025 13:19:47] "GET /favicon.ico HTTP/1.1" 404 -
```

А на сайте видим разноцветную надпись `hello appsec world`.

- [X] 12. Откройте соседнее окно терминала и выведите на терминале

```bash 
$ open -a "Google Chrome" http://localhost:8000
```

Так как на wls нет команды open, открываем сайт с помощью команды `explorer.exe http://localhost:8000`

После открытия http://localhost:8000 появляется новый запрос к серверу, что подтверждается строкой в логах GET / HTTP/1.1 со статусом 200:
```bash
server_1  | 172.21.0.1 - - [14/Dec/2025 13:24:15] "GET / HTTP/1.1" 200 -
```

- [X] 13. Остановите работу `docker-compose`.

```bash 
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05$ docker-compose down
Removing lab05_client_1 ... done
Removing lab05_server_1 ... done
Removing network lab05_app_net
```
_`docker-compose down` останавливает и удаляет контейнеры, созданные docker-compose up, и удаляет сеть проекта._

- [X] 14. Доработайте `docker-compose` и скрипт, который вы подготовили ранее, что бы вы смогли воспроизвести шаги п.11 по п.13 с демонстрацией. Сделайте `commit`.

Добавим в скрипт healthcheck
```python
@app.get("/health")
def health():
    return "ok", 200
```

Также добавляем в docker-compose.yml секцию healthcheck для сервиса server
```yaml
services:
  server:
    build: ./server
    ports:
      - "8000:8000"
    networks:
      - app_net
    command: python app.py
    healthcheck:
      test: ["CMD", "python", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health').read()"]
      interval: 5s
      timeout: 3s
      retries: 20
```
_Секция healthcheck в docker-compose.yml задаёт команду проверки состояния контейнера server._

Поменяем client.py на следующий код:
```python
import sys
import time
import requests

SERVER_URL = "http://server:8000"
RETRIES = 30
SLEEP_S = 1.0
TIMEOUT_S = 3.0

def colorful_print(text):
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m']
    reset = '\033[0m'
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(color + char + reset)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def wait_for_server():
    health_url = SERVER_URL.rstrip("/") + "/health"

    for _ in range(RETRIES):
        try:
            r = requests.get(health_url, timeout=TIMEOUT_S)
            if r.status_code == 200:
                return True
        except requests.RequestException:
            pass

    return False

if __name__ == "__main__":
    if not wait_for_server():
        print(f"ERROR: server is not reachable: {SERVER_URL}", file=sys.stderr)
        sys.exit(1)

    response = requests.get(SERVER_URL.rstrip("/") + "/", timeout=TIMEOUT_S)
    response.raise_for_status()
    colorful_print(response.text)
```
Здесь мы добавили функцию ожидания доступности сервера перед выполнением основного запроса.

_Функция `wait_for_server()` многократно запрашивает `GET /health` и завершает ожидание при `status_code == 200`. Если сервер недоступен по `/health`, клиент завершает выполнение с ошибкой._

Запускаем и смотрим логи:
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05$ docker-compose up --build
WARNING: The Docker Engine you're using is running in swarm mode.

Compose does not use swarm mode to deploy services to multiple nodes in a swarm. All containers will be scheduled on the current node.

To deploy your application across the swarm, use `docker stack deploy`.

Creating network "lab05_app_net" with the default driver
Building server
[+] Building 4.1s (14/14) FINISHED                                                     docker:default
 => [internal] load build definition from Dockerfile                                             0.0s
 => => transferring dockerfile: 431B                                                             0.0s
 => [internal] load .dockerignore                                                                0.0s
 => => transferring context: 2B                                                                  0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                              4.0s
 => [auth] library/python:pull token for registry-1.docker.io                                    0.0s
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e6  0.0s
 => [internal] load build context                                                                0.0s
 => => transferring context: 876B                                                                0.0s
 => CACHED [builder 2/4] WORKDIR /app                                                            0.0s
 => CACHED [builder 3/4] COPY requirements.txt .                                                 0.0s
 => CACHED [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requ  0.0s
 => CACHED [stage-1 3/6] COPY --from=builder /wheels /wheels                                     0.0s
 => CACHED [stage-1 4/6] COPY requirements.txt .                                                 0.0s
 => CACHED [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt     0.0s
 => [stage-1 6/6] COPY app.py .                                                                  0.0s
 => exporting to image                                                                           0.0s
 => => exporting layers                                                                          0.0s
 => => writing image sha256:a06c6f30c9d996a419ebe7055fc56fa20d9294de38c1558a8f1c7c7cbf820cfa     0.0s
 => => naming to docker.io/library/lab05_server                                                  0.0s
Building client
[+] Building 2.2s (14/14) FINISHED                                                     docker:default
 => [internal] load .dockerignore                                                                0.0s
 => => transferring context: 2B                                                                  0.0s
 => [internal] load build definition from Dockerfile                                             0.0s
 => => transferring dockerfile: 437B                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                              2.0s
 => [auth] library/python:pull token for registry-1.docker.io                                    0.0s
 => [internal] load build context                                                                0.0s
 => => transferring context: 1.16kB                                                              0.0s
 => [stage-1 1/6] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e6  0.0s
 => CACHED [stage-1 2/6] WORKDIR /app                                                            0.0s
 => CACHED [builder 3/4] COPY requirements.txt .                                                 0.0s
 => CACHED [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requ  0.0s
 => CACHED [stage-1 3/6] COPY --from=builder /wheels /wheels                                     0.0s
 => CACHED [stage-1 4/6] COPY requirements.txt .                                                 0.0s
 => CACHED [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt     0.0s
 => [stage-1 6/6] COPY client.py .                                                               0.0s
 => exporting to image                                                                           0.0s
 => => exporting layers                                                                          0.0s
 => => writing image sha256:497347d27a0fcb5126781451b69327448c9ea35c40c44d4766e8c7e0426ce0af     0.0s
 => => naming to docker.io/library/lab05_client                                                  0.0s
Creating lab05_server_1 ... done
Creating lab05_client_1 ... done
Attaching to lab05_server_1, lab05_client_1
server_1  |  * Serving Flask app 'app'
server_1  |  * Debug mode: off
server_1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server_1  |  * Running on all addresses (0.0.0.0)
server_1  |  * Running on http://127.0.0.1:8000
server_1  |  * Running on http://172.22.0.2:8000
server_1  | Press CTRL+C to quit
server_1  | 172.22.0.3 - - [14/Dec/2025 13:44:58] "GET /health HTTP/1.1" 200 -
server_1  | 172.22.0.3 - - [14/Dec/2025 13:44:58] "GET / HTTP/1.1" 200 -
client_1  |
client_1  |     <html>
client_1  |     <head><title>Colorful Output</title></head>
client_1  |     <body style="font-family: monospace; font-size: 24px;">
server_1  | 172.22.0.1 - - [14/Dec/2025 13:45:02] "GET / HTTP/1.1" 200 -
server_1  | 127.0.0.1 - - [14/Dec/2025 13:45:02] "GET /health HTTP/1.1" 200 -
server_1  | 127.0.0.1 - - [14/Dec/2025 13:45:07] "GET /health HTTP/1.1" 200 -
client_1  |     <span style="color:red">h</span><span style="color:green">e</span><span style="color:yellow">l</span><span style="color:blue">l</span><span style="color:purple">o</span><span style="color:red"> </span><span style="color:green">a</span><span style="color:yellow">p</span><span style="color:blue">p</span><span style="color:purple">s</span><span style="color:red">e</span><span style="color:green">c</span><span style="color:yellow"> </span><span style="color:blue">w</span><span style="color:purple">o</span><span style="color:red">r</span><span style="color:green">l</span><span style="color:yellow">d</span>
server_1  | 127.0.0.1 - - [14/Dec/2025 13:45:13] "GET /health HTTP/1.1" 200 -
client_1  |     </body>
client_1  |     </html>
client_1  |
lab05_client_1 exited with code 0
server_1  | 127.0.0.1 - - [14/Dec/2025 13:45:18] "GET /health HTTP/1.1" 200 -
server_1  | 127.0.0.1 - - [14/Dec/2025 13:45:23] "GET /health HTTP/1.1" 200 -
server_1  | 127.0.0.1 - - [14/Dec/2025 13:45:28] "GET /health HTTP/1.1" 200 -
server_1  | 127.0.0.1 - - [14/Dec/2025 13:45:33] "GET /health HTTP/1.1" 200 -
```

Проверка HTTP-ответов через curl:
```bash
uniqm@DESKTOP-OT4LBEF:~$ curl -i http://localhost:8000/ | head -n 20
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   761  100   761    0     0  64014      0 --:--:-- --:--:-- --:--:-- 69181
HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.14
Date: Sun, 14 Dec 2025 13:45:02 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 761
Connection: close


    <html>
    <head><title>Colorful Output</title></head>
    <body style="font-family: monospace; font-size: 24px;">
    <span style="color:red">h</span><span style="color:green">e</span><span style="color:yellow">l</span><span style="color:blue">l</span><span style="color:purple">o</span><span style="color:red"> </span><span style="color:green">a</span><span style="color:yellow">p</span><span style="color:blue">p</span><span style="color:purple">s</span><span style="color:red">e</span><span style="color:green">c</span><span style="color:yellow"> </span><span style="color:blue">w</span><span style="color:purple">o</span><span style="color:red">r</span><span style="color:green">l</span><span style="color:yellow">d</span>
    </body>
    </html>

```

```bash
uniqm@DESKTOP-OT4LBEF:~$ curl -i http://localhost:8000/health
HTTP/1.1 200 OK
Server: Werkzeug/2.3.7 Python/3.11.14
Date: Sun, 14 Dec 2025 13:47:35 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 2
Connection: close
```

- [X] 15. Залейте изменения в свой удаленный репозиторий, проверьте историю `commit`.

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab05$ git log -4 --oneline --decorate --graph
* 104a233 (HEAD -> Sergeev_lab03) update docker compose
* 973b9c7 add tar archives and requirements
* f6b73f8 new python printer
* fd69c69 add hello.tar
```

- [X] 16. Подготовьте отчет `gist`.
 
***

## Links

- [Docker](https://docs.docker.com/)
- [Markdown](https://stackedit.io)
- [Gist](https://gist.github.com)
- [GitHub CLI](https://cli.github.com)

Copyright (c) 2025 Nikita Sergeev
