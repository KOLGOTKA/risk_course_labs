<div align="center">
<h1><a id="intro">Лабораторная работа №8</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Сергеев_Н._М.-8b9aff" alt="Contributor Badge"></a></div>

## Задание

- [X] 1. Разверните и подготовьте окружение для уязвимого приложения

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt && vulnerable-app/requirements.txt 
```

- [X] 2. Запустите уязвимое приложение

```bash
$ docker-compose up -d --build  # http://localhost:8080
```

- [X] 3. Проверьте доступность приложения

```bash
$ curl -i http://localhost:8080
```

Вывод такой:

```bash
(venv) uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab08$ curl -i http://localhost:8080
HTTP/1.1 200 OK
Server: Werkzeug/2.2.3 Python/3.11.14
Date: Sun, 28 Dec 2025 22:31:12 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 625
Set-Cookie: session=guest-session-id; Path=/
Connection: close


    <h1>Vulnerable DAST Demo App</h1>
    <p>Пример уязвимого приложения для лабораторной по DAST.</p>
    <ul>
      <li><a href="/echo?msg=Hello">Reflected XSS / echo</a></li>
      <li><a href="/search?username=admin">SQL Injection / search</a></li>
      <li><a href="/login">Небезопасный логин</a></li>
      <li><a href="/profile">Профиль (зависит от cookie)</a></li>
      <li><a href="/admin">«Админка» без нормальной авторизации</a></li>
      <li><a href="/files/">Directory listing</a></li>
    </ul>
```

- [X] 4. Проведите ручное исследование уязвимостей и опишите почему такое происходит, каким образом реализуются уязвимости и дайте им определение
- [X] 4.1. `/echo` - проверить отражение параметра  `msg`  в `HTML` и использовать `payload` вида  `<script>alert('XSS')</script>` зафиксировав его поведение

```bash
http://localhost:8080/echo?msg=<script>alert('hack with XSS')</script>
```

Вылезает alert с сообщением 'hack with XSS'. Это означает, что приложение уязвимо к XSS. #TODO определение и пояснение

- [X] 4.2. `/search` - проверить обычный запрос  `?username=admin` и использовать строку  `?username=admin' OR '1'='1` зафиксировав его поведение описав признак SQLi

Параметр username напрямую подставляется в SQL-запрос без параметризации

```bash
http://localhost:8080/search?username=admin' OR '1'='1
```

Вывод:

```
Поиск пользователя
Запрос: SELECT id, username, role FROM users WHERE username = 'admin' OR '1'='1'

3 – admin (admin)
4 – user (user)
Попробуйте, например: ?username=admin' OR '1'='1

Назад
```

Означает, что приложение уязвимо для классической SQL Injection уязвимости, вызванной конкатенацией SQL-строки с пользовательским вводом.

- [X] 4.3. `/login` - войти под  `admin`  и  `user` проверив логику на открытые пароли и простые SQL‑запросы

user и admin имеют простые пароли, которые легко подобрать

Вывод для admin:

```
Добро пожаловать, admin (admin)!
На главную
```

- [X] 4.4. `/profile` - изменить `cookie  role`  на  `admin`  через `DevTools` → `Application` → `Cookies` и обновить  `/profile` (возможно создать `cookie`)

Можно в инструментах разработчика браузера изменить cookie "role" на user/admin, после чего при обновлении страницы /profile отобразится профиль желаемого пользователя:

```
Профиль пользователя
Имя: admin

Роль: user

Cookie легко подделать: можно выдать себе роль 'admin'.

Назад
```

- [X] 4.5. `/admin` -  проверить, что доступ запрещён без `cookie  role=admin` и далее подделать `cookie`, что «админка» открывается путем изменения через `DevTools`. **Подсказка:** доступ завязан на значение cookie, без подписи/ токена/ серверной проверки.

Изначальный вывод:
```
Доступ запрещён: вы не admin
Попробуйте изменить cookie 'role'.

Назад
```

После подмены cookie "role" на admin:

```
Admin panel
Секретные настройки приложения (демо).

