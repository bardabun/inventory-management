import pandas as pd
import DataBaseConnection


class TableRow:
    def __init__(self, arg):

        """
        :type arg: list
        """
        if len(arg) == 3:

            self.df = arg[0]
            """
            :type df: pandas.DataFrame
            """
            self.index = arg[1]
            """
            :type index: integer 
            """
            self.values = arg[2]
            """
            :type values: list 
            """

        elif len(arg) == 1:

            self.index = arg[0].index
            """
            :type index: integer 
            """
            self.df = arg[0].df
            """
            :type df: pandas.DataFrame
            """
            self.values = arg[0].values
            """
            :type values: list 
            """

        else:
            raise Exception("problem to get arguments")
        self.headers = list(self.df.columns.values)

    def change(self, header, val):
        index = self.headers.index(header)
        self.values[index] = val
        self.df.loc[self.index, header] = val
        return self

    def drop(self):
        self.df.drop(self.index, inplace=True)


class TableObj:
    def __init__(self, df, sql_con, name=""):
        self.df = df
        """
        :type df: pandas.DataFrame
        """
        self.sql_con = sql_con
        """
        :type sql_con: DataBaseConnection.SqlConnection
        """
        self.name = name
        """
        :type name: str
        """

    def add_item(self, values):
        if not len(values) == len(self.df.columns.values):
            raise Exception("the function needs " + str(len(self.df.columns.values))\
                            + "\nbut get " + str(len(values)))
        indexes = self.df.index
        index = indexes[len(indexes)-1] + 1
        self.df.loc[index] = values
        return TableRow([self.df, index, values])

    def rows_list(self):
        pd.DataFrame().itertuples()
        ls = []
        indexes = self.df.index
        cnt = 0
        for row in self.df.itertuples():
            ls.append(TableRow([self.df, indexes[cnt], [row]]))
            cnt += 1
        return ls

    def save(self):
        try:
            self.sql_con.replace_table(self)
        except Exception as e:
            x = e
            return
        return

    def __str__(self):
        string = "Table Name : " + "\"" + self.name + "\"\n"
        string += str(self.sql_con) + "\n"
        string += "Data Frame : \n"
        string += str(self.df)
        return string
