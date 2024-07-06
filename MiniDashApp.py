# In[]: Import Packages

import plotly.express as px
import pandas as pd

from dash import Dash, html, dcc, callback, Output, Input

# In[]: Read CSV File (Online File)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv"
)

# In[]: Create Dash Application 

app = Dash()


# In[]: Create Layout 

# 1.) html   # 2.) Button / DropList / Sliders # 3.) Graph
app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}), 
    dcc.Dropdown(df.country.unique(), 'Ireland', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])


# In[]:  Create Logic (Callback function)

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    df_new = df[df.country == value]
    return  px.line(df_new, x='year', y='pop')


# In[]:   

if __name__ == "__main__":
    app.run(debug=True)