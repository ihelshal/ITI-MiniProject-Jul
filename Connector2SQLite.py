# In[]: Import Packages

import sqlite3
import sys
from sqlite3 import Error

import pandas as pd

# In[]: Build The SQLite Class and its functions.


class SQLite:
    def __init__(self, database_name: str = None) -> None:
        self._connection = sqlite3.connect(database_name)

    # def handle_different_queries(queries):
    # pass required queries to get_tables

    def get_tables(
        self, query: str, output_file_name: str, batch_size: int = 10000
    ) -> pd.DataFrame:
        try:
            # Initalize Connection and execute query
            cur = self._connection.cursor()
            # "SELECT * FROM Netflix;"
            cur.execute(query)

            rows = []
            while True:
                batch = cur.fetchmany(batch_size)
                if not batch:
                    break
                rows.extend(batch)

            columns = [col[0] for col in cur.description]
            # # print(columns)
            # # sys.exit('Under Test....')
            df = pd.DataFrame(rows, columns=columns)
            df.to_csv(output_file_name + ".csv", index=False)

            if df.empty:
                print("Table exists but is empty !")
                return None

            return df

        except Error as e:
            print(f"Error excuting: {e}")

    def create_table(self, table_name: str, df: pd.DataFrame) -> None:
        try:
            df.to_sql(table_name, self._connection, if_exists="fail", index=False)
            print('TABLE CREATED')
        except Error as e:
            print(f"Error excuting: {e}")

    def insert_to_table(self, table_name: str, df: pd.DataFrame) -> None:
        # IF WE INSERT NEW QUERY ONLY 
        try:
            cur = self._connection.cursor()
            r, _ = df.shape

            for i in range(r):
                # SQL: INSERT INTO TABLE_NAME VALUES() ()
                cur.execute(
                    "Insert into {0} values (?,?)".format(table_name),
                    (
                        str(df['principal_genre'][i]),
                        int(df['TopPrincipalGenre'][i]),
                    )
                )
                self._connection.commit()
        except:
            self._connection.rollback()
            raise Exception("Error")

    def terminate_connection(self) -> None:
        self._connection.close()


# In[]:

# list1 = [1,2,3]
# list1.append(4)

# print(list1)

# list1 = [1,2,3]
# list1.append([1,4])

# print(list1) # -> [1,2,3,[1,4]]

# list1 = [1,2,3]
# list1.extend([1,4]) # -> [1,2,3,1,4]
