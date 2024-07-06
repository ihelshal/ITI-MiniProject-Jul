# In[]: Import Packages

import os
import config
import dash
from dash import Dash, html, dcc, callback, Output, Input

# In[]:

app  = Dash()

# In[]: 

html_file = [config.frames_path + fle for fle in os.listdir(config.frames_path) if fle != '.DS_Store']

# In[]: 

def generate_figure_html(html_file):
    with open(html_file, "r") as f:
        figure_html = f.read()
    return figure_html

# In[]: 

app.layout = html.Div([
    html.H1("Plotly Figures"),
    html.Div(id='figures'),
    dcc.Interval(
        id='interval-compontent',
        interval=60*1000, #in milliseconds (1 min)
        n_intervals=0
    )
])

# In[]: 

@app.callback(
    Output("figures", "children"),
    Input("interval-compontent", "n_intervals")
)
def update_figures(n_intervals):
    figure_divs = []
    for file in html_file:
        figure_html = generate_figure_html(file)
        figure_divs.append(
            html.Div(
                [
                    html.Iframe(srcDoc=figure_html, width="50%", height="600")
                ]
            )
        )
    return figure_divs

# In[]: 

if __name__ == "__main__":
    app.run_server(debug=True)