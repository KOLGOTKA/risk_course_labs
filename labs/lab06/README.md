<div align="center">
<h1><a id="intro">Лабораторная работа №6</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Сергеев_Н._М.-8b9aff" alt="Contributor Badge"></a></div>

***

## Задание

- [X] 1. Необходимо установить `Docker Engine` для Linux

Docker уже был установлен на моей, поэтому просто проверил версию и скачал образ `docker-bench-security`:

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab06$ docker --version
Docker version 29.1.3, build f52814d
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab06$ docker pull docker/docker-bench-security
Using default tag: latest
latest: Pulling from docker/docker-bench-security
cd784148e348: Pull complete
48fe0d48816d: Pull complete
164e5e0f48c5: Pull complete
378ed37ea5ff: Pull complete
Digest: sha256:ddbdf4f86af4405da4a8a7b7cc62bb63bfeb75e85bf22d2ece70c204d7cfabb8
Status: Downloaded newer image for docker/docker-bench-security:latest
docker.io/docker/docker-bench-security:latest
```

- [X] 2. Проверьте работу докера и сделать скрипт `audit.sh` исполняемым

Проверяем работоспособность Docker запуском `hello-world` образа:
```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab06$ docker version
Client: Docker Engine - Community
 Version:           29.1.3
 API version:       1.43 (downgraded from 1.52)
 Go version:        go1.25.5
 Git commit:        f52814d
 Built:             Fri Dec 12 14:49:51 2025
 OS/Arch:           linux/amd64
 Context:           default

Server: Docker Desktop
 Engine:
  Version:          24.0.6
  API version:      1.43 (minimum version 1.12)
  Go version:       go1.20.7
  Git commit:       1a79695
  Built:            Mon Sep  4 12:32:16 2023
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.22
  GitCommit:        8165feabfdfe38c65b599c4993d227328c231fca
 runc:
  Version:          1.1.8
  GitCommit:        v1.1.8-0-g82f18fe
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab06$ docker run hello-wirld
Unable to find image 'hello-wirld:latest' locally
^Cuniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab06$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```

Скрипт `audit.sh` уже являлся исполяемым, что можно увидеть по битам прав доступа:

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab06$ ls -l audit.sh
-rwxr-xr-x 1 uniqm uniqm 9700 Dec 14 22:55 audit.sh
```

- [X] 3. Развернуть уязвимое приложение как отдельные стенды

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab06$ docker container ps
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS              PORTS                    NAMES
c04bd705b990   alpine:latest        "/bin/sh -c 'apk add…"   5 seconds ago    Up 4 seconds                                 debug-shell
e1e94b3862a6   nginx:latest         "/docker-entrypoint.…"   29 seconds ago   Up 29 seconds                                vulnerable-web
aa8fe9748c72   python:3.11-alpine   "sh -lc 'pip install…"   2 minutes ago    Up About a minute   0.0.0.0:5001->5000/tcp   vulnerable-app
2449d724abcd   postgres:16-alpine   "docker-entrypoint.s…"   2 minutes ago    Up About a minute   0.0.0.0:5432->5432/tcp   insecure-db
```

- [X] 4. Запустите скрипт из `venv` и проанализируйте то, что вывело на терминале и что вывело при конвертировании

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install openpyxl odfpy
$ ./audit.sh
$ deactivate # или $ deactivate 2>/dev/null || true
```

В итоге было проведено 105 проверок, а общая оценка безопасности составила -10 очков.

- [X] 5. Проведите анализ уязвимостей, опишите их причину возникновения

* [x] **5. Проведите анализ уязвимостей, опишите их причину возникновения (актуально для нашего стенда)**

Ниже только применимые уязвимости:

### 5.1. `docker-compose.yml`

#### `insecure-db` (PostgreSQL)

**Слабый пароль и секреты в открытом виде**

* **Причина:** `POSTGRES_PASSWORD=root` задан в `environment` (простое значение + хранится в YAML).
* **Почему это плохо:** пароль легко подобрать/угадать; утечка через `docker inspect`, логи, репозиторий/CI → компрометация БД и данных.

**Открытый порт БД наружу**

