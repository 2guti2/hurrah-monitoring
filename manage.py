from application import create_app
from flask_migrate import MigrateCommand, Manager
import glob
import importlib.util

manager = Manager(create_app)
manager.add_command('db', MigrateCommand)


# make SqlAlchemy detect the models
def import_models():
    for model_name in glob.glob('application/**/models/[!_]*'):
        spec = importlib.util.spec_from_file_location(
            '.'.join(model_name.replace('.py', '').split('/')),
            f'./{model_name}'
        )
        model = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(model)


import_models()

# DOCS
# https://flask-migrate.readthedocs.io/en/latest/

if __name__ == '__main__':
    manager.run()
