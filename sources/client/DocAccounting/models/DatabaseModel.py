# from DocAccounting.database.docaccounting_db_classes import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DocAccounting.database.docaccounting_db_classes import Position, \
    Department, Source, CategoryDoc, Developer, StatusDoc, ViewDoc, Doc
from sqlalchemy import exc
class DatabaseModel(object):
    """
    Класс модели базы данных
    """
    def __init__(self):
        """Конструктор"""
        pass
    def connectionToDatabase(self, dialect, userName, password, host, port, database):
        """Подключение к базе данных"""
        self.connection = '{0}://{1}:{2}@{3}:{4}/{5}?charset=utf8'.format(
            dialect,
            userName,
            password,
            host,
            port,
            database
        )
        try:
            self.engine = create_engine(self.connection)
            self.Session = sessionmaker(bind=self.engine)
            self.engine.connect()
            return "connected"
        except exc.SQLAlchemyError as e:
            return "error connecting"
    def setValuesDatabase(self):
        """Заполнение базы данных значениями"""
        session = self.Session()
        # Удаление в таблице Документы
        session.execute("delete from Docs where (code <> -1)")
        session.commit()
        # Удаление в таблице Сотрудники
        session.execute("delete from Employees where (code <> -1)")
        session.commit()
        # Удаление в таблице Должности
        session.execute("delete from Positions where (code <> -1)")
        session.commit()
        # Добавление в таблицу Должности
        for value in range(10):
            v = value + 1
            clazz = Position()
            clazz.code = v
            clazz.title = "title" + str(v)
            session.add(clazz)
            session.commit()
        # Удаление в таблице Отдел
        session.execute("delete from Departments where (code <> -1)")
        session.commit()
        # Добавление в таблицу Отдел
        for value in range(10):
            v = value + 1
            clazz = Department()
            clazz.code = v
            clazz.title = "title" + str(v)
            session.add(clazz)
            session.commit()
        # Удаление в таблице Источники
        session.execute("delete from Sources where (code <> -1)")
        session.commit()
        # Добавление в таблицу Источники
        for value in range(10):
            v = value + 1
            clazz = Source()
            clazz.code = v
            clazz.title = "title" + str(v)
            session.add(clazz)
            session.commit()
        # Удаление в таблице Категории документов
        session.execute("delete from Category_Docs where (code <> -1)")
        session.commit()
        # Добавление в таблицу Категории документов
        for value in range(10):
            v = value + 1
            clazz = CategoryDoc()
            clazz.code = v
            clazz.title = "title" + str(v)
            session.add(clazz)
            session.commit()
        # Удаление в таблице Разработчики
        session.execute("delete from Developers where (code <> -1)")
        session.commit()
        # Добавление в таблицу Разработчики
        for value in range(10):
            v = value + 1
            clazz = Developer()
            clazz.code = v
            clazz.title = "title" + str(v)
            clazz.comments = "comments" + str(v)
            session.add(clazz)
            session.commit()
        # Удаление в таблице Статус документа
        session.execute("delete from Status_Docs where (code <> -1)")
        session.commit()
        # Добавление в таблицу Статус документа
        for value in range(10):
            v = value + 1
            clazz = StatusDoc()
            clazz.code = v
            clazz.title = "title" + str(v)
            clazz.description = "description" + str(v)
            session.add(clazz)
            session.commit()
        # Удаление в таблице Вид документа
        session.execute("delete from View_Docs where (code <> -1)")
        session.commit()
        # Добавление в таблицу Вид документа
        for value in range(10):
            v = value + 1
            clazz = ViewDoc()
            clazz.code = v
            clazz.title = "title" + str(v)
            clazz.description = "description" + str(v)
            session.add(clazz)
            session.commit()
        # Добавление в таблицу Сотрудники
        for value in range(10):
            v = value + 1
            text1 = "code, positions_code, departments_code, allnames, email, login, " \
                    "password, editable, reading"
            sqlText = "insert into Employees ({0}) values (" \
                      "{1}, {1}, {1}, 'allnames{1}', 'email{1}', 'login{1}', 'password{1}', 'editable{1}', 'reading{1}')".format(
                text1, v
            )
            session.execute(sqlText)
            session.commit()
        # Добавление в таблицу Документ
        for value in range(10):
            v = value + 1
            text1 = "code, category_code, view_code, employee_code, status_code, " \
                    "developer_code, source_code, title, date_loading, date_change, barcode, " \
                    "keywords, section_number, pages, copy_n, cupboard, rack, description, " \
                    "docs, docs_ext, sizeMB"
            sqlText = "insert into Docs ({0}) values ({1}, {1}, " \
                      "{1}, {1}, {1}, {1}, {1}, 'title{1}', '{2}', '{2}', 'barcode{1}', 'keywords{1}'," \
                      "{1}, {1}, {1}, 'cupboard{1}', 'rack{1}', 'description{1}', '', '', '')".format(
                text1, v, "2022-02-04 10:10:10"
            )
            session.execute(sqlText)
            session.commit()
        # Удаление в таблице Нормативные документы
        session.execute("delete from Regulations where (code <> -1)")
        session.commit()
        # Добавление в таблицу Нормативные документы
        for value in range(10):
            v = value + 1
            text1 = "code, category, title, docs, docs_ext, url"
            sqlText = "insert into Regulations ({0}) values ({1}, 'category{1}', 'title{1}', '', '', 'url{1}')"\
                .format(
                    text1, v
            )
            session.execute(sqlText)
            session.commit()
    def showTables(self, Clazz):
        """Все значения таблицы"""
        session = self.Session()
        clazzs = session.query(Clazz).all()
        session.close()
        return clazzs
    def addData(self, Clazz, values):
        """Добавление данных в таблицу"""
        session = self.Session()
        clazzs = session.query(Clazz).all()
        codes = [clazz.code for clazz in clazzs]
        clazz = Clazz()
        clazz.code = max(codes) + 1
        for value in values:
            if value[0] != "code":
                if "code" in value[0] and value[0] != "barcode":
                    if value[1] == "":
                        return "error"
                    else:
                        setattr(clazz, value[0], int(value[1]))
                else:
                    if value[0] == "docs":
                        if value[0] == "":
                            setattr(clazz, value[0], bytes("", encoding='utf-8'))
                        else:
                            setattr(clazz, value[0], value[1])
                    else:
                        setattr(clazz, value[0], value[1])

        session.add(clazz)
        session.commit()
        return "add"
    def updateData(self, Clazz, values):
        """Обновление данных в таблице"""
        session = self.Session()
        for value in values:
            if value[0] == "code":
                clazz = session.query(Clazz).filter(Clazz.code == value[1]).one()
                break
        for value in values:
            if value[0] != "code":
                if "code" in value[0] and value[0] != "barcode":
                    if value[1] == "":
                        return "error"
                    else:
                        setattr(clazz, value[0], int(value[1]))
                else:
                    if value[0] == "docs":
                        setattr(clazz, value[0], bytes("", encoding='utf8'))
                    else:
                        setattr(clazz, value[0], value[1])

        session.add(clazz)
        session.commit()
        return "update"
    def delData(self, Clazz, code):
        """Удаление данных в таблице"""
        session = self.Session()
        clazz = session.query(Clazz).filter(Clazz.code == code).one()
        session.delete(clazz)
        session.commit()
        return "del"
    def searchData(self, Clazz, code):
        """Поиск данных в таблице"""
        session = self.Session()
        clazz = session.query(Clazz).filter(Clazz.code == code).one()
        session.commit()
        return clazz