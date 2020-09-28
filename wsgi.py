from server import create_app
import os

default_port = 5000
host = '0.0.0.0'

app = create_app()
port = int(os.environ.get('PORT', default_port))

if __name__ == '__main__':
    env = os.environ.get('ENV', 'development')
    if env == 'development':
        app.run(debug=True)
    else:
        app.run(host=host, port=port, threaded=True)
