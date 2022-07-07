import psutil
import pynvml
import dash
from dash.dependencies import Input, Output
import dash_daq as daq
from dash import dcc
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([

    # first row
    html.Div(children=[

        # first column of first row
        html.Div(children=[

            daq.Gauge(
                id='my-gauge-1',
                # color="#76b900",
                size=200,
                color={"gradient": True, "ranges": {
                    "green": [0, 69], "yellow":[69, 85], "red":[85, 100]}},
                showCurrentValue=True,
                units="C",
                label="CPU Temp",
                min=0,
                max=100,
                value=50
            ),
            dcc.Interval(
                id='interval-component-1',
                interval=1*1000,  # in milliseconds
                n_intervals=0
            )

        ], style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '3vw', 'margin-top': '3vw'}),

        # second column of first row
        html.Div(children=[

            daq.Gauge(
                id='my-gauge-2',
                # color="#76b900",
                size=200,
                color={"gradient": True, "ranges": {
                    "green": [0, 69], "yellow":[69, 85], "red":[85, 100]}},
                showCurrentValue=True,
                units="C",
                label="GPU Temp",
                min=0,
                max=100,
                value=50
            ),
            dcc.Interval(
                id='interval-component-2',
                interval=1*1000,  # in milliseconds
                n_intervals=0
            )

        ], style={'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '3vw', 'margin-top': '3vw'}),

    ], className='row'),
])


@app.callback(Output('my-gauge-1', 'value'),
              Input('interval-component-1', 'n_intervals'))
def update_output(value):
    cpu_temp = ((psutil.sensors_temperatures()['k10temp'][1]).current)
    return cpu_temp


@app.callback(Output('my-gauge-2', 'value'),
              Input('interval-component-2', 'n_intervals'))
def update_output(value):
    pynvml.nvmlInit()  # initialization
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)
    gpuTemperature = pynvml.nvmlDeviceGetTemperature(
        handle, 0)  # Reading temperature
    gpu_temp = gpuTemperature
    return gpu_temp


if __name__ == "__main__":
    app.run_server(debug='False', port=8050,host='0.0.0.0')