* **Причина:** `ports: "5432:5432"` без привязки к `127.0.0.1` (по умолчанию биндинг на `0.0.0.0`).
* **Почему это плохо:** БД становится доступной с хоста/сети → рост поверхности атаки (сканирование, брутфорс, эксплуатация CVE).

**Инициализация БД через `init.sql` с хоста**

* **Причина:** `./db/init.sql:/docker-entrypoint-initdb.d/init.sql:ro` (сценарии/пользователи/права задаются SQL-файлом на хосте).
* **Почему это плохо:** при ошибках в `init.sql` можно случайно выдать лишние привилегии (например, суперправа/расширения), а также файл может содержать тестовые креды/данные.

#### `app` (python)

**Секреты в environment и пароль в строке подключения**

* **Причина:** `APP_SECRET_KEY=hardcoded-in-env`, `DB_URL=postgresql://...:root@...` заданы в `environment`.
* **Почему это плохо:** секреты утекут через `docker inspect`, логи, дампы; скомпрометированный `APP_SECRET_KEY` может позволить подделку сессий/токенов, а `DB_URL` даёт прямой доступ к БД.

**Включён DEBUG**

* **Причина:** `DEBUG=true`.
* **Почему это плохо:** повышает риск утечек (детальные ошибки/трейсбеки), иногда открывает отладочные механизмы; облегчает эксплуатацию уязвимостей приложения.

**RW bind mount к коду приложения**

* **Причина:** `volumes: ./app:/app:rw`.
* **Почему это плохо:** при RCE в контейнере атакующий может менять код/скрипты на хосте (закрепление, подмена логики, внедрение бэкдора).

**Нет ограничений ресурсов (CPU/RAM/PIDs)**

* **Причина:** в compose отсутствуют лимиты `cpus`, `mem_limit`, `pids_limit`.
* **Почему это плохо:** DoS хоста (переполнение памяти/процессов, высокая нагрузка CPU) → деградация всех контейнеров и ОС.

**Публичная публикация порта**

* **Причина:** `ports: "5001:5000"` без привязки к `127.0.0.1` (по умолчанию `0.0.0.0`).
* **Почему это плохо:** приложение доступно со всех интерфейсов хоста → выше вероятность внешней эксплуатации уязвимостей приложения.

#### `vulnerable-web` (nginx)

**Отсутствие HEALTHCHECK**

* **Причина:** `healthcheck` не задан ни в образе, ни в compose.
* **Почему это плохо:** сбой/компрометация может быть незаметной; оркестратор не понимает, что сервис деградировал.

### 5.2. `vulnerable-app.yml`

#### `vulnerable-web` (критический профиль)

**privileged: true**

* **Причина:** контейнер запущен в привилегированном режиме.
* **Почему это плохо:** резко ослабляет изоляцию; при компрометации контейнера высока вероятность полного захвата хоста.

**cap_add: ALL**

* **Причина:** добавлены все Linux capabilities.
* **Почему это плохо:** контейнер получает системные возможности, которые обычно запрещены → расширение поверхности атаки и сценариев container escape.

**network_mode: host**

* **Причина:** используется сетевой namespace хоста.
* **Почему это плохо:** теряется изоляция сети; проще перехватывать/слушать сетевые сервисы хоста и обходить сегментацию.

**pid: host**

* **Причина:** используется PID namespace хоста.
* **Почему это плохо:** контейнер видит процессы хоста → упрощается разведка и атаки на процессы (в зависимости от прав).

**apparmor:unconfined / seccomp:unconfined**

* **Причина:** отключены профили AppArmor/Seccomp.
* **Почему это плохо:** снимаются ограничения на syscalls/доступы → выше риск kernel-level эксплуатации и escape.

**/var/run/docker.sock проброшен внутрь контейнера**

* **Причина:** `- /var/run/docker.sock:/var/run/docker.sock`.
* **Почему это плохо:** доступ к Docker API ≈ управление Docker daemon → можно запускать контейнеры с монтированием `/` и получить контроль над хостом.

**/:/hostroot:rw**

* **Причина:** корень хоста примонтирован в контейнер с правом записи.
* **Почему это плохо:** прямой RW доступ к файлам хоста (конфиги, ключи, systemd, cron) → утечка данных и гарантированное закрепление.

