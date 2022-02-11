:: Генерация схем классов, пакетов и модулей по исходному коду
pyreverse -d schemes DocAccounting
:: Конвертирование dot в png
"C:\Program Files (x86)\Graphviz\bin\dot.exe" -Tpng schemes/classes.dot > schemes/classes.png
"C:\Program Files (x86)\Graphviz\bin\dot.exe" -Tpng schemes/packages.dot > schemes/packages.png