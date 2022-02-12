# DocAccounting-v0.1.1
ИС Учёт документации в организации ООО "Импэкс"
Инструкция по запуску
1. Скачать mysql-installer-web-community-5.7.37.0.msi по ссылке
https://dev.mysql.com/downloads/windows/installer/5.7.html
2. Установить только mysql-server (по умолчанию имя пользователя и пароль для ИС: root)
3. Запустить sql server. Настройка базы данных:
	3.1 Создание базы данных: CREATE DATABASE DocAccountingDB CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
	3.2 Выбрать базу данных: USE DocAccountingDB;
	3.3 Создать таблицы в базе данных: source <path to sql file>\doc_accounting_first.sql
  Желательно уазывать путь без пробелов, например source C:\temp\DocAccounting-v0.1.1-main\sources\server\doc_accounting_first.sql;
4. Запускаем исполняемый файл DocAccounting-v0.1.1--main\bin\DocAccounting_v0_1_1.exe
