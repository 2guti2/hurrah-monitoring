from server import create_app
import os

default_port = 5000
host = '0.0.0.0'

app = create_app()
port = int(os.environ.get('PORT', default_port))

is_development = app.config.get('DEVELOPMENT')

if is_development:
    app.run(debug=True)
else:
    app.run(host=host, port=port, threaded=True)
