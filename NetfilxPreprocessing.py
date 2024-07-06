# In[]:

import copy

import pandas as pd

import config
from Connector2SQLite import SQLite

# In[]:


class NetFilxPreprocessor:
    def __init__(self) -> None:
        pass

    def _get_data_from_db(self) -> None:
        db = SQLite(database_name=config.path + "netfilx")
        sql_query = "SELECT * FROM Netflix;"
        self.df = db.get_tables(sql_query, "NetFilx_Data")
        # db.handle_different_queries()
        db.terminate_connection()
        # Code to connect to MySQL server
        # import MySQLdb
        # connection = MySQLdb.connect(
        #     host=,
        #     password=,
        #     port=,
        #     datbase_name=,
        #     uername=,
        # )
        return None

    def _preprocessing(self) -> pd.DataFrame:
        """
        arg: None
        return: preprocessed Dataframe
        description:
        Remove null values, handle missing data, add new features, and remove duplicates
        """
        df_tmp = copy.deepcopy(self.df)
        df_tmp = df_tmp.drop(["director", "cast"], axis=1)
        df_tmp = df_tmp[df_tmp["date_added"].notna()]
        df_tmp = df_tmp.reset_index(drop=True)
        df_tmp["country"] = df_tmp["country"].fillna(df_tmp["country"].mode()[0])
        df_tmp["year_added"] = df_tmp["date_added"].apply(lambda x: x.split(" ")[-1])
        df_tmp["month_added"] = df_tmp["date_added"].apply(lambda x: x.split(" ")[0])
        df_tmp = df_tmp.drop_duplicates()
        df_tmp["target_ages"] = df_tmp.rating.replace(config.rating_ages)
        # df_tmp["genre"] = df_tmp["listed_in"].apply(
        #     lambda x: x.replace(" ,", ",").replace(", ", ",").split(",")
        # )
        return df_tmp

    def run_processor(self) -> pd.DataFrame:
        self._get_data_from_db()
        df_final = self._preprocessing()
        return df_final
