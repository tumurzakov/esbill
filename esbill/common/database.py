import orjson as json

class Database:

    def save(self, entity):
        pass

class JsonDatabase(Database):
    def read_all(self, collection):
        try:
            with open(f"db/{collection}.json", 'r') as f:
                return json.loads(f.read())
        except:
            return {}

    def write_all(self, collection, entries):
        with open(f"db/{collection}.json", 'wb') as f:
            return f.write(json.dumps(entries))

    def save(self, collection, obj):
        entries = self.read_all(collection)
        entries[str(obj['id'])] = obj
        self.write_all(collection, entries)

    def read(self, collection, obj):
        entries = self.read_all(collection)
        return entries[str(obj['id'])]