**Секреты в environment (ADMIN_PASSWORD/DB_PASSWORD/FLAG)**

* **Причина:** креды и “секрет” заданы прямо в YAML.
* **Почему это плохо:** легко утекут через `docker inspect`, логи, репозиторий; сложно ротировать.

#### `debug-shell` (критический профиль)

**privileged: true + host namespaces (network_mode/pid)**

* **Причина:** контейнер отладки запущен как privileged и разделяет namespaces хоста.
* **Почему это плохо:** фактически “технический бэкдор” — при доступе к контейнеру легко перейти к компрометации хоста.

**Root-доступ по паролю (SSH_PASSWORD=password / PermitRootLogin=yes)**

* **Причина:** пароль и разрешение root-login заданы прямо в команде запуска.
* **Почему это плохо:** тривиальная компрометация через подбор/утечку пароля; затем эскалация до хоста через privileged/hostroot.

**/:/hostroot:rw**

* **Причина:** примонтирован корень хоста на запись.
* **Почему это плохо:** полный доступ к данным и конфигурации хоста → утечка/подмена/закрепление.

### 5.3. Trivy

**CVE/уязвимости базовых образов (nginx:alpine, python:3.11-alpine, postgres:16-alpine)**

* **Причина:** уязвимости в пакетах Alpine и/или зависимостях языка (Python packages, бинарники).
* **Почему это плохо:** при эксплуатации конкретной CVE возможны RCE/DoS/утечки; снижает базовую защищённость контейнеров.
  (Детали — в `./audit_reports/xlsx/*-trivy.xlsx` и `./audit_reports/odt/*-trivy.odt`.)

- [X] 6. Опишите влияния уязвимостей, их сценарий атаки

### 6.1. Критические сценарии (компрометация хоста / полный контроль)

#### Сценарий A: Компрометация хоста через `/var/run/docker.sock` (CR)

**Предпосылка:** злоумышленник получает выполнение команд внутри `vulnerable-web` (RCE/компрометация веба/доступ к shell).
**Ход атаки:**

1. В контейнере доступен `/var/run/docker.sock` (Docker API).
2. Злоумышленник обращается к Docker API и запускает вспомогательный контейнер с расширенными правами и монтированием хоста:

   * `--privileged`
   * `-v /:/host`
3. Далее из этого контейнера: читает/меняет файлы хоста (`/etc/shadow`, `/root/.ssh/authorized_keys`, systemd units, cron).
   В итоге полная компрометация узла, закрепление, чтение и подмена данных, компрометация всех контейнеров на хосте.

#### Сценарий B: Выход на уровень хоста через `privileged + cap_add=ALL + seccomp unconfined` (CR)

**Предпосылка:** злоумышленник получил доступ в контейнер `vulnerable-web`.
**Ход атаки:**

1. Контейнер работает почти без ограничений (`privileged`, все capabilities, снят seccomp, AppArmor unconfined).
2. Злоумышленник использует расширенные системные возможности (опасные syscalls, доступ к устройствам, изменение kernel-настроек, эксплуатация ядра/драйверов).
3. Получает выполнение на хосте или доступ к его пространствам имён/устройствам.
   **Влияние:** полный захват хоста или эквивалентный уровень контроля, обход контейнерной изоляции.

#### Сценарий C: Прямая компрометация хоста через `/:/hostroot:rw` (CR)

**Предпосылка:** злоумышленник получил доступ к контейнеру `vulnerable-web`.
**Ход атаки:**

1. На контейнер смонтирован корень файловой системы хоста в режиме RW.
2. Злоумышленник:

   * читает секреты (SSH keys, токены, конфиги),
   * подменяет бинарники/скрипты,
   * добавляет пользователя/ключи в `/etc/passwd`, `/etc/shadow`,
   * внедряет backdoor в systemd/cron.
     **Влияние:** нарушение конфиденциальности и целостности хоста, быстрое закрепление и развитие атаки до полного контроля.

### 6.2. Сценарии lateral movement и сетевые атаки

#### Сценарий D: Сетевой перехват/сканирование через `network_mode: host` (DL/CR)

**Предпосылка:** злоумышленник внутри `vulnerable-web`.
**Ход атаки:**

