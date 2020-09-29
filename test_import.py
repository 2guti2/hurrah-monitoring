import glob
models = []
for name in glob.glob('server/**/models'):
    models.append(name.replace('/', '.'))
print(models)
