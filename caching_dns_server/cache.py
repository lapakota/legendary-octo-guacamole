import time


class Cache:
    def __init__(self, filename):
        self.filename = filename
        self.data = dict()

    def read_cache(self):
        with open(self.filename) as f:
            for line in f.readlines():
                line = line.rstrip('\n').split()
                if not line:
                    break
                name = line[0]
                if name not in self.data:
                    self.data[name] = dict()
                self.data[name][int(line[1])] = line[2:]
        expired = []
        for i in self.data.keys():
            for j in self.data[i].keys():
                if float(self.data[i][j][2]) <= time.time():
                    expired.append(i)
        if expired:
            print(f'Expired:')
        for i in expired:
            print(i)
            del self.data[i]
        if expired:
            self.update_cache()
            print('\n')

        if self.data:
            print('Available cache:')
            [print(i, j) for i, j in zip(self.data.keys(), self.data.values())]
        else:
            print('Cache is empty\n')

    def update_cache(self):
        with open(self.filename, 'w') as f:
            updated_data = {}
            for k, v in self.data.items():
                for u, d in v.items():
                    if float(d[2]) > time.time():
                        f.write(f'{k} {u} {" ".join(map(str, d))}\n')
                        if k not in updated_data.keys():
                            updated_data[k] = dict()
                        updated_data[k][int(u)] = d
        self.data = updated_data

    def add_record(self, name, rtype, data):
        if name not in self.data.keys():
            self.data[name] = dict()
        self.data[name][rtype] = data
        self.update_cache()