1. Из-за `host network` контейнер в сетевом пространстве хоста.
2. Атакующий:

   * сканирует локальные порты хоста (включая сервисы, не опубликованные наружу),
   * пытается перехватывать/анализировать трафик (в зависимости от возможностей и наличия инструментов),
   * атакует соседние сервисы на `127.0.0.1` хоста (которые обычно недоступны из bridge-сети).
     **Влияние:** повышение вероятности компрометации внутренних сервисов, облегчение lateral movement, возможная утечка сетевых данных.

#### Сценарий E: Разведка и атаки на процессы хоста через `pid: host` (DL/CR)

**Предпосылка:** злоумышленник внутри `vulnerable-web`.
**Ход атаки:**

1. Контейнер видит процессы хоста (`ps`, `/proc`).
2. Атакующий получает информацию о сервисах/аргументах запуска/путях, может точнее подбирать эксплойты.
3. В некоторых условиях — отправляет сигналы процессам, пытается вмешиваться в работу сервисов.
   **Влияние:** облегчение разведки и подготовки атак, потенциальное нарушение доступности и целостности.

### 6.3. Сценарии утечки секретов и компрометации данных

#### Сценарий F: Утечка секретов через переменные окружения (DL)

**Предпосылка:** злоумышленник получил доступ к Docker API/хосту или к контейнеру (или к CI/репозиторию/логам).
**Ход атаки:**

1. Секреты лежат в `environment` (`ADMIN_PASSWORD`, `DB_PASSWORD`, `FLAG`, `APP_SECRET_KEY`, `DB_URL`).
2. Их можно извлечь через:

   * `docker inspect`,
   * чтение `/proc/1/environ` внутри контейнера,
   * логи/дампы,
   * утечки из git/compose.
3. Далее атакующий использует креды:

   * подключается к БД,
   * подделывает сессии/токены (если секрет — ключ подписи),
   * расширяет доступ внутри инфраструктуры.
     **Влияние:** утечка данных, компрометация учётных записей, масштабирование атаки на БД/другие сервисы.

#### Сценарий G: Компрометация БД через публикацию порта на `0.0.0.0` и слабые учетные данные (DL/CR)

**Предпосылка:** порт БД опубликован наружу (`0.0.0.0:5432->5432`) или доступен из сети, и используются слабые/утекшие креды.
**Ход атаки:**

1. Атакующий находит открытый порт 5432 (скан).
2. Пробует/получает пароль (root/из env/из compose).
3. Подключается к Postgres, читает/меняет данные, создаёт бэкдор-роль.
   **Влияние:** нарушение конфиденциальности (утечка), целостности (подмена), доступности (удаление/шифрование).

### 6.4. Сценарии отказа в обслуживании и деградации

#### Сценарий H: DoS хоста из-за отсутствия лимитов CPU/RAM/PIDs (DL)

**Предпосылка:** атакующий может инициировать тяжёлые операции в приложении или имеет shell в контейнере.
**Ход атаки:**

1. Контейнеры запускаются без ограничений ресурсов (CPU/RAM/PIDs).
2. Атакующий:

   * форкает процессы (fork bomb),
   * потребляет память,
   * загружает CPU бесконечными задачами.
3. Хост и другие контейнеры начинают “задыхаться”, возможен OOM-kill и падение сервисов.
   **Влияние:** отказ в обслуживании стенда, деградация соседних систем на одном хосте.

### 6.5. Операционные риски (детектирование/устойчивость)

#### Сценарий I: Скрытая деградация/компрометация из-за отсутствия `HEALTHCHECK` (DL)

**Предпосылка:** сервис частично сломан или подменён (например, после атаки).
**Ход атаки:**

1. Нет healthcheck, оркестратор не различает “процесс жив” и “сервис работает корректно”.
2. Компрометированный контейнер может продолжать отвечать “как будто всё нормально”, либо сервис деградирует без автоматического восстановления.
   **Влияние:** ухудшение обнаружения инцидента и MTTR, повышенные последствия атак/сбоев.

- [X] 7. Оцените риски ИБ и предложите меры для их снижения: 

### 7.1. Разбор `docker-compose.yml` (что небезопасно и почему)

**1) insecure-db (PostgreSQL)**

