import dash
import psutil
from dash.dependencies import Input, Output
import dash_daq as daq
from dash import dcc
from dash import html

# cpu_temp = psutil.sensors_temperatures()['k10temp'][1]
# cpu_current_temp = str(cpu_temp.current)
# cpu_load = str(psutil.cpu_percent(interval=None))

app = dash.Dash(__name__)

app.layout = html.Div([
    daq.Gauge(
        id='my-gauge-1',
        color="#76b900",
        showCurrentValue=True,
        units="C",
        label="CPU Temp",
        min=0,
        max=100,
        value=50
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
    cpu_temp = ((psutil.sensors_temperatures()['k10temp'][1]).current)
    return cpu_temp


if __name__ == '__main__':
    app.run_server(debug=True)
