import json, datetime, urllib.request


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target
        self.filename = 'ratios.json'
        self.date = str(datetime.date.today())
        self.url = f'https://api.exchangerate.host/convert?from={base}&to={target}'

    def was_ratio_saved_today(self):
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise
        with open(self.filename, 'r') as f:
            data = json.load(f)
            for conversion in data:
                if self.base == conversion['base_currency'] and \
                        self.target == conversion['target_currency'] and \
                        self.date == conversion['date_fetched']:
                    return True
            return False

    def fetch_ratio(self):
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it
        with urllib.request.urlopen(self.url) as f:
            data = json.loads(f.read().decode('utf-8'))
        self.save_ratio(data['result'])

    def save_ratio(self, ratio):
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        with open(self.filename, 'r') as f:
            data = json.load(f)
            for conversion in data:
                if self.base == conversion['base_currency'] and \
                        self.target == conversion['target_currency']:
                    data[data.index(conversion)]['ratio'] = ratio
                    data[data.index(conversion)]['date_fetched'] = self.date
                    break
                if data[-1] == conversion:
                    data.append({
                        "base_currency": self.base,
                        "target_currency": self.target,
                        "date_fetched": self.date,
                        "ratio": ratio
                    })
            with open(self.filename, 'w') as g:
                json.dump(data, g, indent=True)

    def get_matched_ratio_value(self):
        # Should read file and receive exchange rate for given base and target currency from that file
        with open(self.filename, 'r') as f:
            data = json.load(f)
            for conversion in data:
                if self.base == conversion['base_currency'] and \
                        self.target == conversion['target_currency'] and \
                        self.date == conversion['date_fetched']:
                    return conversion['ratio']

