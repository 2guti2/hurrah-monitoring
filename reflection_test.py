import glob
models = []
for name in glob.glob('server/**/*_module.py'):
    models.append(name.replace('/', '.'))
print(models)
