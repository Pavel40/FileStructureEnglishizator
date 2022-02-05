#!/usr/bin/python3
import os


class PathFinder:

    def __init__(self, start_directory, recursive=False):
        self.recursive = recursive
        self.start_directory = start_directory

    def get_paths(self):
        paths = {
            'directories': [],
            'files': []
        }

        for root, directories, filenames in os.walk(self.start_directory):
            for directory in directories:
                path = os.path.join(root, directory)
                paths['directories'].append(path)
            for filename in filenames:
                path = os.path.join(root, filename)
                paths['files'].append(path)
            if not self.recursive:
                break

        return paths
