from server import create_app
from flask_migrate import MigrateCommand, Manager
import glob

manager = Manager(create_app)
manager.add_command('db', MigrateCommand)


# make SqlAlchemy detect the models
def import_models():
    for model_name in glob.glob('server/**/models/[!_]*'):
        all_path = model_name.replace('.py', '').split('/')
        module_name = '.'.join(all_path)
        import importlib.util
        spec = importlib.util.spec_from_file_location(module_name, f'./{model_name}')
        model = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(model)


import_models()

# DOCS
# https://flask-migrate.readthedocs.io/en/latest/

if __name__ == '__main__':
    manager.run()
