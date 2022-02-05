#!/usr/bin/python3
import os
import zipfile

from modules.PathFinder import PathFinder

class Backuper:
    
    def __init__(self, backup_name = 'backup', recursive = False):
        self.backup_name = backup_name
        self.recursive = recursive
        self.paths_to_backup = None

    def generate_paths_to_backup(self):
        self.paths_to_backup = []
        current_directory = os.getcwd()
        pathfinder = PathFinder(current_directory, self.recursive)
        paths = pathfinder.get_paths()
        self.paths_to_backup = paths['files'] + paths['directories']
    
    def make_backup(self):
        if self.paths_to_backup is None:
            self.generate_paths_to_backup()
 
        with zipfile.ZipFile(f"{self.backup_name}.zip", 'w') as zip:
            for path in self.paths_to_backup:
                relative_path = os.path.relpath(path)
                zip.write(path, relative_path)
