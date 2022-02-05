#!/usr/bin/python3

from modules.Backuper import Backuper
from modules.ConfigLoader import ConfigLoader
from modules.FileRenamer import FileRenamer


def main():
    config_loader = ConfigLoader()
    config_loader.load_from_json()
    config = config_loader.get_config()

    print('Loaded config:')
    for key in config:
        print(f"{key}: {config[key]}")
    if config['confirm_required']:
        proceed = input('Proceed (y/n): ')
        if proceed != 'y':
            exit()

    if config['backup']:
        print('Creating backup...')
        backuper = Backuper(config['backup_name'], config['recursive'])
        backuper.make_backup()
        print('Backup created.')

    file_renamer = FileRenamer(
        config['replace_spaces'], config['recursive'], config['files'], config['directories'], config['ignored_names'])
    file_renamer.rename()

    print('Done!')


if __name__ == "__main__":
    main()