* `POSTGRES_PASSWORD=root` / креды в `environment`
  **Почему небезопасно:** секреты в открытом виде (утечки через git, `docker inspect`, логи), пароль слабый.
  **Риск:** **DL высокий** (утечка данных БД), **CR средний** (через БД иногда дальше атакуют приложение/хост).
* `ports: "5432:5432"`
  **Почему:** публикация БД наружу увеличивает поверхность атаки (скан/брут/эксплойты).
  **Риск:** **DL высокий**, CR повышается при слабых кредах.

**2) app (python)**

* `APP_SECRET_KEY=hardcoded-in-env`, `DB_URL` с паролем, `DEBUG=true`
  **Почему:** секреты утекут; debug-режим часто даёт избыточные ошибки/информацию и иногда RCE при ошибочной конфигурации.
  **Риск:** **DL высокий**, **CR средний/высокий** (если уязвимость в приложении → shell в контейнере → развитие атаки на БД/окружение).
* `volumes: ./app:/app:rw` + установка пакетов в runtime
  **Почему:** контейнер может модифицировать код на хосте (подмена/закладки), непредсказуемость поставки (supply chain).
  **Риск:** DL/CR повышаются.

**3) vulnerable-web (nginx)**

* Проброс порта `8080:80` на `0.0.0.0`
  **Почему:** сервис доступен извне; при уязвимостях в приложении/конфиге — точка входа.

### 7.2. Разбор `vulnerable-app.yml` (что небезопасно и почему)

**1) vulnerable-web**

* `privileged: true` + `cap_add: [ALL]`
  **Почему:** контейнер почти равен root на хосте; резкое падение изоляции.
  **Риск:** **CR очень высокий**.
* `network_mode: host`, `pid: host`
  **Почему:** доступ к сети/процессам хоста → разведка, lateral movement, упрощение атак.
  **Риск:** **CR высокий**, **DL высокий**.
* `security_opt: apparmor:unconfined`, `seccomp:unconfined`
  **Почему:** сняты штатные ограничения безопасности.
  **Риск:** **CR высокий**.
* `volumes: /:/hostroot:rw`
  **Почему:** прямой RW доступ к файловой системе хоста.
  **Риск:** **CR/DL очень высокий**.
* `volumes: /var/run/docker.sock:/var/run/docker.sock`
  **Почему:** доступ к Docker API = фактически root на хосте.
  **Риск:** **CR максимальный**.
* секреты в `environment` (`ADMIN_PASSWORD`, `DB_PASSWORD`, `FLAG`)
  **Почему:** утечки через repo/inspect/logs.
  **Риск:** **DL высокий**.
* `image: nginx:latest`
  **Почему:** плавающая версия → непредсказуемость/уязвимости.
  **Риск:** операционный (качество/безопасность).

**2) debug-shell**

* `privileged`, `host network`, `host pid`, `user: 0:0`
  **Почему:** отладочный контейнер фактически “бэкдор” к хосту при любом доступе.
  **Риск:** **CR очень высокий**.
* `openssh-server` + пароль/`PermitRootLogin=yes`
  **Почему:** простой пароль + root login → лёгкий захват.
  **Риск:** **CR очень высокий**, **DL высокий**.
* `/ :/hostroot:rw`
  **Почему:** полный доступ к ФС хоста.
  **Риск:** **CR/DL очень высокий**.

### 7.3. Исправленные `.yaml`

####  `docker-compose.yml`

* БД не публикуем наружу (доступна только внутри сети compose).
* Секреты — через `.env`.
* Приложение запускаем не в DEBUG, код монтируем `ro`, добавляем tmpfs, лимиты.

