import os
import warnings

from apps.layout import create_layout, create_layout_1, create_layout_2, create_layout_3
from apps.callbacks import register_callbacks
import dash
import dash_auth

from apps.run import Runner

from dotenv import load_dotenv
load_dotenv()
username = os.getenv("APP_USERNAME")
password = os.getenv("APP_PASSWORD")

VALID_USERNAME_PASSWORD_PAIRS = {
    username: password
    }

runner = Runner()
data = runner.data_manager.get_all_data_as_df()
print(f"LOADED SOME DATA: {len(data)}")

app = dash.Dash(__name__, suppress_callback_exceptions=True)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS,
    secret_key="Whatever_makes_the_dash_happy!123",
)

app.layout = create_layout()

register_callbacks(app, runner, data) 

@app.callback(
    dash.dependencies.Output('page-content', 'children'),
    dash.dependencies.Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/page_1':
        return create_layout_1()
    elif pathname == '/page_2':
        return create_layout_2()
    elif pathname == '/page_3':
        return create_layout_3()
   
if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port=8050)
