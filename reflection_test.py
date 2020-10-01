import glob
models = []
for name in glob.glob('application/**/*_module.py'):
    models.append(name.replace('/', '.'))
print(models)
