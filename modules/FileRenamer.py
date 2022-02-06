#!/usr/bin/python3
import os
import unidecode


class FileRenamer:

    def __init__(self, replace_spaces=True, recursive=False, files=True, directories=True, ignored_names=[]):
        self.replace_spaces = replace_spaces
        self.recursive = recursive
        self.files = files
        self.directories = directories
        self.ignored_names = ignored_names

    def check_if_path_should_be_skipped(self, path):
        for ignored_name in self.ignored_names:
            if ignored_name in path:
                return True
        return False

    def generate_new_path(self, old_path):
        new_path = old_path
        if self.replace_spaces:
            new_path = new_path.replace(' ', '_')
        new_path = unidecode.unidecode(new_path)
        return new_path

    def rename_files(self):
        current_directory = os.getcwd()
        for root, directories, filenames in os.walk(current_directory):
            for filename in filenames:
                path = os.path.join(root, filename)
                if not self.check_if_path_should_be_skipped(path):
                    new_filename = self.generate_new_path(filename)
                    new_path = os.path.join(root, new_filename)
                    if path != new_path:
                        print(f"Renaming: {path} -> {new_path}")
                        os.rename(path, new_path)
            if not self.recursive:
                break

    def rename_folders(self):
        current_directory = os.getcwd()
        for root, directories, filenames in os.walk(current_directory, topdown=False):
            for directory in directories:
                path = os.path.join(root, directory)
                if not self.check_if_path_should_be_skipped(path):
                    new_dirname = self.generate_new_path(directory)
                    new_path = os.path.join(root, new_dirname)
                    if path != new_path:
                        print(f"Renaming: {path} -> {new_path}")
                        try:
                            os.rename(path, new_path)
                        except PermissionError:
                            print(f"Permission error when renaming {path}")
            if not self.recursive:
                break

    def rename(self):
        if self.files:
            self.rename_files()
        if self.directories:
            self.rename_folders()