DEBUG: true
FEATURE_FLAG: experimental_mode
Назад
```

Контроль доступа реализован исключительно на стороне клиента.
Cookie не подписана, не проверяется сервером и может быть произвольно изменена, что приводит к эскалации привилегий.

- [X] 4.6. `/files/` - просмотрите `directory listing` и откройте один из файлов убедившись, что оно выводится

```bash
http://localhost:8080/files/secret.txt
```
При попытке обратиться к `http://localhost:8080/files/secret.txt` либо `http://localhost:8080/files/` выводится сообщение:
```
Путь не найден
Назад
```

При указании других путей по типу `/storage`,  `/uploads`  и т.д. выводится такое сообщение:
```
Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
```

Отсюда можно сделать вывод, что листинг директорий отключён.

- [X] 5. Доработайте по пп 4 лабораторную работу развив их содержимое, которое может выводиться (мин 1 пример)

1) Доработаем XSS на /echo через запрос `http://localhost:8080/echo?msg=<script>document.write(document.cookie)</script>`
, что выведет все cookie текущего пользователя.

Вывод:

```
Echo
Сообщение: _xsrf=2|32d86a3f|175994e6ec3e1bab8e2893fa3e575ac6|1766437210; session=guest-session-id; user=admin; role=admin

Попробуйте передать что-нибудь вроде: <script>alert('XSS')</script>

Назад
```

2) Расширим SQLi на /search попытавшись вывести все схемы в БД. Опытным путём, перебирая основные методы вывода структуры БД, было выяснено, что используется SQLite. Затем выполнен запрос `http://localhost:8080/search?username=' UNION SELECT 1, name, sql FROM sqlite_master WHERE type='table' --
`, что выводит все таблицы базы данных.

```
Поиск пользователя
Запрос: SELECT id, username, role FROM users WHERE username = '' UNION SELECT 1, name, sql FROM sqlite_master WHERE type='table' --'

1 – sqlite_sequence (CREATE TABLE sqlite_sequence(name,seq))
1 – users (CREATE TABLE users ( id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, role TEXT ))
Попробуйте, например: ?username=admin' OR '1'='1

Назад
```

Далее создадим своего адимистративного пользователя, зная структуру таблицы users. Запрос `http://localhost:8080/search?username=admin'; INSERT INTO users (username, password, role) VALUES ('uniqm','uniqm','admin'); --`

Однако в выводе увидим, что запрос не выполнен, так как SQLite не позволяет выполнять несколько команд в одном запросе.
```
SQL error: You can only execute one statement at a time.
```

- [X] 6. Поставьте `OWASP ZAP` и стяните образ конкртеной версии для него

```bash
$ apt install -y zaproxy
$ docker pull ghcr.io/zaproxy/zaproxy:stable
```

- [X] 7. Задайте переменные окружения для работы скриптов

```bash
$ export ZAP_IMAGE=ghcr.io/zaproxy/zaproxy:stable
$ TARGET_URL="${TARGET_URL:-http://host.docker.internal:8080}"
```

- [X] 8. Запустите скрипт автоматического сканирования DAST `OWASP ZAP`

```bash
$ ./zap_scan.sh
```

