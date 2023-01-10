from flaskwebgui import FlaskUI
from main import app


FlaskUI(app, start_server='flask', maximized=True,fullscreen=False,
        close_server_on_exit=False, host="localhost", port=1234,).run()
