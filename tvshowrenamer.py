from os import listdir, rename

from time import sleep
from random import randint

print('''
***********************************
*                                 *
*   File Renamer to PLEX format   *
*                                 *
***********************************
''')

path = input('Enter path: ').replace('\\', '/').rstrip('/')

show_name = path[27:path.find('Season') - 1]
forced = ['forced', 'Forced', 'FORCED']
renamed_files = 0
unchanged_videos = 0
unchanged_subs = 0
unknown = 0
reads = 0

for countdown in range(3, 0, - 1):
    color = randint(1, 7)
    print(f'\033[3{color}mStarting in {countdown}\033[m')
    sleep(1)

print()

for original_name in listdir(path):
    file_name = original_name.lower()

    if 's0' in file_name:
        episode_info = file_name[file_name.find(
            's0'):file_name.find('s0') + 6].upper()
    elif 't0' in file_name:
        episode_info = 'S' + \
            file_name[file_name.find(
                't0') + 1:file_name.find('t0') + 6].upper()
    else:
        episode_info = ''

    file_extension = file_name[-4:]

    if file_extension == '.srt' and 'forced' in file_name and not '.en' in file_name:
        file_extension = '.pt-BR.forced.srt'

    elif file_extension == '.srt' and not '.en' in file_name:
        file_extension = '.pt-BR.srt'

    elif '.en' in file_name and 'forced' in file_name:
        file_extension = '.en.forced.srt'

    elif '.en' in file_name:
        file_extension = '.en.srt'

    elif file_extension == '.srt':
        file_extension = '.pt-BR.srt'

    elif file_extension in ['.mkv', '.mp4', '.avi', '.rmvb']:
        pass

    else:
        file_extension = ''

    final_name = f'{show_name} - {episode_info}{file_extension}'

    if original_name == final_name and '.srt' in file_extension:
        print(f'{original_name}\033[32m no alteration needed\033[m')
        unchanged_subs += 1

    elif original_name == final_name:
        print(f'{original_name}\033[32m no alteration needed\033[m')
        unchanged_videos += 1

    else:
        print(f'{original_name}\033[32m renamed to \033[m{final_name}.')
        renamed_files += 1

    reads += 1

    if episode_info == '' or file_extension == '' or episode_info == '':
        unknown += 1
        print(f'{original_name}\033[31m missing information\033[m')
        continue

    path_to_file = path + '/' + original_name
    path_to_renamed_file = path + '/' + final_name
    rename(path_to_file, path_to_renamed_file)

    sleep(0.5)

print(f'''
RESULTS:
{reads} files/folders readed
{renamed_files} files renamed
{unchanged_videos} videos unchanged
{unchanged_subs} subtitles unchanged''')

sleep(0.5)

print('''\033[32m
DONE!
\033[m''')