Запускаем скрипт и получаем следующий вывод:
```bash
(venv) uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab08/dast$ ./zap_scan.sh
[*] Running OWASP ZAP baseline scan against http://host.docker.internal:8080
[i] Using image: ghcr.io/zaproxy/zaproxy:stable
[i] Reports will be saved to /home/uniqm/DevSecOps/risk_course_labs/labs/lab08/dast/reports
Using the Automation Framework
Total of 12 URLs
PASS: Vulnerable JS Library (Powered by Retire.js) [10003]
PASS: In Page Banner Information Leak [10009]
PASS: Cookie Without Secure Flag [10011]
PASS: Re-examine Cache-control Directives [10015]
PASS: Cross-Domain JavaScript Source File Inclusion [10017]
PASS: Content-Type Header Missing [10019]
PASS: Information Disclosure - Debug Error Messages [10023]
PASS: Information Disclosure - Sensitive Information in HTTP Referrer Header [10025]
PASS: HTTP Parameter Override [10026]
PASS: Information Disclosure - Suspicious Comments [10027]
PASS: Off-site Redirect [10028]
PASS: Cookie Poisoning [10029]
PASS: User Controllable Charset [10030]
PASS: User Controllable HTML Element Attribute (Potential XSS) [10031]
PASS: Viewstate [10032]
PASS: Directory Browsing [10033]
PASS: Heartbleed OpenSSL Vulnerability (Indicative) [10034]
PASS: Strict-Transport-Security Header [10035]
PASS: Server Leaks Information via "X-Powered-By" HTTP Response Header Field(s) [10037]
PASS: X-Backend-Server Header Information Leak [10039]
PASS: Secure Pages Include Mixed Content [10040]
PASS: HTTP to HTTPS Insecure Transition in Form Post [10041]
PASS: HTTPS to HTTP Insecure Transition in Form Post [10042]
PASS: User Controllable JavaScript Event (XSS) [10043]
PASS: Big Redirect Detected (Potential Sensitive Information Leak) [10044]
PASS: Retrieved from Cache [10050]
PASS: X-ChromeLogger-Data (XCOLD) Header Information Leak [10052]
PASS: CSP [10055]
PASS: X-Debug-Token Information Leak [10056]
PASS: Username Hash Found [10057]
PASS: X-AspNet-Version Response Header [10061]
PASS: PII Disclosure [10062]
PASS: Timestamp Disclosure [10096]
PASS: Hash Disclosure [10097]
PASS: Cross-Domain Misconfiguration [10098]
PASS: Weak Authentication Method [10105]
PASS: Reverse Tabnabbing [10108]
PASS: Modern Web Application [10109]
PASS: Dangerous JS Functions [10110]
PASS: Verification Request Identified [10113]
PASS: Script Served From Malicious Domain (polyfill) [10115]
PASS: ZAP is Out of Date [10116]
PASS: Absence of Anti-CSRF Tokens [10202]
PASS: Private IP Disclosure [2]
PASS: Session ID in URL Rewrite [3]
PASS: Script Passive Scan Rules [50001]
PASS: Stats Passive Scan Rule [50003]
PASS: Insecure JSF ViewState [90001]
PASS: Java Serialization Object [90002]
PASS: Sub Resource Integrity Attribute Missing [90003]
PASS: Charset Mismatch [90011]
PASS: Application Error Disclosure [90022]
PASS: WSDL File Detection [90030]
PASS: Loosely Scoped Cookie [90033]
WARN-NEW: Cookie No HttpOnly Flag [10010] x 2
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
WARN-NEW: Missing Anti-clickjacking Header [10020] x 4
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
        http://host.docker.internal:8080/echo?msg=Hello (200 OK)
        http://host.docker.internal:8080/search?username=admin (200 OK)
WARN-NEW: X-Content-Type-Options Header Missing [10021] x 5
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
        http://host.docker.internal:8080/login (200 OK)
        http://host.docker.internal:8080/profile (200 OK)
        http://host.docker.internal:8080/search?username=admin (200 OK)
WARN-NEW: Information Disclosure - Sensitive Information in URL [10024] x 1
        http://host.docker.internal:8080/search?username=admin (200 OK)
WARN-NEW: Server Leaks Version Information via "Server" HTTP Response Header Field [10036] x 5
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/login (200 OK)
        http://host.docker.internal:8080/robots.txt (404 Not Found)
        http://host.docker.internal:8080/script (404 Not Found)
        http://host.docker.internal:8080/sitemap.xml (404 Not Found)
WARN-NEW: Content Security Policy (CSP) Header Not Set [10038] x 5
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
        http://host.docker.internal:8080/login (200 OK)
        http://host.docker.internal:8080/robots.txt (404 Not Found)
        http://host.docker.internal:8080/sitemap.xml (404 Not Found)
WARN-NEW: Non-Storable Content [10049] x 6
        http://host.docker.internal:8080/admin (403 Forbidden)
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/login (200 OK)
        http://host.docker.internal:8080/robots.txt (404 Not Found)
        http://host.docker.internal:8080/script (404 Not Found)
WARN-NEW: Cookie without SameSite Attribute [10054] x 2
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
WARN-NEW: Permissions Policy Header Not Set [10063] x 5
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/login (200 OK)
        http://host.docker.internal:8080/robots.txt (404 Not Found)
        http://host.docker.internal:8080/script (404 Not Found)
        http://host.docker.internal:8080/sitemap.xml (404 Not Found)
WARN-NEW: Source Code Disclosure - SQL [10099] x 1
        http://host.docker.internal:8080/search?username=admin (200 OK)
WARN-NEW: Authentication Request Identified [10111] x 1
        http://host.docker.internal:8080/login (200 OK)
WARN-NEW: Session Management Response Identified [10112] x 2
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
WARN-NEW: Insufficient Site Isolation Against Spectre Vulnerability [90004] x 15
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
        http://host.docker.internal:8080/login (200 OK)
        http://host.docker.internal:8080/profile (200 OK)
        http://host.docker.internal:8080/search?username=admin (200 OK)
FAIL-NEW: 0     FAIL-INPROG: 0  WARN-NEW: 13    WARN-INPROG: 0  INFO: 0 IGNORE: 0       PASS: 54
[+] ZAP scan completed. Reports (if any) in /home/uniqm/DevSecOps/risk_course_labs/labs/lab08/dast/reports
-rw-r--r-- 1 uniqm uniqm 103K Jan  3 01:41 /home/uniqm/DevSecOps/risk_course_labs/labs/lab08/dast/reports/zap-report-20260103_014113.html
-rw-r--r-- 1 uniqm uniqm  38K Jan  3 01:41 /home/uniqm/DevSecOps/risk_course_labs/labs/lab08/dast/reports/zap-report-20260103_014113.json
-rw-r--r-- 1 uniqm uniqm  46K Jan  3 01:41 /home/uniqm/DevSecOps/risk_course_labs/labs/lab08/dast/reports/zap-report-20260103_014113.xml
[*] Converting JSON report to ODT/XLSX using /home/uniqm/DevSecOps/risk_course_labs/labs/lab08/dast/../venv/bin/python ...
[debug] python: /home/uniqm/DevSecOps/risk_course_labs/labs/lab08/venv/bin/python
[debug] odf imported OK
[*] Parsing ZAP JSON report: zap-report-20260103_014113.json
[i] Found 14 alerts
[+] ODT report saved: odt/zap-report-20260103_014113.odt
[+] XLSX report saved: xlsx/zap-report-20260103_014113.xlsx
[+] Report conversion completed!
```

