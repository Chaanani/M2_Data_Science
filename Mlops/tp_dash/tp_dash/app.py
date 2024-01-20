# import numpy as np
import pandas as pd
import plotly.express as px
from joblib import load
import numpy as np
# import plotly.express as px

import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, dcc


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

linear_model = load("linear_model.joblib")
df = pd.read_csv("new_data.csv")

app.layout = html.Div(children=[
    #######################
    html.H6("Saisissez le texte de votre choix ci-dessous :"),
    html.Div(["Input: ", dcc.Input(id='my-input', value='toto', type='text')]),
    html.Br(),
    html.Div(id='my-output'),
    #####################
    html.Hr(),
    html.H6("Select a column for X-axis:"),
    dcc.Dropdown( id='column-dropdown', options=[{'label': col, 'value': col} for col in df.columns], value=df.columns[0]),
    html.Div(id='scatter-plot-container'),
    ############################
    
    html.Hr(),
    html.H6("Select values for prediction:"),
    html.Div([dbc.Row([
            dbc.Col(dcc.Slider(min=0, max=100, step=10, value=50, id='slider-x0')),
            dbc.Col(dcc.Slider(min=0, max=100, step=10, value=50, id='slider-x1')),
            dbc.Col(dcc.Slider(min=0, max=100, step=10, value=50, id='slider-x2'))])]),
    html.Div(id='prediction-output'),
    ##################################
    html.Hr(),
    html.H6("Histograme"),
    html.Div(id='histogram-container'),


    ])


@app.callback( Output(component_id='my-output', component_property='children'), Input(component_id='my-input', component_property='value'))
def update_output_div(input_value):
    return f'Output: {input_value}'

@app.callback(Output('scatter-plot-container', 'children'), [Input('column-dropdown', 'value'), Input('slider-x0', 'value'),Input('slider-x1', 'value'), Input('slider-x2', 'value')])
def update_scatter_plot(selected_column, x0, x1, x2):
    y_pred = linear_model.predict(np.array([x0, x1, x2]).reshape(1,-1))
    fig = px.scatter(df, x=selected_column, y='y')
    xi_value = df[selected_column].iloc[-1]  
    fig.add_scatter(x=[xi_value], y=[y_pred], mode='markers', marker_color='green', marker=dict(color='green', size=10), name='Prediction')
    return dcc.Graph(figure=fig)

@app.callback( Output('prediction-output', 'children'), [Input('slider-x0', 'value'), Input('slider-x1', 'value'), Input('slider-x2', 'value')])
def update_prediction(x0, x1, x2):
    prediction = linear_model.predict([[x0, x1, x2]])
    return f'Predicted y: {prediction[0]}'

@app.callback( Output('histogram-container', 'children'), Input('column-dropdown', 'value'))
def update_histogram(selected_column):
    fig = px.histogram(df, x=selected_column)
    return dcc.Graph(figure=fig)


    


# 2. Définir un 2e callback permettant, à partir des valeurs de X0, X1, X2
# choisies avec 3 sliders placés dans le layout ci-dessus
# de calculer la prévision de y correspondante (en utilisant linear_model)
# et de l'afficher dans le dashboard

# Questions subsidiaires :
# 3. Tracer un histogramme de Xi (selon le choix du dropdown utilisé en 1.)
#
# 4. Modifier le graphe du 1er callback pour qu'il affiche le point (Xi, y_pred),
# où y_pred est calculé dans la question 2.
#
# 5. Aligner les 3 sliders sur la même ligne


if __name__ == '__main__':
    app.run_server(debug=True)
