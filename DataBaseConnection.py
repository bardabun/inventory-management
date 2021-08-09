import pandas as pd
import TablesObj
import numpy as np
import os
import threading as td
from sqlalchemy import create_engine
import sqlalchemy
import pymysql


class SqlConnection:
    def __init__(self, engine_path="mysql+pymysql://root:Aa123456@localhost:3306/info_sys", schema_name="info_sys"):
        # fixed - 'mysql+pymysql://' username = "root" + ":" password = "Aa123456" + "@" +
        # localhost: +port | dataset "/" +"info_sys"
        self.schema_name = schema_name
        self.__engine = sqlalchemy.create_engine(engine_path)

    def add_table(self, name, df):
        try:
            df.to_sql(name=name, con=self.__engine, index=False, if_exists='fail')
        except ValueError as vx:
            print(vx)
            return
        except Exception as ex:
            print(ex)
            return
        else:
            print("Table %s created successfully." % name)
        return TablesObj.TableObj(df, name)

    def delete_table(self, name):
        self.__engine.execute("DROP TABLE " + name)

    def append_line(self, table_obj, values_list):
        string = (str(values_list) + "").replace("[", "(").replace("]", ")") + ";"
        self.__engine.execute("INSERT INTO " + table_obj.name + " VALUES " + string)

    def replace_table(self, table_obj):
        try:
            table_obj.df.to_sql(name=table_obj.name, con=self.__engine, index=False, if_exists='replace')
        except ValueError as vx:
            print(vx)
            return False
        except Exception as ex:
            print(ex)
            return False
        print("Table %s replace successfully." % table_obj.name)
        return True

    def append_data_frame(self, table_obj, data_frame):
        try:
            data_frame.to_sql(name=table_obj.name, con=self.__engine, index=False, if_exists='append')
        except ValueError as vx:
            print(vx)
        except Exception as ex:
            print(ex)
        else:
            print("Table %s created successfully." % table_name.name)
        return table_obj.df.append(table_obj.df)

    def query_to_dataframe(self, query_string):
        result_proxy = self.__engine.execute(query_string)
        rows = result_proxy.fetchall()
        headers = result_proxy.keys()
        return pd.DataFrame(data=rows, columns=headers)

    def get_table(self, name):
        result_proxy = self.__engine.execute("SELECT * FROM " + name)
        rows = result_proxy.fetchall()
        headers = result_proxy.keys()
        return TablesObj.TableObj(pd.DataFrame(data=rows, columns=headers), self, name)

    def get_tables_names(self):
        return self.__engine.table_names()

    def is_exist(self, table_name):
        return table_name in self.get_tables_names()

    def __str__(self):
        string = "Schema name : " + "\"" + self.schema_name + "\"\n"
        string += "Engine path : " + "\"" + self.__engine.name + "\""
        return string

