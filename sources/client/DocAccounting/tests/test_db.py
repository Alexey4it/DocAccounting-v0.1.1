from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DocAccounting.tests.test_db_classes import *
def connecDBAndShowTable():
    dialect = "mysql+mysqlconnector"
    username = "root"
    password = "root"
    host = "localhost"
    port = "3306"
    database = "test1"
    connection = '{0}://{1}:{2}@{3}:{4}/{5}'.format(
        dialect,
        username,
        password,
        host,
        port,
        database
    )
    engine = create_engine(connection)
    Session = sessionmaker(bind=engine)
    engine.connect()
    session = Session()
    records = session.query(Testtable).all()
    for record in records:
        print("{0} {1}".format(record.id, record.value1))
    session.commit()
