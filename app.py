# In[]: Import packages

import pandas as pd
from NetfilxPreprocessing import NetFilxPreprocessor
from Connector2SQLite import SQLite

# In[]:


def app():
    # obj = NetFilxPreprocessor()
    # output_df = obj.run_processor()
    # print(output_df)

    df = pd.read_csv("TopPrincipalGenre.csv")

    obj = SQLite('nas')
    # obj.create_table('output_table', df)

    df = pd.DataFrame(
        {
            'principal_genre':['Light Comdey', 'Egyptain Drama'],
            'TopPrincipalGenre':[1000, 2]
        }
    )
    obj.insert_to_table('output_table',df)


# In[]:

if __name__ == "__main__":
    app()
