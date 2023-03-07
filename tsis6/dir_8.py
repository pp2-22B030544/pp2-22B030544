import os


fpath = '1.py'
# print(fpath)
print(
    os.path.join(
        os.getcwd(),
        'tsis6',
        fpath,
    )
)
os.remove('1.py')
# print(os.path.abspath(fpath))
if os.path.exists(fpath):
    os.remove(fpath)
    print('del file')