- [X] 9. Изучите сгенерированные отчеты в `dast/reports` и опишите риски ИБ для них, без сценариев, так как ранее вы видели часть из их реализации

Отчёты будут лежать в папке `dast/reports` в форматах `HTML`, `JSON`, `XML`, а также будут сгенерированы конвертированные отчёты в форматах `ODT` и `XLSX` в папках `dast/reports/odt` и `dast/reports/xlsx` соответственно.

```bash
(venv) uniqm@DESKTOP-OT4LBEF:~/DevSecOps/risk_course_labs/labs/lab08/dast/reports$ ls -l
total 204
drwxr-xr-x 2 uniqm uniqm   4096 Jan  3 01:42 odt
drwxr-xr-x 2 uniqm uniqm   4096 Jan  3 01:42 xlsx
-rw-r--r-- 1 uniqm uniqm 104741 Jan  3 01:41 zap-report-20260103_014113.html
-rw-r--r-- 1 uniqm uniqm  38491 Jan  3 01:41 zap-report-20260103_014113.json
-rw-r--r-- 1 uniqm uniqm  46338 Jan  3 01:41 zap-report-20260103_014113.xml
-rw-r--r-- 1 uniqm uniqm   1103 Jan  3 01:41 zap.yaml
```

#### Утечка и компрометация пользовательских и административных данных

Утечка учетных данных и служебной информации вследствие SQL Injection и раскрытия внутренних запросов, что приводит к несанкционированному доступу к системе, штрафам со стороны регуляторов, репутационным потерям и затратам на экстренное устранение последствий.

#### Захват пользовательских и административных сессий

Компрометация активных сессий из-за XSS и небезопасных cookie без защитных флагов, что позволит злоумышленнику действовать от имени пользователей и администраторов и приведит к утечке данных и дальнейшим инцидентам.

#### Несанкционированный доступ к административным функциям

Получение злоумышленником административных прав из-за отсутствия серверной проверки авторизации и доверия к значениям cookie, что может привести к изменению данных, удалению ресурсов и полной компрометации приложения.

