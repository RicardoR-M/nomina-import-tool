from sqlalchemy import create_engine, MetaData
from os import getenv


def save_to_db(dbase, db_table_name, lista_evas, semana, mes, anho):
    db_conn = getenv("DB_CONN")
    db = dbase
    source = f"{db_conn}/{db}"
    engine = create_engine(source, echo=False)

    meta_data = MetaData(bind=engine)
    meta_data.reflect(only=[db_table_name])
    engine.execution_options(autocommit=True).execute(f"DELETE FROM [{db_table_name}] WHERE [SEMANA]={semana} AND [MES]='{mes}'  AND [AÑO]={anho}")
    engine.execute(meta_data.tables[db_table_name].insert(), lista_evas)
