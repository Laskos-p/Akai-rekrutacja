import json


class Importer:

    def __init__(self):
        self.filename = 'taski.json'
        self.data = {}

    def read_tasks(self):
        with open(self.filename, 'r', encoding='utf8') as f:
            self.data = json.load(f)

    def get_tasks(self):
        return self.data
