import re
import os
import requests

skipped_files = []


# Not my own code. Stole this from Stackoverflow. Thanks Alexander McFarlane.
def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location_download = winreg.QueryValueEx(key, downloads_guid)[0]
        return location_download
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


# Also from stack btw. I couldn't note the name.
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)


def create_directories(directory_path_list, download_folder):
    for i in directory_path_list:
        if os.path.exists(os.path.join(download_folder, i)):
            print(f'{i} exists')
        else:
            os.mkdir(os.path.join(download_folder, i))
            print(f'Created folder {i}')


def download_files(url, location_file):
    print(f'Downloading file {location_file}')
    retried = False
    try:
        r = requests.get(url, timeout=None)
        r.raise_for_status()
        downloaded_file = open(location_file, 'wb')
        for chunk in r.iter_content(100000):
            downloaded_file.write(chunk)
        print(f'Downloaded {location_file}')
        if [url, location_file] in skipped_files:
            skipped_files.remove([url, location_file])
    except Exception as e:
        print("File was skipped.")
        if not [url, location_file] in skipped_files:
            skipped_files.append([url, location_file])


def downloader_main():
    folder_names = []
    file_names = []
    folder_file = open('tempFolder.txt', 'r')
    file_file = open('tempFile.txt', 'r')

    sub_string = '%20'

    folder_urls = folder_file.read().split('\n')
    file_urls = file_file.read().split('\n')
    file_urls.pop()
    folder_urls.pop()

    for j in range(len(file_urls)):
        file_urls[j] = re.sub('\?a=view$', '', file_urls[j])

    for i in file_urls:
        location = find_all(i, sub_string)
        file_names.append(i.replace('%20', ' '))
        file_names[file_urls.index(i)] = re.sub('^(https://ddl2.finisher.site/|https://scarlet2.finisher.site/)', '',
                                                file_names[file_urls.index(i)])
        file_names[file_urls.index(i)] = re.sub(':', '-', file_names[file_urls.index(i)])
        file_names[file_urls.index(i)] = re.sub('\?', '', file_names[file_urls.index(i)])

    for i in folder_urls:
        location = find_all(i, sub_string)
        folder_names.append(i.replace('%20', ' '))
        folder_names[folder_urls.index(i)] = re.sub('^(https://ddl2.finisher.site/|https://scarlet2.finisher.site/)',
                                                    '', folder_names[folder_urls.index(i)])
        folder_names[folder_urls.index(i)] = folder_names[folder_urls.index(i)].strip('\n')
        folder_names[folder_urls.index(i)] = re.sub(':', '-', folder_names[folder_urls.index(i)])

    custom_path = input(
        '\nDefault is the Downloads folder\n. Do you want to set a custom path for the download?\n').lower()

    if custom_path == 'y':
        while True:
            download_location = input('Enter the location (e.g D:/Games/)\n')
            if os.path.exists(download_location):
                break
            else:
                print('Enter a VALID path.')

    else:
        download_location = get_download_path()

    create_directories(folder_names, download_location)

    for i in range(len(file_urls)):
        download_files(file_urls[i], os.path.join(download_location, file_names[i]))

    retry_number = 0
    index_retry = 0
    while skipped_files:
        for i in skipped_files:
            print(f'\nskipped files were found, retrying them.')
            print(i)
            download_files(i[0], i[1])
        print(f'retry_number {retry_number}')
        if retry_number > 2:
            print('Some files remain skipped. Something bad must have happened.')
            break
        retry_number += 1

    f = open('debug_file.txt', 'w+')
    for i in skipped_files:
        f.write(str(i) + '\n')
    print('You can check debug_file.txt for the file')
