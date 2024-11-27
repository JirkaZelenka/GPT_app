from datetime import datetime, timedelta
from dash.dependencies import Input, Output, State
from dash import dcc, html

def register_callbacks(app, runner, data):
    
    @app.callback(
        [Output('output-data-length', 'children'),
        Output('data-table', 'data')
        ],
        Input('refresh-data-button', 'n_clicks'),
    )
     
    def refres_number_of_records(n_clicks):
        
        if n_clicks > 0:
            current_time = datetime.now()
            message = f"Currently, {current_time}, there are {len(data)} records loaded."
            return message, data.to_dict('records')
                
        else:
            return 'No clicks yet', []
            
          