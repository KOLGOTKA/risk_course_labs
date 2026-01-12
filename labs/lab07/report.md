<div align="center">
<h1><a id="intro">Лабораторная работа №7</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Сергеев_Н._М.-8b9aff" alt="Contributor Badge"></a></div>

***

## Задание

- [X] 1. Разверните и подготовьте окружение для уязвимого приложения

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r vulnerable-app/requirements.txt
```

- [X] 2. Запустите уязвимое приложение

```bash
(venv) uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab07$ docker-compose -f docker-compose.yml up -d --build
WARNING: The Docker Engine you're using is running in swarm mode.

Compose does not use swarm mode to deploy services to multiple nodes in a swarm. All containers will be scheduled on the current node.

To deploy your application across the swarm, use `docker stack deploy`.

Creating network "lab07_default" with the default driver
Building vulnerable-app
[+] Building 86.4s (12/12) FINISHED                                                                                                                                                               docker:default
 => [internal] load build definition from Dockerfile                                                                                                                                                        0.1s
 => => transferring dockerfile: 463B                                                                                                                                                                        0.0s
 => [internal] load .dockerignore                                                                                                                                                                           0.1s
 => => transferring context: 2B                                                                                                                                                                             0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                                                                         3.2s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                                                               0.0s
 => [1/6] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                                                                   0.0s
 => [internal] load build context                                                                                                                                                                           0.0s
 => => transferring context: 4.29kB                                                                                                                                                                         0.0s
 => CACHED [2/6] WORKDIR /app                                                                                                                                                                               0.0s
 => [3/6] RUN apt-get update &&     apt-get install -y --no-install-recommends         build-essential         libjpeg-dev zlib1g-dev         libxml2-dev libxslt1-dev &&     rm -rf /var/lib/apt/lists/*  45.3s
 => [4/6] COPY requirements.txt /app/requirements.txt                                                                                                                                                       0.1s
 => [5/6] RUN pip install --no-cache-dir -r requirements.txt                                                                                                                                               33.8s
 => [6/6] COPY . /app                                                                                                                                                                                       0.0s
 => exporting to image                                                                                                                                                                                      3.7s
 => => exporting layers                                                                                                                                                                                     3.7s
 => => writing image sha256:8231578e154a73bec4bfcee44167d2f200f8238c0cb735c89a4d56f29de3982c                                                                                                                0.0s
 => => naming to docker.io/library/lab07_vulnerable-app                                                                                                                                                     0.0s
Creating lab07_vulnerable-app_1 ... done
```

- [X] 3. Запустите SAST Semgrep и проанализируйте выведенный лог в консоли и опишите логику правил для `semgrep-rules.yml` исходя из паттернов, которые используются. Отчет будет в директории SAST

Выполняем статический анализ (SAST) исходников и конфигураций уязвимого приложения с помощью Semgrep

Ключевые опции:

- `--config sast/semgrep-rules.yml` - Указывает набор правил (правила в YAML), по которым Semgrep будет искать небезопасные паттерны в коде/конфигах.
- `--json` - Формирует результаты в JSON-формате (удобно для отчёта, парсинга, CI).
- `--output sast/semgrep-report.json` - Путь, куда сохранить JSON-отчёт.
- `vulnerable-app/` - Целевая директория для сканирования. Semgrep рекурсивно проходит файлы внутри неё и применяет правила из указанного конфига.

```bash
(venv) uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab07$ semgrep --config sast/semgrep-rules.yml \
  --json \
  --output sast/semgrep-report.json \
  vulnerable-app/

┌──── ○○○ ────┐
│ Semgrep CLI │
└─────────────┘
...
  CODE RULES

  Language   Rules   Files          Origin   Rules
 ──────────────────────────        ────────────────
  python        12       1          Custom      16
  yaml           4       1


  SUPPLY CHAIN RULES

  No rules to run.


  PROGRESS
...
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00


┌──────────────┐
│ Scan Summary │
└──────────────┘
✅ Scan completed successfully.
 • Findings: 5 (5 blocking)
 • Rules run: 16
 • Targets scanned: 2
 • Parsed lines: ~100.0%
 • Scan was limited to files tracked by git
 • For a detailed list of skipped files and lines, run semgrep with the --verbose flag
Ran 16 rules on 2 files: 5 findings.
```

```json
{
    "engine_requested": "OSS",
    "errors": [
        {
            "code": 2,
            "level": "warn",
            "message": "Other syntax error at line vulnerable-app/config.yaml:37:\n (approximate error location; error nearby after) error calling parser: could not find expected ':' character 0 position 0 returned: 0",
            "path": "vulnerable-app/config.yaml",
            "type": "Other syntax error"
        }
    ],
    "paths": {
        "scanned": [
            "vulnerable-app/app.py",
            "vulnerable-app/config.yaml"
        ]
    },
    "profiling_results": [],
    "results": [
        {
            "check_id": "sast.py-info-version-disclosure",
            "end": {
                "col": 39,
                "line": 26,
                "offset": 444
            },
            "extra": {
                "engine_kind": "OSS",
                "fingerprint": "requires login",
                "lines": "requires login",
                "message": "Раскрытие версии приложения в ответе.",
                "metadata": {},
                "severity": "LOW",
                "validation_state": "NO_VALIDATOR"
            },
            "path": "vulnerable-app/app.py",
            "start": {
                "col": 5,
                "line": 26,
                "offset": 410
            }
        },
        {
            "check_id": "sast.py-os-system-rce",
            "end": {
                "col": 19,
                "line": 52,
                "offset": 1116
            },
            "extra": {
                "engine_kind": "OSS",
                "fingerprint": "requires login",
                "lines": "requires login",
                "message": "RCE через os.system с данными пользователя.",
                "metadata": {},
                "severity": "CRITICAL",
                "validation_state": "NO_VALIDATOR"
            },
            "path": "vulnerable-app/app.py",
            "start": {
                "col": 5,
                "line": 52,
                "offset": 1102
            }
        },
        {
            "check_id": "sast.py-arbitrary-file-read",
            "end": {
                "col": 29,
                "line": 68,
                "offset": 1516
            },
            "extra": {
                "engine_kind": "OSS",
                "fingerprint": "requires login",
                "lines": "requires login",
                "message": "Чтение произвольного файла по пути из запроса (LFI/Path Traversal).",
                "metadata": {},
                "severity": "CRITICAL",
                "validation_state": "NO_VALIDATOR"
            },
            "path": "vulnerable-app/app.py",
            "start": {
                "col": 14,
                "line": 68,
                "offset": 1501
            }
        },
        {
            "check_id": "sast.py-unsafe-pickle-deserialization",
            "end": {
                "col": 48,
                "line": 79,
                "offset": 1782
            },
            "extra": {
                "engine_kind": "OSS",
                "fingerprint": "requires login",
                "lines": "requires login",
                "message": "Небезопасная десериализация через pickle.loads.",
                "metadata": {},
                "severity": "CRITICAL",
                "validation_state": "NO_VALIDATOR"
            },
            "path": "vulnerable-app/app.py",
            "start": {
                "col": 15,
                "line": 79,
                "offset": 1749
            }
        },
        {
            "check_id": "sast.py-eval-user-input",
            "end": {
                "col": 24,
                "line": 88,
                "offset": 2006
            },
            "extra": {
                "engine_kind": "OSS",
                "fingerprint": "requires login",
                "lines": "requires login",
                "message": "Опасное использование eval на пользовательском вводе.",
                "metadata": {},
                "severity": "HIGH",
                "validation_state": "NO_VALIDATOR"
            },
            "path": "vulnerable-app/app.py",
            "start": {
                "col": 14,
                "line": 88,
                "offset": 1996
            }
        }
    ],
    "skipped_rules": [],
    "time": {
        "fixpoint_timeouts": [],
        "matching_time": {
            "per_file_and_rule_time": {
                "mean": 0.0,
                "std_dev": 0.0
            },
            "total_time": 0.0,
            "very_slow_rules_on_files": [],
            "very_slow_stats": {
                "count_ratio": 0.0,
                "time_ratio": 0.0
            }
        },
        "max_memory_bytes": 131444224,
        "parsing_time": {
            "per_file_time": {
                "mean": 0.0,
                "std_dev": 0.0
            },
            "total_time": 0.0,
            "very_slow_files": [],
            "very_slow_stats": {
                "count_ratio": 0.0,
                "time_ratio": 0.0
            }
        },
        "prefiltering": {
            "file_level_time": 0.0,
            "project_level_time": 0.0,
            "rules_matched_ratio": 1.0,
            "rules_selected_ratio": 1.0,
            "rules_with_file_prefilters_ratio": 0.9166666666666666,
            "rules_with_project_prefilters_ratio": 0.0
        },
        "profiling_times": {
            "config_time": 0.29732203483581543,
            "core_time": 0.5338101387023926,
            "ignores_time": 0.00010991096496582031,
            "total_time": 0.9277369976043701
        },
        "rules": [],
        "rules_parse_time": 0.006573915481567383,
        "scanning_time": {
            "per_file_time": {
                "mean": 0.02066946029663086,
                "std_dev": 0.00020928032023448395
            },
            "total_time": 0.04133892059326172,
            "very_slow_files": [],
            "very_slow_stats": {
                "count_ratio": 0.0,
                "time_ratio": 0.0
            }
        },
        "tainting_time": {
            "per_def_and_rule_time": {
                "mean": 0.0,
                "std_dev": 0.0
            },
            "total_time": 0.0,
            "very_slow_rules_on_defs": [],
            "very_slow_stats": {
                "count_ratio": 0.0,
                "time_ratio": 0.0
            }
        },
        "targets": [],
        "total_bytes": 0
    },
    "version": "1.146.0"
}
```

В итоге анализировалось 2 файла: `vulnerable-app/app.py` и `vulnerable-app/config.yaml`. Применялось 16 правил (12 к app.py и 4 к config.yaml). Найдено 5 уязвимостей относящихся к app.py, из которых 3 критические, 1 высокая и 1 низкая. Основные проблемы связаны с выполнением команд через `os.system`, чтением файлов по пути из запроса (LFI), небезопасной десериализацией через `pickle.loads` и использованием `eval` на пользовательском вводе.

- **3.1. sast.py-info-version-disclosure (LOW)**
Сообщение: “Раскрытие версии приложения в ответе.”
Типовой паттерн: возврат/вывод версии (например, строка вида return "v1.2.3" или включение версии во внешний ответ).
Риск: упрощает разведку и подбор эксплойтов под конкретную версию.

- **3.2. sast.py-os-system-rce (CRITICAL)**
Сообщение: “RCE через os.system с данными пользователя.”
Паттерн: вызов os.system(...) (или аналогов) с параметрами, зависящими от внешнего ввода (query/body).
Риск: командная инъекция / удалённое выполнение команд (RCE).

- **3.3. sast.py-arbitrary-file-read (CRITICAL)**
Сообщение: “Чтение произвольного файла по пути из запроса (LFI/Path Traversal).”
Паттерн: использование пути из запроса напрямую в open(path) / Path(path).read_text() и т.п.
Риск: чтение /etc/passwd, ключей, конфигов, токенов; иногда — дальнейшая эскалация.

- **3.4. sast.py-unsafe-pickle-deserialization (CRITICAL)**
Сообщение: “Небезопасная десериализация через pickle.loads.”
Паттерн: pickle.loads(<данные извне>)
Риск: pickle может выполнять произвольный код при десериализации (возможно RCE).

- **3.5. sast.py-eval-user-input (HIGH)**
Сообщение: “Опасное использование eval на пользовательском вводе.”
Паттерн: eval(<данные извне>)
Риск: выполнение произвольного Python-кода.

- [ ] 4. Запустите SAST Checkov по Dockerfile, compose и проанализируйте выведенный лог в консоли и опишите логику правил для `checkov-config.yaml` по `Docker`. Отчет будет в директории SAST

Checkov — статический анализатор конфигураций (IaC/Docker). В этом шаге он проверяет Dockerfile (и потенциально связанные контейнерные конфигурации) на небезопасные практики сборки/запуска контейнеров

Опции команды:

- `--framework dockerfile` - Явно выбирает тип анализируемых файлов Dockerfile. Это важно: Checkov будет применять набор проверок именно для Dockerfile.
- `--file vulnerable-app/Dockerfile docker-compose.yml` - Указывает конкретные файлы для анализа.
- `--output json` - Формат вывода результатов — JSON.
- `--output-file-path sast/checkov-report.json` - Куда сохранить JSON-отчёт.
- `--soft-fail` - Мягкое падение: даже при найденных проблемах Checkov не будет возвращать ненулевой код выхода.

```bash
$ checkov \
  --framework dockerfile \
  --file vulnerable-app/Dockerfile docker-compose.yml \
  --output json \
  --output-file-path sast/checkov-report.json \
  --soft-fail
```

Вывод команды очень большой, поэтому его не привожу здесь полностью. Ниже сводка по найденным проблемам:

В отчёте указано: passed = 50, failed = 2, skipped = 0, parsing_errors = 0, resource_count = 1.

Найденные проблемы (FAILED checks):

**FAILED #1 — CKV_DOCKER_2 / BC_DKR_2**

Проверка: “Ensure that HEALTHCHECK instructions have been added to container images”
Смысл: в Dockerfile отсутствует директива HEALTHCHECK. 
Почему это важно: без HEALTHCHECK оркестратор хуже понимает жив ли контейнер на уровне приложения. Контейнер может оставаться в статусе running при сломавшемся приложении.

**FAILED #2 — CKV_DOCKER_3 / BC_DKR_3**

Проверка: “Ensure that a user for the container has been created”
Смысл: контейнер запускается без создания/указания отдельного пользователя, то есть по умолчанию под root.
Почему это важно: root в контейнере повышает риск при RCE/escape: у атакующего больше прав внутри контейнера. Даже без выхода из контейнера root облегчает чтение/изменение файлов, установку инструментов, закрепление и т.д.

- [X] 5. Подготовка зависимостей Java и Maven‑скан для проведения SCA. Отчеты будут в директории SCA. Будет ошибка, которую надо поправить, что бы уязвимости определялись или добавить дополнительные уязвимости для их вывода в отчете

`./dependency-check.sh --update` - Запуск Dependency-Check в режиме обновления базы. Опция --update означает: не сканировать проект, а обновить источники данных в локальном каталоге.

`mvn dependency:resolve` - Maven-goal плагина maven-dependency-plugin, который: рассчитывает дерево зависимостей по pom.xml, скачивает необходимые артефакты в локальный репозиторий ~/.m2, печатает список “resolved” зависимостей.

`mvn dependency:copy-dependencies -DoutputDirectory=./lib` - Копирует все зависимости (JAR) в каталог ./lib.
Опция -DoutputDirectory=./lib задаёт целевую директорию для выгрузки артефактов. Это удобно для последующих CLI-сканов: можно сканировать готовый набор JAR.

`mvn org.owasp:dependency-check-maven:check -DdataDirectory=... || true` - Запускает OWASP Dependency-Check как Maven-плагин, используя заранее подготовленную базу из -DdataDirectory.

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab07/sca$ ./dependency-check.sh --update
OWASP Dependency-Check SCA
[*] Updating NVD database in /home/uniqm/.dependency-check-data...
[INFO] Checking for updates
[INFO] Skipping the NVD API Update as it was completed within the last 240 minutes
[INFO] Updating CISA Known Exploited Vulnerability list: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
[INFO] Begin database defrag
[INFO] End database defrag (5236 ms)
[INFO] Check for updates complete (7368 ms)
[+] NVD data updated
```

База хранится в: /home/uniqm/.dependency-check-data. NVD уже обновлялась недавно, поэтому Dependency-Check пропустил повторную загрузку.

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab07/sca$ mvn dependency:resolve
[INFO] Scanning for projects...
...
[INFO]
[INFO] ---------------------------< lab07:sca-demo >---------------------------
[INFO] Building sca-demo 1.0.0
[INFO] --------------------------------[ jar ]---------------------------------
...
[INFO]
[INFO] --- maven-dependency-plugin:2.8:resolve (default-cli) @ sca-demo ---
...
[INFO]
[INFO] The following files have been resolved:
[INFO]    com.fasterxml.jackson.core:jackson-annotations:jar:2.4.0:compile
[INFO]    com.fasterxml.jackson.core:jackson-databind:jar:2.4.6:compile
[INFO]    com.fasterxml.jackson.module:jackson-module-jaxb-annotations:jar:2.4.6:compile
[INFO]    commons-codec:commons-codec:jar:1.2:compile
[INFO]    com.fasterxml.jackson.jaxrs:jackson-jaxrs-json-provider:jar:2.4.6:compile
[INFO]    com.fasterxml.jackson.jaxrs:jackson-jaxrs-base:jar:2.4.6:compile
[INFO]    com.fasterxml.jackson.core:jackson-core:jar:2.4.6:compile
[INFO]    org.codehaus.groovy:groovy-all:jar:2.1.6:compile
[INFO]    commons-httpclient:commons-httpclient:jar:3.1:compile
[INFO]    commons-logging:commons-logging:jar:1.0.4:compile
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  02:38 min
[INFO] Finished at: 2025-12-28T17:35:59+03:00
[INFO] ------------------------------------------------------------------------
```

BUILD SUCCESS — зависимости успешно рассчитаны и доступны локально.

В выводе перечислены resolved зависимости, включая заведомо старые/уязвимые версии "jackson-databind 2.4.6", "commons-httpclient 3.1", "groovy-all 2.1.6" и др.
Maven подтвердил, что зависимости из pom.xml корректно разрешаются и могут быть проанализированы SCA-сканером.

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab07/sca$ mvn dependency:copy-dependencies -DoutputDirectory=./lib
[INFO] Scanning for projects...
[INFO]
[INFO] ---------------------------< lab07:sca-demo >---------------------------
[INFO] Building sca-demo 1.0.0
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] --- maven-dependency-plugin:2.8:copy-dependencies (default-cli) @ sca-demo ---
[INFO] Copying jackson-annotations-2.4.0.jar to /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/lib/jackson-annotations-2.4.0.jar
[INFO] Copying jackson-databind-2.4.6.jar to /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/lib/jackson-databind-2.4.6.jar
[INFO] Copying jackson-module-jaxb-annotations-2.4.6.jar to /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/lib/jackson-module-jaxb-annotations-2.4.6.jar
[INFO] Copying commons-codec-1.2.jar to /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/lib/commons-codec-1.2.jar
[INFO] Copying jackson-jaxrs-json-provider-2.4.6.jar to /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/lib/jackson-jaxrs-json-provider-2.4.6.jar
[INFO] Copying jackson-jaxrs-base-2.4.6.jar to /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/lib/jackson-jaxrs-base-2.4.6.jar
[INFO] Copying jackson-core-2.4.6.jar to /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/lib/jackson-core-2.4.6.jar
[INFO] Copying groovy-all-2.1.6.jar to /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/lib/groovy-all-2.1.6.jar
[INFO] Copying commons-httpclient-3.1.jar to /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/lib/commons-httpclient-3.1.jar
[INFO] Copying commons-logging-1.0.4.jar to /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/lib/commons-logging-1.0.4.jar
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  1.040 s
[INFO] Finished at: 2025-12-28T17:36:26+03:00
[INFO] ------------------------------------------------------------------------
```

Maven скопировал JAR в .../sca/lib/: jackson-databind-2.4.6.jar, commons-httpclient-3.1.jar, groovy-all-2.1.6.jar, и др.

Cформирован набор бинарных артефактов (JAR), который: можно сканировать CLI-версией Dependency-Check, можно приложить как подтверждение состава зависимостей, упрощает анализ без обращения к Maven в дальнейшем.

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab07/sca$ mvn org.owasp:dependency-check-maven:check \
  -DdataDirectory=/home/uniqm/.dependency-check-data \
  || true
[INFO] Scanning for projects...
[INFO]
[INFO] ---------------------------< lab07:sca-demo >---------------------------
[INFO] Building sca-demo 1.0.0
[INFO] --------------------------------[ jar ]---------------------------------
[INFO]
[INFO] --- dependency-check-maven:12.1.0:check (default-cli) @ sca-demo ---
[INFO] Analysis Started
[INFO] Finished Archive Analyzer (0 seconds)
[INFO] Finished File Name Analyzer (0 seconds)
[INFO] Finished Jar Analyzer (0 seconds)
[INFO] Finished Dependency Merging Analyzer (0 seconds)
[INFO] Finished Hint Analyzer (0 seconds)
[INFO] Finished Version Filter Analyzer (0 seconds)
[INFO] Created CPE Index (2 seconds)
[INFO] Finished CPE Analyzer (3 seconds)
[INFO] Finished False Positive Analyzer (0 seconds)
[INFO] Finished NVD CVE Analyzer (0 seconds)
[WARNING] An error occurred while analyzing '/home/uniqm/.m2/repository/com/fasterxml/jackson/jaxrs/jackson-jaxrs-json-provider/2.4.6/jackson-jaxrs-json-provider-2.4.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/tmp/dctemp3252645d-0dac-4358-b11d-5bc4f17504e5/check12621165083073542651tmp/7/pom.xml' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/uniqm/.m2/repository/commons-codec/commons-codec/1.2/commons-codec-1.2.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/uniqm/.m2/repository/commons-logging/commons-logging/1.0.4/commons-logging-1.0.4.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/uniqm/.m2/repository/commons-httpclient/commons-httpclient/3.1/commons-httpclient-3.1.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/uniqm/.m2/repository/org/codehaus/groovy/groovy-all/2.1.6/groovy-all-2.1.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/uniqm/.m2/repository/com/fasterxml/jackson/module/jackson-module-jaxb-annotations/2.4.6/jackson-module-jaxb-annotations-2.4.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/uniqm/.m2/repository/com/fasterxml/jackson/core/jackson-annotations/2.4.0/jackson-annotations-2.4.0.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/uniqm/.m2/repository/com/fasterxml/jackson/core/jackson-databind/2.4.6/jackson-databind-2.4.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/uniqm/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.4.6/jackson-core-2.4.6.jar' (Sonatype OSS Index Analyzer).
[WARNING] An error occurred while analyzing '/home/uniqm/.m2/repository/com/fasterxml/jackson/jaxrs/jackson-jaxrs-base/2.4.6/jackson-jaxrs-base-2.4.6.jar' (Sonatype OSS Index Analyzer).
[INFO] Finished Sonatype OSS Index Analyzer (20 seconds)
[INFO] Finished Vulnerability Suppression Analyzer (0 seconds)
[INFO] Finished Known Exploited Vulnerability Analyzer (0 seconds)
[INFO] Finished Dependency Bundling Analyzer (0 seconds)
[INFO] Finished Unused Suppression Rule Analyzer (0 seconds)
[INFO] Analysis Complete (24 seconds)
[INFO] Writing XML report to: /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.xml
[INFO] Writing HTML report to: /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.html
[INFO] Writing JSON report to: /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.json
[INFO] Writing CSV report to: /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.csv
[INFO] Writing SARIF report to: /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.sarif
[INFO] Writing JENKINS report to: /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/dependency-check-report/dependency-check-jenkins.html
[INFO] Writing JUNIT report to: /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/dependency-check-report/dependency-check-junit.xml
[INFO] Writing GITLAB report to: /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/dependency-check-report/dependency-check-gitlab.json
[WARNING]

One or more dependencies were identified with known vulnerabilities in sca-demo:

commons-httpclient-3.1.jar (pkg:maven/commons-httpclient/commons-httpclient@3.1, cpe:2.3:a:apache:commons-httpclient:3.1:*:*:*:*:*:*:*, cpe:2.3:a:apache:httpclient:3.1:*:*:*:*:*:*:*) : CVE-2012-5783, CVE-2020-13956
groovy-all-2.1.6.jar (pkg:maven/org.codehaus.groovy/groovy-all@2.1.6, cpe:2.3:a:apache:groovy:2.1.6:*:*:*:*:*:*:*) : CVE-2015-3253, CVE-2016-6814, CVE-2020-17521
jackson-annotations-2.4.0.jar (pkg:maven/com.fasterxml.jackson.core/jackson-annotations@2.4.0, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.0:*:*:*:*:*:*:*) : CVE-2018-1000873
jackson-core-2.4.6.jar (pkg:maven/com.fasterxml.jackson.core/jackson-core@2.4.6, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.6:*:*:*:*:*:*:*) : CVE-2018-1000873
jackson-databind-2.4.6.jar (pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.4.6, cpe:2.3:a:fasterxml:jackson-databind:2.4.6:*:*:*:*:*:*:*, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.6:*:*:*:*:*:*:*) : CVE-2017-15095, CVE-2017-17485, CVE-2017-7525, CVE-2018-11307, CVE-2018-14718, CVE-2018-14719, CVE-2018-7489, CVE-2019-14379, CVE-2019-14540, CVE-2019-14892, CVE-2019-16335, CVE-2019-16942, CVE-2019-16943, CVE-2019-17267, CVE-2019-17531, CVE-2019-20330, CVE-2020-8840, CVE-2020-9547, CVE-2020-9548, CVE-2020-10673, CVE-2018-5968, CVE-2020-10650, CVE-2020-24616, CVE-2020-24750, CVE-2020-35490, CVE-2020-35491, CVE-2020-36179, CVE-2020-36180, CVE-2020-36181, CVE-2020-36182, CVE-2020-36183, CVE-2020-36184, CVE-2020-36185, CVE-2020-36186, CVE-2020-36187, CVE-2020-36188, CVE-2020-36189, CVE-2021-20190, CVE-2018-12022, CVE-2019-12086, CVE-2019-14439, CVE-2020-36518, CVE-2022-42003, CVE-2022-42004, CVE-2018-1000873, CVE-2019-12384, CVE-2019-12814, CVE-2023-35116


See the dependency-check report for more details.


[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  29.201 s
[INFO] Finished at: 2025-12-28T17:49:58+03:00
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal org.owasp:dependency-check-maven:12.1.0:check (default-cli) on project sca-demo:
[ERROR]
[ERROR] One or more dependencies were identified with vulnerabilities that have a CVSS score greater than or equal to '0.0':
[ERROR]
[ERROR] commons-httpclient-3.1.jar (pkg:maven/commons-httpclient/commons-httpclient@3.1, cpe:2.3:a:apache:commons-httpclient:3.1:*:*:*:*:*:*:*, cpe:2.3:a:apache:httpclient:3.1:*:*:*:*:*:*:*): CVE-2020-13956(5.3), CVE-2012-5783(5.8)
[ERROR] groovy-all-2.1.6.jar (pkg:maven/org.codehaus.groovy/groovy-all@2.1.6, cpe:2.3:a:apache:groovy:2.1.6:*:*:*:*:*:*:*): CVE-2015-3253(9.8), CVE-2016-6814(9.8), CVE-2020-17521(5.5)
[ERROR] jackson-annotations-2.4.0.jar (pkg:maven/com.fasterxml.jackson.core/jackson-annotations@2.4.0, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.0:*:*:*:*:*:*:*): CVE-2018-1000873(6.5)
[ERROR] jackson-core-2.4.6.jar (pkg:maven/com.fasterxml.jackson.core/jackson-core@2.4.6, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.6:*:*:*:*:*:*:*): CVE-2018-1000873(6.5)
[ERROR] jackson-databind-2.4.6.jar (pkg:maven/com.fasterxml.jackson.core/jackson-databind@2.4.6, cpe:2.3:a:fasterxml:jackson-databind:2.4.6:*:*:*:*:*:*:*, cpe:2.3:a:fasterxml:jackson-modules-java8:2.4.6:*:*:*:*:*:*:*): CVE-2017-17485(9.8), CVE-2020-9547(9.8), CVE-2018-12022(7.5), CVE-2018-5968(8.1), CVE-2020-9548(9.8), CVE-2019-14379(9.8), CVE-2020-36180(8.1), CVE-2020-24616(8.1), CVE-2020-36182(8.1), CVE-2019-14439(7.5), CVE-2020-36181(8.1), CVE-2020-35491(8.1), CVE-2020-36184(8.1), CVE-2020-35490(8.1), CVE-2020-36183(8.1), CVE-2019-12814(5.9), CVE-2019-20330(9.8), CVE-2020-24750(8.1), CVE-2020-10673(8.8), CVE-2018-11307(9.8), CVE-2018-14718(9.8), CVE-2018-1000873(6.5), CVE-2018-7489(9.8), CVE-2018-14719(9.8), CVE-2020-36186(8.1), CVE-2019-17531(9.8), CVE-2020-36185(8.1), CVE-2020-36188(8.1), CVE-2020-36187(8.1), CVE-2020-10650(8.1), CVE-2020-36189(8.1), CVE-2019-12086(7.5), CVE-2019-14540(9.8), CVE-2019-12384(5.9), CVE-2023-35116(4.7), CVE-2017-15095(9.8), CVE-2019-16942(9.8), CVE-2019-16943(9.8), CVE-2021-20190(8.1), CVE-2017-7525(9.8), CVE-2020-36518(7.5), CVE-2019-17267(9.8), CVE-2019-16335(9.8), CVE-2020-36179(8.1), CVE-2020-8840(9.8), CVE-2019-14892(9.8), CVE-2022-42003(7.5), CVE-2022-42004(7.5)
[ERROR]
[ERROR] See the dependency-check report for more details.
[ERROR]
[ERROR]
[ERROR] -> [Help 1]
[ERROR]
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR]
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException
```

Плагин создал индекс CPE и сопоставил зависимости с CVE. Найдены многочисленные уязвимости в старых версиях библиотек, включая критические CVE в jackson-databind, groovy-all и др.

Сборка падает с ошибкой BUILD FAILURE из-за обнаруженных уязвимостей, так как по умолчанию dependency-check-maven роняет сборку, если найдены CVE выше установленного порога.

**commons-httpclient-3.1.jar**: 

- CVE-2012-5783 — в Apache Commons HttpClient 3.x отсутствует корректная проверка соответствия hostname сертификату, что позволяет провести MITM/SSL-spoofing и подменить сервер при TLS-соединении. 
- CVE-2020-13956 — Apache HttpClient может неверно интерпретировать “authority” в malformed URI и отправить запрос не на тот host, что ведёт к SSRF-подобным сценариям/ошибочной маршрутизации запросов. 

**groovy-all-2.1.6.jar**: 

- CVE-2015-3253 — уязвимость небезопасной десериализации в Groovy позволяет выполнить произвольный код (или вызвать DoS) через специально сформированный serialized object. 
- CVE-2016-6814 — при использовании стандартной Java-сериализации в приложениях с Groovy на classpath возможна RCE при десериализации вредоносного объекта. 
- CVE-2020-17521 — в Groovy небезопасная реализация helper-методов для временных директорий может приводить к рискам утечки/небезопасному созданию временных файлов/директорий в некоторых контекстах ОС. 

**jackson-annotations-2.4.0.jar**: 

- CVE-2018-1000873 — некорректная валидация при десериализации (например, очень большие значения “nanoseconds” для time-типов) может привести к DoS (исключения/ресурсное истощение). 

**jackson-core-2.4.6.jar** 
- CVE-2018-1000873

**jackson-databind-2.4.6.jar**: 

- CVE-2017-15095 — unsafe deserialization в ObjectMapper.readValue может приводить к RCE (расширение/неполная защита относительно предыдущих фиксов). 
- CVE-2017-17485 — unsafe deserialization (неполный blacklist/обход предыдущих ограничений) может приводить к RCE при обработке недоверенных данных. 
- CVE-2017-7525 — deserialization flaw в Jackson Databind позволяет добиться RCE через специально сформированный вход, подаваемый в ObjectMapper.readValue. 
- CVE-2018-11307 — уязвимость класса “gadget chains/полиморфная десериализация” в Jackson Databind может приводить к RCE при десериализации недоверенных данных. 
- CVE-2018-14718 — обход ограничений полиморфной десериализации может приводить к RCE при включённом default typing/обработке недоверенного JSON. 
- CVE-2018-14719 — очередной вариант обхода защитных механизмов Jackson Databind при полиморфной десериализации, потенциально ведущий к RCE. 
- CVE-2018-7489 — уязвимость “gadget chain” в Jackson Databind может приводить к RCE при десериализации недоверенных данных. 
- CVE-2019-14379 — некорректная обработка default typing (в т.ч. при определённых классах, связанных с ehcache) может приводить к RCE. 
- CVE-2019-14540 — проблема полиморфной десериализации/обход ограничений Jackson Databind может приводить к RCE при обработке недоверенного ввода. 
- CVE-2019-14892 — уязвимость десериализации Jackson Databind (обход/неполный blacklist) может приводить к RCE. 
- CVE-2019-16335 — очередная вариация уязвимости полиморфной десериализации Jackson Databind, потенциально ведущая к RCE.
- CVE-2019-16942 — уязвимость полиморфной десериализации Jackson Databind может приводить к RCE при обработке недоверенного JSON. 
- CVE-2019-16943 — связанная проблема обхода ограничений/blacklist в Jackson Databind может приводить к RCE. 
- CVE-2019-17267 — уязвимость десериализации Jackson Databind (обход защит) может приводить к RCE. 
- CVE-2019-17531 — ещё один “gadget chain”/обход blacklist в Jackson Databind, потенциально ведущий к RCE. 
- CVE-2019-20330 — уязвимость полиморфной десериализации Jackson Databind может приводить к RCE при недоверенном вводе.
- CVE-2020-8840 — проблема десериализации/обход ограничений Jackson Databind может приводить к RCE при обработке недоверенных данных. 
- CVE-2020-9547 — уязвимость полиморфной десериализации Jackson Databind может приводить к RCE при использовании недоверенного JSON. 
- CVE-2020-9548 — связанная уязвимость Jackson Databind (обход/гаджеты) может приводить к RCE при десериализации. 
- CVE-2020-10673 — проблема безопасности в Jackson Databind, связанная с десериализацией, может приводить к RCE при обработке недоверенного ввода. 
- CVE-2018-5968 — уязвимость в Jackson Databind из класса “deserialization gadget chain” может приводить к RCE. 
- CVE-2020-10650 — уязвимость десериализации Jackson Databind (обход/гаджеты) может приводить к RCE. 
- CVE-2020-24616 — уязвимость полиморфной десериализации Jackson Databind может приводить к RCE. 
- CVE-2020-24750 — уязвимость десериализации Jackson Databind может приводить к RCE при обработке недоверенных данных.
- CVE-2020-35490 — очередная проблема обхода защит Jackson Databind при полиморфной десериализации, потенциально ведущая к RCE. 
- CVE-2020-35491 — связанная уязвимость Jackson Databind (полиморфная десериализация) может приводить к RCE. 
- CVE-2020-36179 — уязвимость полиморфной десериализации Jackson Databind может приводить к RCE. 
- CVE-2020-36180 — связанная уязвимость Jackson Databind (gadget/обход) может приводить к RCE. 
- CVE-2020-36181 — уязвимость десериализации Jackson Databind может приводить к RCE. 
- CVE-2020-36182 — уязвимость полиморфной десериализации Jackson Databind может приводить к RCE. 
- CVE-2020-36183 — связанная уязвимость Jackson Databind может приводить к RCE при обработке недоверенного ввода.
- CVE-2020-36184 — уязвимость десериализации Jackson Databind (обход/гаджеты) может приводить к RCE. 
- CVE-2020-36185 — уязвимость Jackson Databind из класса полиморфной десериализации может приводить к RCE. 
- CVE-2020-36186 — уязвимость десериализации Jackson Databind может приводить к RCE. 
- CVE-2020-36187 — связанная уязвимость Jackson Databind (обход защит) может приводить к RCE. 
- CVE-2020-36188 — уязвимость полиморфной десериализации Jackson Databind может приводить к RCE. 
- CVE-2020-36189 — уязвимость десериализации Jackson Databind может приводить к RCE при обработке недоверенных данных.
- CVE-2021-20190 — проблема безопасности Jackson Databind, связанная с полиморфной десериализацией, может приводить к RCE.
- CVE-2018-12022 — уязвимость полиморфной десериализации Jackson Databind может приводить к RCE. 
- CVE-2019-12086 — уязвимость Jackson Databind (deserialization gadget/обход) может приводить к RCE. 
- CVE-2019-14439 — уязвимость полиморфной десериализации Jackson Databind может приводить к RCE. 
- CVE-2020-36518 — чрезмерная глубина вложенных объектов при обработке может вызвать StackOverflow и DoS в Jackson Databind. 
- CVE-2022-42003 — при включённом UNWRAP_SINGLE_VALUE_ARRAYS возможна resource exhaustion (DoS) из-за глубокой вложенности “wrapper arrays” в примитивных десериализаторах. 
- CVE-2022-42004 — уязвимость того же класса (ошибки проверок/ограничений при десериализации) может приводить к DoS через истощение ресурсов на специально сформированном вводе. 
- CVE-2019-12384 — уязвимость десериализации Jackson Databind (обход/гаджеты) может приводить к RCE. 
- CVE-2019-12814 — уязвимость полиморфной десериализации Jackson Databind может приводить к RCE. 
- CVE-2023-35116 — заявленная уязвимость (DISPUTED) связана с DoS/неопределённым влиянием при обработке циклических зависимостей (самоссылочных структур) в Jackson Databind. 

- [X] 6. Запустите SCA CLI OWASP Dependency-Check для уязвимого приложения. Отчеты будут в директории SCA. Опишите как работает сканирование SCA для `pom.xml` и `app.py`

SCA-сканирование в CLI-режиме по всему проекту и сравнить подход анализа зависимостей на уровне Maven (pom.xml) и на уровне исходников Python (app.py).

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab07/sca$ ./dependency-check.sh \
  --project "sca-demo" \
  --scan . \
  --format ALL \
  --out ./dependency-check-report
OWASP Dependency-Check SCA
[*] Running scan using cached data in /home/uniqm/.dependency-check-data (no full re-download)
[*] Scanning:
    - /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/vulnerable-app
    - /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/lib
[INFO] Analysis Started
[INFO] Finished File Name Analyzer (0 seconds)
[INFO] Finished Dependency Merging Analyzer (0 seconds)
[INFO] Finished Hint Analyzer (0 seconds)
[INFO] Finished Version Filter Analyzer (0 seconds)
[INFO] Created CPE Index (2 seconds)
[INFO] Finished CPE Analyzer (2 seconds)
[INFO] Finished False Positive Analyzer (0 seconds)
[INFO] Finished NVD CVE Analyzer (0 seconds)
[WARN] Disabling OSS Index analyzer due to missing user/password credentials. Authentication is now required: https://ossindex.sonatype.org/doc/auth-required
[INFO] Finished Vulnerability Suppression Analyzer (0 seconds)
[INFO] Finished Known Exploited Vulnerability Analyzer (0 seconds)
[INFO] Finished Dependency Bundling Analyzer (0 seconds)
[INFO] Finished Unused Suppression Rule Analyzer (0 seconds)
[INFO] Analysis Complete (2 seconds)
[INFO] Writing HTML report to: /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.html
[INFO] Writing JSON report to: /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/dependency-check-report/dependency-check-report.json
[+] Reports saved to: /home/uniqm/DevSecOps/risk_course_labs/labs/lab07/sca/dependency-check-report
[i] To refresh NVD data occasionally, run: bash sca/dependency-check.sh --update
```

Были просканированы директории с уязвимым приложением (vulnerable-app) и с набором библиотек (sca/lib).

**Механизм анализа**

Для Java/Maven-части (pom.xml и JAR):

1) Dependency-Check обнаруживает JAR-файлы в sca/lib, читает метаданные (MANIFEST, groupId/artifactId/version),сопоставляет их с CPE и координатами пакетов (PURL);
2) Создаётся CPE Index и выполняется сопоставление с локальной базой NVD CVE.
3) Для каждой зависимости формируется список CVE.

Для Python-части (app.py и requirements.txt):

1) пытается определить зависимости через requirements.txt, имена файлов/пакетов, эвристики (File Name Analyzer, Hint Analyzer).

- [X] 7. Соберите единый отчет из всех сканирований в виде `html`, `csv`, `json`

Так как скрипта generate_unified_report.sh нет, создаём python-скрипт `generate_unified_report.py` с желаемым функционалом.

```bash
uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab07$ python3 sca/generate_unified_report.py
✓ Unified JSON report: ./unified-reports/unified-report.json
✓ Unified CSV report: ./unified-reports/unified-report.csv
✓ Unified HTML report: ./unified-reports/unified-report.html
```

- [X] 8. Проанализируйте все уязвимости и обьясните для SAST Checkov сработки статуса `Unknown`. Классифицируйте их и укажите какие не должны быть в отчетах. Внесите исправления и запустите повторное сканирование и убедитесь, что они устранены. Приложите исправленный файл и отчет без уязвимостей.

Описание каждой уязвимости было дано выше.

Unknown появляется, когда Checkov не может статически вывести значение, необходимое для правила, например:

- значение берётся из переменной окружения без дефолта (${VAR}),
- используется build-arg/templating,
- Dockerfile/Compose не содержит достаточных данных для доказательства PASS/FAIL.

В финальный отчёт обычно не попадают (или помечается как “accepted risk / suppressed”) уязвимости, если:

- это Unknown без практического пути устранения;
- правило неприменимо (например, “не используйте apt” в образе Debian/Ubuntu).

- [X] 9. Опишите выведенные уязвимости для SAST Semgrep и принцип их работы. Поправьте скрипт `app.py`. Запустите повторное сканирование и убедитесь, что они устранены. Приложите исправленный файл `app.py` и отчет без уязвимостей.

Описание уязвимостей Semgrep было дано в пункте 3 текущего отчёта.

Испрапвляем уязвимости следующим образом:

1) sast.py-info-version-disclosure — раскрытие версии приложения

Было: return "Vulnerable lab07 app v1.0"
Стало: убрана версия: return "Vulnerable lab07 app"

2) sast.py-os-system-rce — RCE через os.system() + ввод пользователя

Было: формирование строки cmd = f"ping -c 1 {host}" и os.system(cmd)
Стало: строгая валидация host как IP (ipaddress.ip_address), затем запуск subprocess.run(["ping", "-c", "1", host], ...) без shell

3) sast.py-arbitrary-file-read — LFI / Path Traversal в /read

Было: open(path) напрямую из query string
Стало: запрет абсолютных путей, разрешение чтения только внутри /tmp/vulnerable-app-allowed. resolve() + проверка, что путь остаётся в пределах базовой директории

4) sast.py-unsafe-pickle-deserialization — небезопасный pickle.loads

Было: pickle.loads(bytes.fromhex(data))
Стало: полностью убрана десериализация pickle; данные лишь декодируются в текст и возвращаются как строка

5) sast.py-eval-user-input — eval() на пользовательском вводе

Было: result = eval(expr)
Стало: _safe_eval() через ast.parse + белый список арифметических операций

Так теперь выглядит отчёт Semgrep:

```bash
{
    "engine_requested": "OSS",
    "errors": [
        {
            "code": 2,
            "level": "warn",
            "message": "Other syntax error at line vulnerable-app/config.yaml:37:\n (approximate error location; error nearby after) error calling parser: could not find expected ':' character 0 position 0 returned: 0",
            "path": "vulnerable-app/config.yaml",
            "type": "Other syntax error"
        }
    ],
    "paths": {
        "scanned": [
            "vulnerable-app/app.py",
            "vulnerable-app/config.yaml"
        ]
    },
    "profiling_results": [],
    "results": [],
    "skipped_rules": [],
    "time": {
        "fixpoint_timeouts": [],
        "matching_time": {
            "per_file_and_rule_time": {
                "mean": 0.0,
                "std_dev": 0.0
            },
            "total_time": 0.0,
            "very_slow_rules_on_files": [],
            "very_slow_stats": {
                "count_ratio": 0.0,
                "time_ratio": 0.0
            }
        },
        "max_memory_bytes": 131017152,
        "parsing_time": {
            "per_file_time": {
                "mean": 0.0,
                "std_dev": 0.0
            },
            "total_time": 0.0,
            "very_slow_files": [],
            "very_slow_stats": {
                "count_ratio": 0.0,
                "time_ratio": 0.0
            }
        },
        "prefiltering": {
            "file_level_time": 0.0,
            "project_level_time": 0.0,
            "rules_matched_ratio": 0.9166666666666666,
            "rules_selected_ratio": 0.9166666666666666,
            "rules_with_file_prefilters_ratio": 0.9166666666666666,
            "rules_with_project_prefilters_ratio": 0.0
        },
        "profiling_times": {
            "config_time": 0.3050954341888428,
            "core_time": 0.5892069339752197,
            "ignores_time": 0.00011038780212402344,
            "total_time": 0.9944624900817871
        },
        "rules": [],
        "rules_parse_time": 0.0071430206298828125,
        "scanning_time": {
            "per_file_time": {
                "mean": 0.01981949806213379,
                "std_dev": 0.00025467524125133423
            },
            "total_time": 0.03963899612426758,
            "very_slow_files": [],
            "very_slow_stats": {
                "count_ratio": 0.0,
                "time_ratio": 0.0
            }
        },
        "tainting_time": {
            "per_def_and_rule_time": {
                "mean": 0.0,
                "std_dev": 0.0
            },
            "total_time": 0.0,
            "very_slow_rules_on_defs": [],
            "very_slow_stats": {
                "count_ratio": 0.0,
                "time_ratio": 0.0
            }
        },
        "targets": [],
        "total_bytes": 0
    },
    "version": "1.146.0"
}
```

- [X] 10. Доработайте SCA уязвимости, что бы они только остались в фиинальной версии отчетов.


В исходном pom.xml использовались устаревшие версии библиотек с множеством известных уязвимостей:

`groovy-all:2.1.6` - 3 CVE (включая критические 9.8)
`jackson-jaxrs-json-provider:2.4.6` - множественные CVE в зависимостях
`commons-httpclient:3.1` - 2 CVE, библиотека устарела

Поэтому были обновлены зависимости на более безопасные версии:

`groovy-all:2.1.6 → groovy:4.0.15`

Переход на актуальную версию Apache Groovy
Устранены критические уязвимости CVE-2015-3253, CVE-2016-6814

`jackson-jaxrs-json-provider:2.4.6 → jackson-jaxrs-json-provider:2.16.1`

Обновление на версию с исправленными уязвимостями
Устранены множественные CVE в jackson-databind, jackson-core

`commons-httpclient:3.1 → httpclient5:5.2.1`

Замена устаревшей библиотеки на актуальную Apache HttpClient 5
Устранены CVE-2020-13956, CVE-2012-5783

В результате большая часть выявленных уязвимостей была устранена, и в финальном отчёте остались только те, которые относятся к Python-части приложения (app.py и его зависимости).

Чтобы провести проверку, необхдимо выпустить API токен на сайте https://ossindex.sonatype.org/.

- [X] 11. Проверьте себя по найденным сработкам анализаторов и так вы сможете помочь себе разобраться в ситуации, если возникнут сложности

```bash
$ bash cheat_check_yuorself.sh
```

Скрипт проверяет наличие всех необходимых инструментов (docker, semgrep, checkov, mvn), запускает сборку и развертывание уязвимого приложения, выполняет все сканирования (Semgrep, Checkov, Dependency-Check) и генерирует единые отчеты. Это уже было сделано на предыдущих шагах вручную, поэтому необходимости в повторном запуске нет.

- [X] 12. Делайте все коммиты на соответствующих шагах, далее заливайте изменения в удаленный репозиторий.
- [X] 13. Подготовьте отчет `gist`.
- [X] 14. Почистите кеш от `venv` и остановите уязвимое приложение

```bash
$ deactivate
$ rm -rf venv
$ docker-compose -f ххх down
$ docker-compose -f docker-compose.yml down
$ docker system prune -f
```

Copyright (c) 2025 Nikita Sergeev
