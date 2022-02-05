#!/usr/bin/python3
import json

class ConfigNotSetError(Exception): pass

class ConfigLoader:

    def __init__(self, json_path='config.json'):
        self.json_path = json_path
        self.__config = None

    def load_from_json(self):
        try:
            with open(self.json_path, 'r', encoding='utf-8') as f:
                self.__config = json.load(f)
        except json.JSONDecodeError:
            print(f"Error loading JSON config {self.json_path}. Using default config.")
            self.__config = {
                'ignored_names': [],
                'files': True,
                'directories': True,
                'recursive': False,
                'backup': True,
                'backup_name': 'backup',
                'replace_spaces': True,
                'confirm_required': True
            }

    def get_config(self):
        if self.__config is None:
            raise ConfigNotSetError
        return self.__config
