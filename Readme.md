Инструкция по запуску программы на локальном компьютере

1. Cоздание виртуального окружения: 

python -m venv .venv
.venv\Scripts\activate

2. Конфигурация файла .env:

DB_HOST = localhost,
DB_PORT = 5432,
DB_NAME = postgres,
DB_USER = postgres,
DB_PASS = postgres,
SECRET_KEY_JWT = dfgfd4354dskfdfgksdsztht5676jhdfFDGDdsf9007dsfgfdasdas12,
SECRET_KEY_USERMANAGER = dfqpd34DG54fddf1sdfsd76ds1324dsdfs43fdgDFGDFG43645dfa8HFSdf6gFfah

3. Установить библиотеки из файла requirements.txt:

pip install -r requirements.txt

4. Команда для запуска программы: 

uvicorn scr.main:app --reload