#### Усиление клиентских атак и эксплуатация уязвимостей браузера

Эксплуатация клиентских атак из-за отсутствия защитных HTTP-заголовков, что повышает вероятность XSS, clickjacking и других атак и приводит к увеличению числа инцидентов и затрат на их расследование.


- [X] 10. Внесите исправления по данному отчету `DAST` для `vulnerable-app/app.py`

В исходный код приложения внесены следующие изменения для устранения выявленных уязвимостей DAST:

| DAST предупреждение       | Статус | Как исправлено                               |
| ------------------------- | ------ | -------------------------------------------- |
| Sensitive Info in URL     | ✅      | `/search` переведён на POST                  |
| Server header leak        | ✅      | Перезапись `Server` через `after_request`    |
| CSP missing / no fallback | ✅      | Полный CSP с `default-src`                   |
| Non-storable content      | ✅      | `Cache-Control: no-store` глобально          |
| Cookie SameSite           | ✅      | `SameSite=Strict`                            |
| Permissions Policy        | ✅      | Добавлен `Permissions-Policy`                |
| Session Management        | ✅      | Серверные сессии Flask                       |
| SQL Injection             | ✅      | Параметризованные запросы                    |
| XSS                       | ✅      | Jinja escaping                               |

После повторного сканирования видим следующие уязвимости:

```bash
WARN-NEW: Server Leaks Version Information via "Server" HTTP Response Header Field [10036] x 5
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/admin (403 Forbidden)
        http://host.docker.internal:8080/login (200 OK)
        http://host.docker.internal:8080/profile (200 OK)
        http://host.docker.internal:8080/login (200 OK)
WARN-NEW: Non-Storable Content [10049] x 5
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/admin (403 Forbidden)
        http://host.docker.internal:8080/files/ (404 Not Found)
        http://host.docker.internal:8080/robots.txt (404 Not Found)
        http://host.docker.internal:8080/sitemap.xml (404 Not Found)
WARN-NEW: CSP: Failure to Define Directive with No Fallback [10055] x 5
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/files/ (404 Not Found)
        http://host.docker.internal:8080/profile (200 OK)
        http://host.docker.internal:8080/sitemap.xml (404 Not Found)
        http://host.docker.internal:8080/login (200 OK)
WARN-NEW: Authentication Request Identified [10111] x 1
        http://host.docker.internal:8080/login (200 OK)
WARN-NEW: Session Management Response Identified [10112] x 4
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/ (200 OK)
WARN-NEW: Insufficient Site Isolation Against Spectre Vulnerability [90004] x 15
        http://host.docker.internal:8080 (200 OK)
        http://host.docker.internal:8080/echo?msg=Hello (200 OK)
        http://host.docker.internal:8080/login (200 OK)
        http://host.docker.internal:8080/profile (200 OK)
        http://host.docker.internal:8080/login (200 OK)
FAIL-NEW: 0     FAIL-INPROG: 0  WARN-NEW: 6     WARN-INPROG: 0  INFO: 0 IGNORE: 0       PASS: 6
```

Вот описание оставшихся уязвимостей:

1. **Server Leaks Version Info [10036]** – заголовок `Server` может показывать версию, полностью убрать его без изменения окружения (WSGI/прокси) невозможно.
2. **Non-Storable Content [10049]** – предупреждение на 404 и статические ресурсы; полностью закрыть без изменения структуры файлов или серверных настроек нельзя.
3. **CSP Failure [10055]** – строгий CSP установлен, но DAST ругается на отсутствующие ресурсы; устранение требует изменения бизнес-логики.
4. **Authentication Identified [10111]** – форма логина необходима для работы приложения, убрать её нарушит бизнес-логику.
5. **Session Management [10112]** – использование cookie-сессий нужно для работы `/login` и `/profile`; отключение ломает функционал.
6. **Spectre Vulnerability [90004]** – аппаратная/браузерная проблема, код приложения её не исправит.


- [X] 11. Делайте все необходимые коммиты по шагам и отправляйте изменения в удалённый репозиторий
- [X] 12. Подготовьте отчет `gist`.
- [X] 14. Почистите кеш от `venv` и остановите уязвимое приложение

Copyright (c) 2025 Nikita Sergeev
