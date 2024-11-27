from dash import dcc, html
import datetime as dt
from dash import dash_table

def create_layout():
    layout = html.Div([
        dcc.Location(id='url', refresh=False),

        html.Div([
            html.Div([                
                html.Img(
                    src="https://some_logo.png",
                    style={
                        'height': '40px',
                        'margin-right': '15px',
                        'vertical-align': 'middle'
                    }
                ),
                dcc.Link('Page 1', href='/page_1', className='nav-link'),
                html.Span("    |    ", className='separator'),
                dcc.Link('Page 2', href='/page_2', className='nav-link'),
                html.Span("    |    ", className='separator'),
                dcc.Link('Page 3', href='/page_3', className='nav-link'),
            ], style={
                'display': 'flex',
                'align-items': 'center',
                'background-color': '#000000',  # Dark blue background
                'padding': '10px 20px'
            }),
        ]),

        html.Div(id='page-content')
    ])

    return layout

def create_layout_1():
    layout = html.Div([
        
        html.H1("Page 1 - Intro?"),
        
        html.H2("Here I want "),
        
        html.Div([
            html.Button("Get Length of loaded data", 
                        id='refresh-data-button', 
                        n_clicks=0,
                        style={
                            'padding': '10px 20px',       
                            'fontSize': '18px',           
                            'backgroundColor': '#007BFF', 
                            'color': 'white',             
                            'border': 'none',             
                            'borderRadius': '8px',        
                            'cursor': 'pointer',          
                            'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.2)',  
                            'transition': 'background-color 0.3s ease' 
                        },
            )],
        style={'margin-top': '10px'}
        ),
        
        html.Div(id='output-data-length', 
                style={'margin-top': '20px'}),
        
        html.Div([      
            dash_table.DataTable(
            id='data-table',
            columns=[
                {"name": "Name", "id": "name"},
                {"name": "Age", "id": "age"},
                {"name": "Email", "id": "email"},
                {"name": "Date of Creation", "id": "created_at"},
                {"name": "Is active", "id": "is_active"},
                ],
            )]
        )
        
    ])
    return layout

def create_layout_2():
    layout = html.Div([
        
        html.H1("Page 2 - Something"),
        
        html.H2("Here I want "),
    ])
    return layout

def create_layout_3():
    layout = html.Div([
        
        html.H1("Page 3 - Something else"),
        
        html.H2("Here I want .. "),
    ])
    return layout
