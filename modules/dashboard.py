import dash
from dash import dcc, html, Input, Output
import plotly.express as px

def create_dashboard(data):

    app = dash.Dash(__name__)

    cities = data['City'].unique()

    # Auto detect numeric columns
    numeric_cols = data.select_dtypes(include='number').columns[:3]

    app.layout = html.Div([
        html.H2("Indian Climate Interactive Dashboard"),

        dcc.Dropdown(
            id='city',
            options=[{'label': c, 'value': c} for c in cities],
            value=cities[0]
        ),

        dcc.Graph(id='climate_graph')
    ])

    @app.callback(
        Output('climate_graph', 'figure'),
        Input('city', 'value')
    )
    def update_graph(city):
        df = data[data['City'] == city]

        df_melt = df.melt(
            id_vars='Date',
            value_vars=numeric_cols,
            var_name='Parameter',
            value_name='Value'
        )

        fig = px.line(
            df_melt,
            x='Date',
            y='Value',
            color='Parameter',
            title=f"Climate Trend - {city}"
        )

        return fig

    return app
