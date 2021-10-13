#import wget
import os
import requests
from zipfile import ZipFile

user = input('Repl.it Username: ')
prefix = input('Files prefix: ')
base = f'https://repl.it/@{user}/{prefix}'
number_of_files = int(input('Number of files: '))
extract = input('Extract Y/n: ').strip().upper()
path = '/home/samuel/Documentos/Scripts/'

if extract == 'N':
    extract = False
else:
    extract = True

for c in range(1, number_of_files + 1):

    if c < 10:
        mid = '0' + str(c)
    else:
        mid = str(c)

    url = base + mid + '.zip'
    file_name = prefix + mid + '.zip'
    resp = requests.get(url)
    fd = open(file_name, 'wb')

    fd.write(resp.content)
    fd.close()

    print(f'File {file_name} download successful.')

    if extract:
        new_file_name = file_name.replace('.zip', '') + '.py'

        with ZipFile(path + file_name, 'r', allowZip64=False) as zip:
            
            zip.extract('main.py', path=path)
            print(f'{file_name} extracted successfuly.')
        
        os.rename(path + 'main.py', path + new_file_name)

print('Done!')
