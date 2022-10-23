import json


class Exporter:

    def __init__(self):
        self.filename = 'taski.json'

    def save_tasks(self, tasks):
        with open(self.filename, 'w', encoding='utf8') as f:
            json.dump(tasks, f, indent=True, ensure_ascii=False)
