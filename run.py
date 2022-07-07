import dash
from dash.dependencies import Input, Output
import dash_daq as daq
from dash import dcc
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    daq.Gauge(
        id='my-gauge-1',
        label="GPU Temp",
        min=0,
        max=100,
        value=50,
    ),
    dcc.Interval(
            id='interval-component',
            interval=1*1000,  # in milliseconds
            n_intervals=0
    )
])


@app.callback(Output('my-gauge-1', 'value'),
              Input('interval-component', 'n_intervals'))
def update_output(value):
    return value


if __name__ == '__main__':
    app.run_server(debug=True)
