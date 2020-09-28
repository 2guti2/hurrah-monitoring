from server import create_app


def run():
    app = create_app()
    if app.config.get('DEVELOPMENT'):
        app.run(debug=True)
    else:
        app.run(host='0.0.0.0', port=app.config.get('PORT'), threaded=True)


if __name__ == '__main__':
    run()