```yaml
version: "3.8"

services:
  vulnerable-web:
    image: nginx:alpine
    container_name: vulnerable-nginx
    depends_on:
      - insecure-db
      - app
    ports:
      - "127.0.0.1:8080:80"   # ограничили интерфейс (только локально)
    volumes:
      - ./config/nginx.conf:/etc/nginx/nginx.conf:ro
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /var/cache/nginx:rw,mode=1777
      - /var/run:rw,mode=1777
      - /tmp:rw,mode=1777
    cap_drop:
      - ALL
    restart: unless-stopped

  insecure-db:
    image: postgres:16-alpine
    container_name: insecure-db
    environment:
      - POSTGRES_DB=vulnapp
      - POSTGRES_USER=vulnuser
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}   # из .env
    # ports: [удалено]  # не публикуем наружу
    volumes:
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    restart: unless-stopped

  app:
    image: python:3.11-alpine
    container_name: vulnerable-app
    depends_on:
      - insecure-db
    working_dir: /app
    volumes:
      - ./app:/app:ro   # только чтение
    command: ["sh", "-lc", "pip install --no-cache-dir -r requirements.txt && python app.py"]
    environment:
      - APP_SECRET_KEY=${APP_SECRET_KEY}         # из .env
      - DB_URL=${DB_URL}                         # из .env
      - DEBUG=false
    ports:
      - "127.0.0.1:5001:5000"
    read_only: true
    tmpfs:
      - /tmp:rw,mode=1777
    restart: unless-stopped
```

### `vulnerable-app.yml`

Убраем то, что даёт CR почти гарантированно: `docker.sock`, `/:/hostroot`, `privileged`, `host network/pid`, unconfined профили, root+SSH.

```yaml
version: "3.8"

services:
  vulnerable-web:
    image: nginx:alpine
    container_name: vulnerable-web
    restart: unless-stopped
    ports:
      - "127.0.0.1:8080:80"
    environment:
      - ADMIN_USERNAME=${ADMIN_USERNAME}
      - ADMIN_PASSWORD=${ADMIN_PASSWORD}
    volumes:
      - ./config/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./backup:/var/backups:rw
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /var/cache/nginx:rw,mode=1777
      - /var/run:rw,mode=1777
      - /tmp:rw,mode=1777
    cap_drop:
      - ALL

  debug-shell:
    image: alpine:latest
    container_name: debug-shell
    profiles: ["debug"]     # запускается только так: docker compose --profile debug up
    command: ["sh", "-lc", "sleep infinity"]
    security_opt:
      - no-new-privileges:true
    read_only: true
    tmpfs:
      - /tmp:rw,mode=1777
    cap_drop:
      - ALL
```

Итоговый свод мер: 

1. Убрать **docker.sock**, `/:/hostroot`, `privileged`, `cap_add: ALL`, `host network/pid`, `unconfined`.
2. Секреты не хранить в yaml: минимум `.env`, лучше secrets/vault.
3. Не публиковать БД наружу, либо биндинг на `127.0.0.1`.
4. `read_only + tmpfs`, `no-new-privileges`, `cap_drop: [ALL]`.
5. `DEBUG=false`, healthcheck (по желанию), лимиты ресурсов (если требуют).

- [X] 8. Сделайте анализ уязвимостей из сгенерированных файлов .odt, .xslx и опишите их в отчете. Файлы конвертируются в эти директории

* **`audit_reports/xlsx/docker-bench-security-trivy.xlsx`** — по образу `docker/docker-bench-security:latest` обнаружены 3 уязвимости уровня ОС (все HIGH) в пакетах `musl`, `libproc`, `openssl`; образ основан на Alpine 3.8 (EOL), поэтому патчи для него ограничены, корректная мера — обновлять базовый образ/пакеты.

* **`audit_reports/xlsx/nginx-alpine-trivy.xlsx`** — по образу `nginx:alpine` уязвимости не выявлены (Trivy отработал детект ОС/пакетов без находок).

* **`audit_reports/xlsx/python-3.11-alpine-trivy.xlsx`** — найдено 1 уязвимость MEDIUM в `pip` (проблема с проверками при распаковке симлинков), фиксируется обновлением `pip` до 25.3 (в образе стояла более старая версия).

* **`audit_reports/xlsx/postgres-16-alpine-trivy.xlsx`** — обнаружено 12 уязвимостей в составе Go-бинарей внутри образа (10 HIGH, 2 MEDIUM, все со статусом *fixed*), т.е. требуется обновление образа до сборки с более свежим Go/toolchain.

- [X] 9. Подготовьте отчет `gist`.
- [X] 10. Почистите кеш от `venv` и остановите уязвимостей приложение, почистите контейнера

Copyright (c) 2025 Nikita Sergeev
